/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  let start = 0,
    end = nums.length - 1;
  let mid = 0;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    const val = nums[mid];
    const left = nums[mid - 1] || -Infinity;
    const right = nums[mid + 1] || -Infinity;

    if (val > left && val > right) return mid;
    if (left > val) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return 0;
};
