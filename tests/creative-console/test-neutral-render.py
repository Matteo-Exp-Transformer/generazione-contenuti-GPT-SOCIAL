import copy, hashlib, importlib.util, json, unittest
from pathlib import Path
from PIL import Image
import io
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('neutral_renderer',ROOT/'neutral-render.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

class ContractTests(unittest.TestCase):
    def setUp(self): self.state=json.loads((ROOT/'neutral-state.json').read_text())
    def test_repeatable(self): self.assertEqual(hashlib.sha256(r.render(self.state)).digest(),hashlib.sha256(r.render(self.state)).digest())
    def test_single_property(self):
        updated=r.change_fill(self.state,'#B36A48',1)
        old=copy.deepcopy(self.state); old['layers'][1]['fill']='#B36A48';old['revision']=2
        self.assertEqual(updated,old)
    def test_diff_localized(self):
        a=Image.open(io.BytesIO(r.render(self.state))).convert('RGB')
        b=Image.open(io.BytesIO(r.render(r.change_fill(self.state,'#B36A48',1)))).convert('RGB')
        changed=[(x,y) for y in range(a.height) for x in range(a.width) if a.getpixel((x,y))!=b.getpixel((x,y))]
        self.assertEqual(len(changed),480*90)
        self.assertTrue(all(60<=x<540 and 100<=y<190 for x,y in changed))
    def test_snapshot_restore(self):
        snapshot=json.dumps(self.state,sort_keys=True)
        modified=r.change_fill(self.state,'#B36A48',1)
        self.assertNotEqual(json.dumps(modified,sort_keys=True),snapshot)
        self.assertEqual(json.dumps(json.loads(snapshot),sort_keys=True),snapshot)
        self.assertEqual(r.render(json.loads(snapshot)),r.render(self.state))
    def test_locked_and_stale(self):
        s=copy.deepcopy(self.state);s['layers'][1]['locked']=True
        with self.assertRaises(ValueError):r.change_fill(s,'#B36A48',1)
        with self.assertRaises(ValueError):r.change_fill(self.state,'#B36A48',0)
    def test_tampered_asset(self):
        s=copy.deepcopy(self.state);s['assets'][0]['sha256']='0'*64
        with self.assertRaises(ValueError):r.render(s)

if __name__=='__main__':unittest.main()
