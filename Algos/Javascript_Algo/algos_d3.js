/* 
    String: Is Palindrome
    Create a function that returns a boolean whether the string is a strict palindrome. 
        - palindrome = string that is same forwards and backwards
    
    Do not ignore spaces, punctuation, or capitalization
*/

// const str1 = "a x a";
// const expected1 = true;

const str2 = "racecar";
// const expected2 = true;

const str3 = "Dud";
// const expected3 = false;

const str4 = "oho!";
// const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
const str1 = "a x a";

function isPalindrome(str) {
    // this is going through the index
    for (var i = 0; i < str.length/2; i++){
        // this is comparing 2 index strting from index 0 and the last index going toward the middle
        if (str[i] == str[str.length - i- 1])
            return true;
        }
        return false;
    }

console.log(isPalindrome(str4))

// Bonus Algo
/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

// const str1 = "what up, daddy-o?";
// const expected1 = "dad";

// const str2 = "uh, not much";
// const expected2 = "u";

// const str3 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";

const str4 = "";
// const expected4 = false;

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
 function longestPalindromicSubstring(str) {
    if str = ""
    return false
    for (var i = 0; i < str.length/2; i++){
        if (str[i] == str[str.length - i- 1])
    }

}
console.log(longestPalindromicSubstring(str4))