class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        min_ind = 1
        max_ind = n
        while (max_ind - min_ind > 1):
            ind = (max_ind - min_ind)/2+min_ind
            ans = isBadVersion(ind)
            if ans:
                max_ind = ind
            else:
                min_ind = ind
        return max_ind
