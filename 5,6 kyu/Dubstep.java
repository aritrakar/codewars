// https://www.codewars.com/kata/551dc350bf4e526099000ae5

public class Dubstep {
  public static String SongDecoder (String song){
     String st[] = song.split("WUB");
     String s="";
     for(int i=0; i<st.length;i++){
       if(!st[i].equals("")){s+= st[i]+" ";}
     }
     return s.trim();
   }
}
