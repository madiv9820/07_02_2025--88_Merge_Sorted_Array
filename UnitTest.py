from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__solution = Solution()
        self.__testcases = {1: ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
                            2: ([1], 1, [], 0, [1]),
                            3: ([0], 0, [1], 1, [1]),
                            4: ([1,3,5,0,0,0], 3, [2,4,6], 3, [1,2,3,4,5,6]),
                            5: ([1, 2, 3, 0, 0, 0], 3, [5,6,7], 3, [1,2,3,5,6,7]),
                            6: ([1,0], 1, [2], 1, [1,2]),
                            7: ([-10, 0, 5, 0, 0, 0], 3, [-5,0,10], 3, [-10,-5,0,0,5,10]),
                            8: ([1,1,1,0,0,0], 3, [1,1,1], 3, [1,1,1,1,1,1]),
                            9: ([0,0,0,0], 0, [], 0, [0,0,0,0]),
                            10: ([1000000000, 2000000000, 3000000000, 0, 0, 0], 3, 
                                 [1500000000, 2500000000, 3500000000], 3, 
                                 [1000000000, 1500000000, 2000000000, 2500000000, 3000000000, 3500000000]),
                            11: ([7,0,0,0], 1, [1,2,3], 3, [1,2,3,7])}
        return super().setUp()
    
    @timeout(0.5)
    def test_standard_case_with_overlapping_elements(self):
        nums1, m, nums2, n, expected = self.__testcases[1]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_nums2_is_empty(self):
        nums1, m, nums2, n, expected = self.__testcases[2]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_nums1_is_empty(self):
        nums1, m, nums2, n, expected = self.__testcases[3]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_both_arrays_are_already_merged_and_sorted(self):
        nums1, m, nums2, n, expected = self.__testcases[4]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_all_elements_in_nums2_are_larger_than_elements_in_nums1(self):
        nums1, m, nums2, n, expected = self.__testcases[5]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_nums1_and_nums2_contain_only_one_element_each(self):
        nums1, m, nums2, n, expected = self.__testcases[6]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_arrays_contain_negative_numbers(self):
        nums1, m, nums2, n, expected = self.__testcases[7]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_arrays_contain_identical_elements(self):
        nums1, m, nums2, n, expected = self.__testcases[8]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_both_arrays_are_empty(self):
        nums1, m, nums2, n, expected = self.__testcases[9]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_large_numbers(self):
        nums1, m, nums2, n, expected = self.__testcases[10]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
    @timeout(0.5)
    def test_nums1_has_a_larger_first_element_than_nums2(self):
        nums1, m, nums2, n, expected = self.__testcases[11]
        self.__solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

if __name__ == '__main__': unittest.main()