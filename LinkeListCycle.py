# Definition for singly-linked list.
import json
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head, pos):
        """
        :type head: ListNode
        :type pos: int
        :rtype: bool
        """
        if not head or pos == -1:
            return False
        if not head.next and pos == 0:
            return True
        tmp = head
        index = 0
        while tmp.next:
            tmp = tmp.next
            index = index + 1
            if index == pos:
                break
        fast = head
        slow = head
        while fast:
            slow = slow.next
            if not fast.next:
                fast = tmp
            else:
                fast = fast.next.next
                if not fast:
                    fast = tmp
            if slow is fast:
                return True
        return False


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)
    # numbers = [3,0,2,4]
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToInt(input):
    return int(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    # input = [3,0,2,4]
    # p = 1
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line)
            line = next(lines)
            pos = stringToInt(line)

            ret = Solution().hasCycle(head, pos)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()