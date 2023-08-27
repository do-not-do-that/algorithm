/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let obj = {};
  let start = 0;
  let end = 0;
  let max = 0;

  while (end < s.length) {
    if (!obj.hasOwnProperty(s[end])) {
      obj[s[end]] = 1;
      end++;
    } else {
      max = Math.max(max, Object.keys(obj).length);
      delete obj[s[start]];
      start++;
    }
  }

  return max;
};
