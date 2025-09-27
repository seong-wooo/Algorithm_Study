class Solution {
    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int[] answer = new int[queries.length];

        for (int i = 0 ; i <queries.length; i++) {
            int[] query = queries[i];
            int k = query[0];
            int trim = query[1];
            Queue<Element> pq = new PriorityQueue<>();

            for(int j = 0;  j < nums.length; j++) {
                String num = nums[j];
                String trimNum = num.substring(num.length() - trim);
                Element e = new Element(j, trimZero(trimNum));
                pq.add(e);
            }

            while (k > 1) {
                k--;      
                pq.poll();
            }
           
            answer[i] = pq.poll().index;
        }
        return answer;
    }

    public String trimZero(String num) {
        for (int i = 0; i < num.length(); i++) {
            if (num.charAt(i) != '0') {
                return num.substring(i);
            }
        }

        return "0";
    }
    
    static class Element implements Comparable<Element>{
        int index;
        String value;

        public Element(int index, String value) {
            this.index = index;
            this.value = value;
        }

        @Override
        public int compareTo(Element e) {
            int lengthCompare = this.value.length() - e.value.length();
            if (lengthCompare == 0) {
                int compare = this.value.compareTo(e.value);
                if (compare == 0) {
                    return this.index - e.index;
                }
                return compare;
            }
            return lengthCompare;
        }
    }
}