import unittest
from main import run
class TestRun(unittest.TestCase):
 def test_smoke(self):
  self.assertIsNotNone(run([], []))
if __name__=="__main__": unittest.main()
