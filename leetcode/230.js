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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  let index = 0;
  let smallest;
  const recursive = (data) => {
    if (!data) {
      return;
    }
    recursive(data.left);
    index++;
    if (index == k) {
      smallest = data.val;
      return;
    }
    recursive(data.right);
  };

  recursive(root);
  return smallest;
};
