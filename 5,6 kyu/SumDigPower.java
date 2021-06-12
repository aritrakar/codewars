// https://www.codewars.com/kata/5626b561280a42ecc50000d1
// The number 89 is the first integer with more than one digit that fulfills the property partially introduced 
// in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.
// In effect: 89 = 8^1 + 9^2
// The next number in having this property is 135.
// See this property again: 135 = 1^1 + 3^2 + 5^3
// We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] 
// (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

import java.util.*;
class SumDigPower {
    public static List<Long> sumDigPow(long a, long b) {
        // your code
        List<Long> l = new ArrayList<Long>();
        for(long i=a; i<b;i++){
            if(check(i)){l.add(i);}
        }
        return l;
    }
    public static boolean check(long m){
        long temp=0, ori=m;
        int len = Long.toString(m).length();
        for(int j=len;j>0; j--){
            temp += Math.pow(m%10,j);
            m = m/10;
        }
        if(ori == temp){return true;}
        else{return false;}
    }
}
