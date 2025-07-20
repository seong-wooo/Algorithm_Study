class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int left = 0;
        int right = 0;

        while (left < nums1.length && right < nums2.length && nums1[left] != nums2[right]) { 
            if (nums1[left] < nums2[right]) {
                left++;
            } else if(nums1[left] > nums2[right]) {
                right++;
            }

            if (left < nums1.length && right < nums2.length && nums1[left] == nums2[right]) {
                break;
            }
        }
        return left < nums1.length && right < nums2.length && nums1[left] == nums2[right] ? nums1[left] : -1;
    }
}