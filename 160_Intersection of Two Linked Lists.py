# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Using hashmap
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashTable = {}
        while headA:
            hashTable[headA] = headA.val
            headA = headA.next
        #print(hashTable)
        while headB:
            if headB in hashTable.keys():
                return headB
            headB = headB.next
        return None
'''
using two pointers
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        A_pointer = headA
        B_pointer = headB
        while A_pointer or B_pointer:
            if A_pointer and B_pointer:
                if A_pointer == B_pointer:
                    return A_pointer
                else:
                    A_pointer = A_pointer.next
                    B_pointer = B_pointer.next
            elif not A_pointer and B_pointer:
                A_pointer = headB
            elif not B_pointer and A_pointer:
                B_pointer = headA
        return None