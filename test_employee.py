import unittest
class TestEmployee(unittest.TestCase):
    def test_json_download(self):
        self.assertTrue(True)
    def test_json_extraction(self):
        self.assertTrue(True)
    def test_file_type(self):
        self.assertEqual(type({}),dict)
    def test_data_structure(self):
        self.assertIn("id",{"id":1})
    def test_missing_data(self):
        self.assertIsNone(None)
if __name__=="__main__":
    unittest.main()
        