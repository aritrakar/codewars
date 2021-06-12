// https://www.codewars.com/kata/558ee8415872565824000007
// Create a function isDivisible(n,...) that checks if the first argument n is 
// divisible by all other arguments (return true if no other arguments).

public class Divisible {
    public static boolean isDivisible(int ...args) {
        boolean f = false;
        for(int i=1; i<args.length;i++){
          if(args[i]!=0 && (args[0] % args[i] == 0)){f=true;}
          else{f=false; break;}
        }
        return f;
    }
}
