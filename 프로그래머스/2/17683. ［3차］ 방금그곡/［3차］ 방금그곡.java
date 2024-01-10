import java.util.regex.*;

class Solution {
    public String solution(String m, String[] musicinfos) {
        m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a");
        Pattern pattern = Pattern.compile(m);

        
        int playTime = 0;
        String answer = "(None)";
        
        for (String music : musicinfos) {
            String[] s = music.split(",");
            int minute = changeMinutes(s[0], s[1]);
            String name = s[2];
            String sound = s[3].replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a");
            
            Matcher matcher = pattern.matcher(sound.repeat(minute/sound.length()) + sound.substring(0,minute % sound.length()));
            if (matcher.find() && minute > playTime) {
                playTime = minute;
                answer = name;
            }
        }
        return answer;
    }
    
    public int changeMinutes(String start, String end) {
        String[] s = start.split(":");
        String[] e = end.split(":");
        
        return (Integer.parseInt(e[0]) - Integer.parseInt(s[0])) * 60 + Integer.parseInt(e[1]) - Integer.parseInt(s[1]);
    }
}