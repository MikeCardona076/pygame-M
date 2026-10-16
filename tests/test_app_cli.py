import unittest
from contextlib import redirect_stdout
from io import StringIO

from pygame_m.app import main


class AppCliTests(unittest.TestCase):
    def test_help_lists_basic_commands(self) -> None:
        output = StringIO()

        with self.assertRaises(SystemExit) as error, redirect_stdout(output):
            main(["--help"])

        self.assertEqual(error.exception.code, 0)
        self.assertIn("Comandos basicos:", output.getvalue())
        self.assertIn("python -m pygame_m --version", output.getvalue())

    def test_version_prints_installed_version(self) -> None:
        output = StringIO()

        with self.assertRaises(SystemExit) as error, redirect_stdout(output):
            main(["--version"])

        self.assertEqual(error.exception.code, 0)
        self.assertIn("pygame-m 0.1.0", output.getvalue())


if __name__ == "__main__":
    unittest.main()
