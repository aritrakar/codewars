// https://www.codewars.com/kata/5848565e273af816fb000449
// You want to create secret messages which can be deciphered by the Decipher this! kata. 
// Here are the conditions:
// Your message is a string containing space separated words.
// You need to encrypt each word in the message using the following rules:
// The first letter needs to be converted to its ASCII code.
// The second letter needs to be switched with the last letter
// Keepin' it simple: There are no special characters in input.

public class Kata {
    public static String encryptThis(String text) {
        // Implement me! :)
      if(text != ""){
        String f="";
        String st[] = text.split(" ");
        for(int j=0;j<st.length;j++){
            f+= transform(st[j])+" ";
        }
        return f.trim();
      } else{return "";}
    }
    static String transform(String s){
        if(s.length() > 2){
            return Integer.toString((int)s.charAt(0)) + Character.toString(s.charAt(s.length()-1)) 
            + s.substring(2,s.length()-1) + Character.toString(s.charAt(1));//s.substring(1);
        }
        else if(s.length() == 2){return Integer.toString((int)s.charAt(0)) + s.substring(1);}
        else{return Integer.toString((int)s.charAt(0));}
    }
}
