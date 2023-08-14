import unittest

class TestImportModules(unittest.TestCase):

    def test_import_modules(self):
        modules_to_test = [
            "models",
            "models.user",
            # Add more modules you want to test here
        ]
        
        for module_name in modules_to_test:
            try:
                __import__(module_name)
                print(f"Module '{module_name}' imported successfully.")
            except ModuleNotFoundError as e:
                print(f"Error importing module '{module_name}': {e}")

if __name__ == "__main__":
    unittest.main()
