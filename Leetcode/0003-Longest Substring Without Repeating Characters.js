/* 1. Initialize the longest substring to the first character of the string. 
2. Iterate through the string, checking if the current character is in the substring. 
3. If it is, then we need to find the index of the character in the substring. 
4. We then need to extract the substring from the index to the end of the substring. 
5. We then need to add the current character to the substring. 
6. If it's not in the substring, then we just add */
var lengthOfLongestSubstring = function (s) {
    if (!s) return 0;
    if (s.length < 2) return s.length;
    let longest = s[0];  
    let current = s[0];
    
    for (let i = 1; i < s.length; i++) {
        let index = current.indexOf(s[i]);
        if (index > -1) {
            if (current.length > longest.length) {
                longest = current;
            }
            current = current.substring(index + 1,current.length) + s[i];
        }
        else{
            current = current + s[i]; 
        }
    }
    if (current.length > longest.length) {
        longest = current;
    } 
    return longest.length; 
};