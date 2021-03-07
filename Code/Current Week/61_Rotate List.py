'''
Approach
- We need at least 2 elements for this algo to work,
so we add edge case for that
- create a circle of LL where tail points 
back to head to make it easy to traverse
- to ensure the k does not exceed n we wrap it up and 
subtract 1 as index starts from 0
tail_idx = n -(k%n) - 1
- new head = tail_idx + 1
- break the cycle
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        #initilaize and traverse to set the tail
        curr_tail = head
        len_list = 1
        while curr_tail.next:
            curr_tail = curr_tail.next
            len_list += 1
        #loop tail back to head
        curr_tail.next = head
        tail_idx = len_list-(k%len_list)-1
        new_tail = head
        for _ in range(tail_idx):
            new_tail = new_tail.next
        new_head = new_tail.next
        #break loop and point tail back to None
        new_tail.next = None
        return new_head