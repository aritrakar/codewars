// https://www.codewars.com/kata/554b4ac871d6813a03000035
// You are given a string of space separated numbers, and have to return the highest and lowest number.

public class Kata {
  public static String highAndLow(String numbers) {
    String st[] = numbers.split(" ");
    int nums[] = new int[st.length];
    for(int j=0;j<st.length;j++){nums[j] = Integer.parseInt(st[j]);}
    int max=nums[0], min=nums[0];
    for(int j=0;j<nums.length;j++){
        if(nums[j] > max){max = nums[j];}
        if(nums[j] < min){min = nums[j];}
    }
    return Integer.toString(max)+" "+Integer.toString(min);
  }
}
