"""Creative Console 001: stdlib + Pillow deterministic neutral renderer."""
import copy, hashlib, io, json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
REGION = (60, 100, 540, 190)

def fixture_bytes():
    im = Image.new('RGB', (600, 750), '#F3F0E8')
    d = ImageDraw.Draw(im)
    d.rectangle((60, 230, 540, 232), fill='#B4AFA6')
    buf = io.BytesIO(); im.save(buf, format='PNG'); return buf.getvalue()

def fixture_sha(): return hashlib.sha256(fixture_bytes()).hexdigest()

def validate(state):
    if state['schemaVersion'] != '1.0.0' or state['canvas'] != {'width':600,'height':750,'background':'#F3F0E8'}:
        raise ValueError('incompatible state')
    if state['assets'][0]['sha256'] != fixture_sha() or state['assets'][0]['id'] != 'asset-neutral-01':
        raise ValueError('asset mismatch')
    if state['template'] != {'id':'neutral-card','version':'1.0.0'} or state['renderer'] != {'id':'pillow-v1','version':'1.0.0'}:
        raise ValueError('renderer/template mismatch')
    if len(state['layers']) != 2 or state['layers'][0] != {'id':'background','kind':'image','assetId':'asset-neutral-01','approved':True,'locked':True}:
        raise ValueError('background changed')
    accent=state['layers'][1]
    if set(accent) != {'id','kind','visible','fill','bounds','approved','locked'} or accent['id']!='accent' or accent['kind']!='rectangle' or accent['bounds'] != [60,100,480,90] or not isinstance(accent['visible'],bool) or accent['locked'] or accent['approved'] or not isinstance(accent['fill'],str) or len(accent['fill'])!=7 or accent['fill'][0]!='#' or any(c not in '0123456789ABCDEFabcdef' for c in accent['fill'][1:]):
        raise ValueError('invalid accent')
    if not isinstance(state['revision'],int) or state['revision']<1: raise ValueError('invalid revision')
    return True

def change_fill(state, new_fill, expected_revision):
    validate(state)
    if state['revision'] != expected_revision: raise ValueError('stale revision')
    if state['layers'][1]['approved'] or state['layers'][1]['locked']: raise ValueError('locked')
    updated=copy.deepcopy(state); updated['layers'][1]['fill']=new_fill; updated['revision']+=1
    validate(updated)
    return updated

def render(state):
    validate(state)
    im=Image.open(io.BytesIO(fixture_bytes())).convert('RGB')
    accent=state['layers'][1]
    if accent['visible']:
        x,y,w,h=accent['bounds']; ImageDraw.Draw(im).rectangle((x,y,x+w-1,y+h-1),fill=accent['fill'])
    buf=io.BytesIO(); im.save(buf,format='PNG'); return buf.getvalue()

def main():
    state=json.loads((ROOT/'neutral-state.json').read_text())
    (ROOT/'fixtures').mkdir(exist_ok=True)
    (ROOT/'fixtures'/'neutral.png').write_bytes(fixture_bytes())
    (ROOT/'render-original.png').write_bytes(render(state))
    changed=change_fill(state,'#B36A48',state['revision'])
    (ROOT/'render-changed.png').write_bytes(render(changed))
    print('fixture sha256:',fixture_sha())
    print('original render sha256:',hashlib.sha256(render(state)).hexdigest())
    print('changed render sha256:',hashlib.sha256(render(changed)).hexdigest())

if __name__=='__main__': main()
