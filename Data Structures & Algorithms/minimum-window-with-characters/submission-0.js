class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {  let left = 0
    let windowSize = Infinity
    let tMap = {}
    for (let ch of t){
        tMap[ch] = (tMap[ch] | 0) + 1
    }
    let required = Object.keys(tMap).length
    let ans = ""

    let window = {}
    let found = 0
    let startIndex = 0
    for (let right = 0; right < s.length; right++){
       window[s[right]] = (window[s[right]] | 0) + 1
        if (window[s[right]] === tMap[s[right]]){
            found++
        }

        //now we reducce the window to see how much we can reduce 
         while (found === required) {
            let currentWindowSize = right - left + 1;

            if (currentWindowSize < windowSize) {
                windowSize = currentWindowSize;
                startIndex = left;
            }

            let leftChar = s[left];
            window[leftChar]--;

            if (
                tMap[leftChar] &&
                window[leftChar] < tMap[leftChar]
            ) {
                found--;
            }

            left++;
        }
    }

    return windowSize === Infinity
        ? ""
        : s.slice(startIndex, startIndex + windowSize);}
}
