// https://www.codewars.com/kata/53697be005f803751e0015aa
// Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
// For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
// Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
// For example, decode("h3 th2r2") would return "hi there".
// For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

function encode(string) {
  string = replaceAll(string, "a", "1");
  string = replaceAll(string,"e","2");
  string = replaceAll(string,"i","3");
  string = replaceAll(string,"o","4");
  string = replaceAll(string,"u","5");
  return string;
}

function decode(string) {
  string = replaceAll(string,"1","a");
  string = replaceAll(string,"2","e");
  string = replaceAll(string,"3","i");
  string = replaceAll(string,"4","o");
  string = replaceAll(string,"5","u");
  return string;
}
function replaceAll(string, search, replace) {
  return string.split(search).join(replace);
}
