// https://www.codewars.com/kata/5656b6906de340bd1b0000ac
// Take 2 strings s1 and s2 including only letters from ato z. 
// Return a new sorted string, the longest possible, containing 
// distinct letters - each taken only once - coming from s1 or s2.

import java.util.Arrays;
public class TwoToOne {    
    public static String longest (String s1, String s2) {
        // your code
        String some="";
        for(int k=0;k<s1.length();k++){
            if(!some.contains(Character.toString(s1.charAt(k)))){some+=Character.toString(s1.charAt(k));}
        }
        for(int k=0;k<s2.length();k++){
            if(!some.contains(Character.toString(s2.charAt(k)))){some+=Character.toString(s2.charAt(k));}
        }
        char[] chars = some.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        return sorted;
    }
}
