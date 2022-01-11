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