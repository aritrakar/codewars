// https://www.codewars.com/kata/5390bac347d09b7da40006f6
// Jaden is known for almost always capitalizing every word. For simplicity, you'll have to 
// capitalize each word, check out how contractions are expected to be in the example below.
// Your task is to convert strings to how they would be written by Jaden Smith. The strings 
// are actual quotes from Jaden Smith, but they are not capitalized in the same way he
// originally typed them.

public class JadenCase {
    public static String toJadenCase(String phrase) {
        // TODO put your code below this comment
        if(phrase != null && phrase != ""){
            String st[] = phrase.split(" ");
            String n="";
            for(int i=0;i<st.length;i++){
            st[i] = st[i].substring(0,1).toUpperCase() + st[i].substring(1);  
            n+= st[i] + " ";
            }
            return n.trim();
        }
        else {return null;}
    }
}
