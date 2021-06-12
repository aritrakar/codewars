// https://www.codewars.com/kata/5266876b8f4bf2da9b000362
// You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
// pictures or other items. We want to create the text that should be displayed next to such an item.
// Implement a function likes :: [String] -> String, which must take in input array, containing the 
// names of people who like an item. It must return the display text as shown in the examples:

import java.util.Arrays;
class Solution {
    public static String whoLikesIt(String... names) {
        //Do your magic here
        String f="";
        if(names.length > 3){f = names[0]+", "+names[1]+" and "+(names.length - 2)+" others like this";}
        else if(names.length == 3){f = names[0]+", "+names[1]+" and "+names[2]+" like this";}
        else if(names.length == 2){ f = names[0]+" and "+names[1]+" like this"; }
        else if(names.length == 1){f = names[0]+" likes this";}
        else {f = "no one likes this";}
        return f;
    }
}
