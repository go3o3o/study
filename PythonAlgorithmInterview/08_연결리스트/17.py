# https://leetcode.com/problems/swap-nodes-in-pairs/
import ListNode


def swapPairsUsingSwitch(self, head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


def swapPairsUsingLoop(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next


def swapPairsUsingRecursive(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairsUsingRecursive(p.next)

        p.next = head
        return p
    return head
