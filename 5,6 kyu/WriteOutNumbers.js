// https://www.codewars.com/kata/52724507b149fa120600031d
// Create a function that transforms any positive number to a string representing 
// the number in words. The function should work for all numbers between 0 and 999999.

var ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]; 
var teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
var tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
var n;

function number2words(num){
    // works for numbers between 0 and 999999   
    n = String(num);
    
    if(n.length <= 3){ return getSegment(num).trim(); }

    else if(n.length > 3 && n.length < 7){
      var seg1 = getSegment(Math.floor(num/1000)) + " thousand "; seg1 = seg1.replace(" zero", "");
      var seg2 = getSegment(num%1000);
      console.log(seg1)
      return (seg1 + seg2).trim();
    }
    else {return "";}
  }

function getSegment(seg){ //To convert 3 digit numbers
  var t;
  var to = seg%100;
    if(String(to).length === 2 && String(to).substring(0,1) === "1"){ // Example: if number is 17, then index will be 7 which is "seventeen"
      t = teens[to-10];
    }
    else if(String(to).length === 1){
      t = ones[to];
      if(n.substring(n.length-2) === "00" && t==="zero"){ t = ""; } //For misleading zeros at the end, eg. 1000
    }
    else {
      if( to%10 == 0 ){ t = tens[to/10 - 2]; } //Example: 30/10 = 3; 3-2 = 1. tens[1] is "thirty"
      else {  t = tens[Math.floor(to/10) - 2] + "-" + ones[to%10]; } //Example: 34%10 = 4; 4+1 = 5. ones[5] is "four"
    }

    if(seg >= 100){
      var p = String(seg).substring(0,1); //hundreds
      var f;
      if(p != "0"){ f = ones[Number(p)] + " hundred"; }  
      return f + " " + t;
    }
    else{ return t; }
}
