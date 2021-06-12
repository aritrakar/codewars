// https://www.codewars.com/kata/545cedaa9943f7fe7b000048
// A pangram is a sentence that contains every single letter of the alphabet at least once. 
// For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
// because it uses the letters A-Z at least once (case is irrelevant).
// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
// Ignore numbers and punctuation.

import java.util.*;
public class PangramChecker {
  public static boolean check(String sentence){
    //code
    sentence = sentence.replaceAll("[.,!\\s0-9]","").toLowerCase();
    String st[] = sentence.split(""); 
    Arrays.sort(st);
    List<String> s = new ArrayList<String>(st.length);
    for(int i=0;i<st.length;i++){s.add(st[i]);}
    long l = s.stream().distinct().count();
    if(l==26){return true;}
    else{return false;}
  }
}
