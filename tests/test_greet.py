import importlib.util
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "src" / "greet.py"
spec = importlib.util.spec_from_file_location("swarm26_greet", SOURCE)
assert spec is not None
assert spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
greet = module.greet


class GreetTests(unittest.TestCase):
    def test_greet_uses_welcome(self):
        self.assertEqual(greet("Waggle"), "Welcome, Waggle!")
