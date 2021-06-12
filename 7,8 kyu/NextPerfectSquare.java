// https://www.codewars.com/kata/56269eb78ad2e4ced1000013
// You might know some pretty large perfect squares. But what about the NEXT one?
// Complete the findNextSquare method that finds the next integral perfect square after 
// the one passed as a parameter. Recall that an integral perfect square is an integer n 
// such that sqrt(n) is also an integer. If the parameter is itself not a perfect square 
// then -1 should be returned. You may assume the parameter is non-negative.

public class NumberFun {
  public static long findNextSquare(long sq) {
    if(Math.sqrt(sq)==(int)Math.sqrt(sq)){
      long res = sq+1;
      boolean found = false;
      while(!found){
        if(Math.sqrt(res)==(int)Math.sqrt(res)){found=true; break;}
        res++;
      }
      return res;
    }
    else{return -1;} 
  }
}
