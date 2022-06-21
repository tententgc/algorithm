/* Given a string of digits, return all possible letter combinations that the number could represent.

The mapping of digits to letters is:

2 -> a, b, c
3 -> d, e, f
4 -> g, h, i
5 -> j, k, l
6 -> m, n, o
7 -> p, q, r, s
8 -> t, u, v
9 -> w, x, y, z

The mapping is provided in the form of a hash table.

The function takes two parameters */
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
    const mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    digits = digits.split("")
    let result = []
    for (const digit of digits) {
        result = charStringMutiply(mapping[digit], result)
    }
    return result
};

var charStringMutiply = function (chars, strings) {
    const result = []
    if (strings.length == 0) {
        return chars
    }
    for (const character of chars) {
        for (const st of strings) {
            result.push(st + character)
        }
    }
    return result
}