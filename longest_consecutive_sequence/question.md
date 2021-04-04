Coding Challenge: (pls use Python) - Difficulty level: HARD (according to the source)
Write a function that takes in an array of integers and returns an array of length 2, representing the largest range of numbers contained in that array. The first number in the output array should be the first number in the range. 

A range of numbers is defined as a set of number that come right after each other in the set of real integers. Example: output array [2,6] represents the range [2,3,4,5,6] which is of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.

Sample input:  [1,11,3,0,15,5,2,4,10,7,12,6]
Sample output: [0, 7]

def get_largest_range(input_: list) -> list:
    ... # Your code here

# Test code
import unittest
import get_largest_range


class TestCodeChallenge(unittest.TestCase):

    def test_largest_range(self):
        self.assertEqual(
            get_largest_range([1,11,3,0,15,5,2,4,10,7,12,6]), 
            [0,7]
        )
Please reply in thread, feel free to discuss ... and try not to Google or it will be less fun. Happy coding ￼
