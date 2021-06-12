// https://www.codewars.com/kata/54da5a58ea159efa38000836
// Given an array of integers, find the one that appears an odd number of times.
// There will always be only one integer that appears an odd number of times.

import java.util.Arrays;
public class FindOdd {
    public static int findIt(int[] a) {
      if(a.length > 1){
        Arrays.sort(a);
        int odd=0, j, i=0;
        while(i<a.length-1){
            int c=0;
            for(j=i;j<a.length;j++){
                if(a[i]==a[j]){c++;}
                else{break;}
            }
            if(c%2!=0){odd = a[i];break;}
            else{i = j; odd = a[j];}
        }
        return odd;
      }
      else{return a[0];}
  }
}
