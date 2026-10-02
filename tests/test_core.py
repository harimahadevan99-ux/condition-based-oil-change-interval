import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import unittest
from simulate import history
from core import plan


class T(unittest.TestCase):
    def test_light_duty_extends(self):
        self.assertGreater(plan(history(1.0))["recommended_change_h"], 500)

    def test_severe_duty_shortens(self):
        r = plan(history(2.2))
        self.assertLess(r["recommended_change_h"], 500)
        self.assertEqual(r["verdict"], "change earlier than fixed interval")


if __name__ == "__main__":
    unittest.main()
