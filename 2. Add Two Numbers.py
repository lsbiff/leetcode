#2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:

        result = ListNode()
        header = result

        carryOver = 0
        # iterating on both lists
        while l1 and l2:
            
            sum = l1.val + l2.val + carryOver

            if sum < 10:
                result.val = sum
                carryOver = 0
            else:
                result.val = sum % 10
                carryOver = 1

            l1, l2 = l1.next, l2.next

            if l1 and l2:

                newItem = ListNode()
                result.next = newItem
                result = result.next
        # if both are done
        if l1 == None and l2 == None:
            # add the carryOver if last values were like 9 + 9
            if carryOver == 1:
                newItem = ListNode(carryOver)
                result.next = newItem
            return header
            
        # if l1 has more elements than l2, add the remaining nodes to the new list considering the carryOver from the last operation
        while l1:

            newItem = ListNode()
            result.next = newItem
            result = result.next
            
            sum = l1.val + carryOver

            if sum < 10:
                result.val = sum
                carryOver = 0
            else:
                result.val = sum % 10
                carryOver = 1

            l1 = l1.next

            
        # same as above but if l2 has more elements than l1
        while l2:

            newItem = ListNode()
            result.next = newItem
            result = result.next
            
            sum = l2.val + carryOver

            if sum < 10:
                result.val = sum
                carryOver = 0
            else:
                result.val = sum % 10
                carryOver = 1

            l2 = l2.next


        # if the last operation create a one last carry over, create a node for him
        if carryOver == 1:
            newItem = ListNode(carryOver)
            result.next = newItem

        return header


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

"""

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(3)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l1 = ListNode(0)
l2 = ListNode(0)


l1 = ListNode(9)
l1.next = ListNode(9)

l2 = ListNode(9)

l1 = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)


l1 = ListNode(5)
l2 = ListNode(5)

"""

mySolution = Solution()
x = mySolution.addTwoNumbers(l1, l2)

while x:
    print(f' {x.val} ')
    x = x.next