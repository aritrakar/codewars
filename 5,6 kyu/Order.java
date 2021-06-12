// https://www.codewars.com/kata/55c45be3b2079eccff00010f
// Your task is to sort a given string. Each word in the string will contain a single number. 
// This number is the position the word should have in the result.
// Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
// If the input string is empty, return an empty string. The words in the input String will 
// only contain valid consecutive numbers.

public class Order {
  public static String order(String words) {
    // ...
   if(words != ""){
    String someString="";
    String st[] = words.split(" ");
    String f[] = new String[st.length];
    for(int j=0; j<st.length;j++){
        int index = num(st[j]) - 1;
        f[index] = st[j];
    }   
    for(int j=0;j<f.length;j++){someString+= f[j]+" ";}
    return someString.trim();   
   }
   else{return "";}
  }
  static int num(String n){
      String temp = "";
      for(int k=0;k<n.length();k++){
          switch(n.charAt(k)){
              case '1': temp="1"; break;
              case '2': temp="2"; break;
              case '3': temp="3"; break;
              case '4': temp="4"; break;
              case '5': temp="5"; break;
              case '6': temp="6"; break;
              case '7': temp="7"; break;
              case '8': temp="8"; break;
              case '9': temp="9"; break;
          }
      }
      return Integer.parseInt(temp);
  }
}
