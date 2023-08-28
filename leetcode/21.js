/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  let node = new ListNode();
  let answer = node;

  while (list1 || list2) {
    if (!list2 || list1?.val < list2.val) {
      // list2 가 없거나 list1.val 값이 더 작을 때
      node.next = new ListNode(list1.val);
      node = node.next;
      list1 = list1.next;
    } else {
      node.next = new ListNode(list2.val);
      node = node.next;
      list2 = list2.next;
    }
  }

  return answer.next;
};
