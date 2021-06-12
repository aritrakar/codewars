// https://www.codewars.com/kata/52c31f8e6605bcc646000082
// Write a function that takes an array of numbers (integers for the tests) and a target number. 
// It should find two different items in the array that, when added together, give the target value. 
// The indices of these items should then be returned in a tuple like so: (index1, index2).

public class Solution{   
    public static int[] twoSum(int[] numbers, int target){
        if(numbers != null){
        int st[] = new int[2];
        for(int i=0;i<numbers.length-1;i++){
            for(int j=i+1;j<numbers.length;j++){
                if(numbers[i] + numbers[j] == target){st[0]=i; st[1]=j; break;}
            }
        }
        return st; // Do your magic!
    }
    else{return null;}
    }
}
