from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Initialize a temporary cache array to store the merged result
        # The cache size is m + n to fit all elements from both nums1 and nums2
        cache = [-1] * (m + n)
        
        # Initialize pointers for the two input arrays and the cache
        i = j = k = 0

        # Merge the elements from both nums1 and nums2 while both arrays still have elements
        while i < m and j < n:
            # If the element from nums1 is smaller, add it to the cache
            if nums1[i] < nums2[j]:
                cache[k] = nums1[i]
                i += 1  # Move pointer in nums1
            else:
                # If the element from nums2 is smaller or equal, add it to the cache
                cache[k] = nums2[j]
                j += 1  # Move pointer in nums2
            k += 1  # Move pointer in cache to the next position

        # If there are any remaining elements in nums1, add them to the cache
        while i < m:
            cache[k] = nums1[i]
            i += 1
            k += 1
        
        # If there are any remaining elements in nums2, add them to the cache
        while j < n:
            cache[k] = nums2[j]
            j += 1
            k += 1
        
        # Copy the merged elements from the cache back to nums1
        for i in range(m + n):
            nums1[i] = cache[i]