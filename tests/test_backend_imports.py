import unittest


class BackendImportTests(unittest.TestCase):
    def test_main_module_imports(self):
        from Backend.main import app

        self.assertIsNotNone(app)


if __name__ == "__main__":
    unittest.main()
