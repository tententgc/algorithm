var findMedianSortedArrays = function (nums1, nums2) {
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    const m = nums1.length;
    const n = nums2.length;
    let start = 0;
    let stop = m;
    while (start <= stop) {
        let p1 = Math.floor((start + stop) / 2);
        let p2 = Math.floor((m + n + 1) / 2) - p1;
        let maxleft1 = p1 == 0 ? Number.MIN_SAFE_INTEGER : nums1[p1 - 1];
        let minright1 = p1 == m ? Number.MAX_SAFE_INTEGER : nums1[p1];
        let maxleft2 = p2 == 0 ? Number.MIN_SAFE_INTEGER : nums2[p2 - 1];
        let minright2 = p2 == n ? Number.MAX_SAFE_INTEGER : nums2[p2];
        if (maxleft1 <= minright2 && maxleft2 <= minright1) {
            if ((m + n) % 2 == 0) {
                return (Math.max(maxleft1, maxleft2) + Math.min(minright1, minright2)) / 2.0;
            } else {
                return Math.max(maxleft1, maxleft2);
            }
        }
        else if (maxleft1 > minright2) {
            stop = p1 - 1;
        }
        else {
            start = p1 + 1;
        }
    }
};