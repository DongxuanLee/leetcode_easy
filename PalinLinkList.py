# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre_node = None
        fast = head
        slow = head
        while fast and fast.next:
            next_node = slow.next
            slow.next = pre_node
            pre_node = slow
            slow = next_node
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != pre_node.val:
                return False
            slow = slow.next
            pre_node = pre_node.next
        return True