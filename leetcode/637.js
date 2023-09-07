/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var averageOfLevels = function (root) {
  const cnt = [];
  const sums = [];
  const aver = [];
  const calc = (data, level) => {
    if (!data) {
      return null;
    }
    if (sums[level] == undefined) {
      sums[level] = 0;
      cnt[level] = 0;
    }
    sums[level] += data.val ?? 0;
    cnt[level] += 1;

    calc(data.left, level + 1);
    calc(data.right, level + 1);
  };

  calc(root, 0);

  for (let i = 0; i < cnt.length; i++) {
    aver.push(sums[i] / cnt[i]);
  }

  return aver;
};
