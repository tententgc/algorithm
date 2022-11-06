class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if nums2 != []:
            nums3 = nums1[:]
            i = 0 
            j = 0
            k = 0 
            while k<= m+n-1: 
                if (j>=n or nums3[i]<nums2[j]) and i<m:
                    nums1[k] = nums3[i]
                    i+=1 
                    k+=1
                else:
                    nums1[k] = nums2[j]
                    j+=1
                    k+=1