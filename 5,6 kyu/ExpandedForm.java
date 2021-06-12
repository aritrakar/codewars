// https://www.codewars.com/kata/5842df8ccbd22792a4000245
// You will be given a number and you will need to return it as a string in Expanded Form.

public class Kata{
    public static String expandedForm(int num){
      String res=""; int c=0;
      int len = Integer.toString(num).length();
      int st[] = new int[len];
      for(int i=len-1; i>0; i--){
          int temp = num/(int)Math.pow(10,i);
          num -= temp*(int)Math.pow(10,i);
          st[c] = temp*(int)Math.pow(10,i);
          c++;
      }
      st[c] = num%10;
      for(int k=0;k<len;k++){
          if((k != len-1) && st[k]!=0){res+= st[k]+" + ";}
          else if(st[k] == 0){;}
          else{res += st[k];}
      }
      if(st[c]==0){System.out.print(res.substring(0,res.length()-3));return res.substring(0,res.length()-3);}
      else{System.out.print(res);return res;}
    }   
}
