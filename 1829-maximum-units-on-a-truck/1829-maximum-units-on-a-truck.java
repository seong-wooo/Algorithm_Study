class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int result = 0;
        for(int[] box : Arrays.stream(boxTypes).sorted(Comparator.comparingInt(a -> -a[1])).toList()) {
            if (truckSize >= box[0]) {
                truckSize -= box[0];
                result += box[0] * box[1];
            } else {
                result += truckSize * box[1];
                truckSize = 0;
            }

            if (truckSize == 0) {
                break;
            }
        }


        return result;
    }
}