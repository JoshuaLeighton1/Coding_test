from coding_test import organize_data, get_points, output_sorted_points
import unittest
import mock

class Test(unittest.TestCase):
    """these tests are written so that the
        input given must be what's stated in the return_value"""
    #testing if one line will return the expected dictionary
    def test_dictionary_output_one_line(self):
        
        with mock.patch('builtins.input', return_value =
                        "lions 1, tigers 2"
                        ):
            actual = organize_data()
            expected = {"tigers": ["win"], "lions": ["lose"]}
            self.assertEqual(actual, expected)
    #testing if two lines will return the expected dictionary
    def test_dictionary_output_two_lines(self):
        
        with mock.patch('builtins.input', return_value = [
            "lions 1, tigers 2","cheetahs 1, tigers 1"
            ]):
            actual = organize_data()
            expected = {"tigers":["win", "draw"], "lions": ["lose"], "cheetahs": ["draw"]}
            self.assertEqual(actual, expected)
    #testing if the get_points method returns the expected dictionary with one line
    def test_dictionary_with_points(self):
        with mock.patch('builtins.input', return_value = "lions 1, tigers 2"):
            initial_data = organize_data()
            actual = get_points(initial_data)
            expected = {"tigers": 3 , "lions" : 0}
            self.assertEqual(actual, expected)
    #testing if the get_points method returns the expected dictionary with two lines
    def test_dictionary_with_points_two(self):
        with mock.patch('builtins.input', return_value = [
            "lions 1, tigers 2","cheetahs 1, tigers 1"
            ]):
            
            initial_data = organize_data()
            actual = get_points(initial_data)
            expected = {"tigers": 4, "lions": 0, "cheetahs": 1}
        
            self.assertEqual(actual, expected)
    #testing if the output_sorted_points method returns the right dictionary, hence the right output
    def test_output_sorted_points(self):
        with mock.patch('builtins.input', return_value = [
            "lions 1, tigers 2","lions 1, cubs 1"
            ]):
            initial_data = organize_data()
            points_data = get_points(initial_data)
            #will return this dictionary while output will still be printed
            final_data = output_sorted_points(points_data)
            expected = {"tigers": 3, "cubs": 1, "lions":1}
            self.assertEqual(final_data, expected)
            
        
            



if __name__ == "__main__":
    unittest.main()
    
            
    
  

