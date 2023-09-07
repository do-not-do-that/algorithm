function rightSideView(root) {
  const res = [];

  function traverse(node, level) {
    if (node?.val === undefined) return null;

    res[level] = node.val;

    traverse(node.left, level + 1);
    traverse(node.right, level + 1);
  }

  traverse(root, 0);

  return res;
}
