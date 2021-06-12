// https://www.codewars.com/kata/5635e7cb49adc7b54500001c
// There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
// You are given money in nominal value of n with 1<=n<=1500.
// Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

public class ATM {
  public int solve(int n) {
      // Your code here
        int coin[] = {500,200,50,20,10};
        int num=0, tot=0, c=0;
        while(tot != n && c<coin.length){
            if(tot + coin[c] <= n){
                num++; tot += coin[c]; 
            }
            else{c++;}
        }
        if(tot==n){return num;}
        else {return -1;}
      
  }
}
