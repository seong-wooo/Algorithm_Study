class Solution {
    public String simplifyPath(String path) {
        String path2 = path.replaceAll("/+", "/");

        String[] sp = path2.split("/");

        String[] answer = new String[sp.length];
        int index = 0;
        
        for (String d : sp) {
            System.out.println(d);
            if (d.equals(".")) {
                continue;
            }

            if (d.equals("..")) {
                if (index > 0) {
                    answer[--index] = "";
                }
            } else {
                answer[index++] = d;
            }
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < index; i++) {
            if (answer[i] != "") {
                sb.append("/");
                sb.append(answer[i]);
            }
        }

        if (sb.isEmpty()) {
            return "/";
        }

        return sb.toString();
    }
}