/* 
    Acronyms
    Create a function that, given a string, returns the string’s acronym 
    (first letter of each word capitalized). 
    Do it with .split first if you need to, then try to do it without
    SPLIT EXAMPLE:
    var str = "Hello world"
    str.split(" ") => ["Hello", "world"]


    var str1 = " there's no free lunch - gotta pay yer way. ";
    var expected1 = "TNFL-GPYW";
    
    var str2 = "Live from New York, it's Saturday Night Live!";
    var expected2 = "LFNYISNL";

    HINT:
    .toUpperCase()

    * Turns the given str into an acronym.
    * - Time: O(?).
    * - Space: O(?).
    * @param {string} str A string to be turned into an acronym.
    * @returns {string} The given str converted into an acronym.
*/

var str1 = " there's no free lunch - gotta pay yer way. "

function acronym(str){

    var new_arr = [];
    // the split function d
    var new_str = str.split();
    // this going through the new arry and pushing it to the new var
    
    for (var i = 0; i < new_str.length; i++ ){
        if (new_str === new_str[0]){
            new_arr.push(i);
        }
        return(new_arr);
    }
    console.log(new_arr)
}

acronym(str1)


/* 
    String: Reverse
    Given a string,
    return a new string that is the given string reversed

    var str1 = "creature";
    var expected1 = "erutaerc";

    var str2 = "dog";
    var expected2 = "god";


    * Reverses the given str.
    * - Time: O(?).
    * - Space: O(?).
    * @param {string} str String to be reversed.
    * @returns {string} The given str reversed.
*/
function reverseString(str) {

}