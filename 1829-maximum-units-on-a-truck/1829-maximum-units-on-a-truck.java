class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int[] boxes = new int[1001];
        int result = 0;

        for (int[] type : boxTypes) {
            boxes[type[1]] += type[0];
        }

        for (int i = 1000; i > 0; i--) {
            if (boxes[i] == 0) {
                continue;
            }
            
            if (truckSize >= boxes[i]) {
                truckSize -= boxes[i];
                result += i * boxes[i];
            } else {
                result += i * truckSize;
                truckSize = 0;
            }

            if (truckSize == 0) {
                break;
            }
        }

        return result;
    }
}