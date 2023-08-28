/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let digit = 0;
  let sum = 0;
  let obj = new ListNode();
  let answer = obj;
  while (l1 || l2 || digit) {
    sum = digit + (l1?.val ?? 0) + (l2?.val ?? 0);
    obj.next = new ListNode(sum % 10);
    digit = Math.floor(sum / 10);
    l1 = l1?.next;
    l2 = l2?.next;
    obj = obj.next;
  }

  return answer.next;
};
