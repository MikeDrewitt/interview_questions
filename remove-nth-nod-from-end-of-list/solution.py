#!/usr/bin/python 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        my_array = []

        while head.next != None:
            my_array.append(head.val)
            head = head.next
        else:
            my_array.append(head.val)

        print(my_array)
        n = -1 * n

        my_array.pop(n)
        return my_array

        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
