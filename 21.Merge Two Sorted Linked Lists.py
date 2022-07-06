#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    #def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        #both lists are empty
        if list1 == None and list2 == None:
            return None

        finalList = ListNode()
        header = finalList

        # if list1 is empty, return the entire list2
        if list1 == None:
            return list2

        # if list2 is empty, return the entire list1
        if list2 == None:
            return list1

        # iterate both lists until you reach the end in one of these
        while list1 != None and list2 != None:

            if list1.val > list2.val:
                finalList.val = list2.val
                list2 = list2.next
            else:
                finalList.val = list1.val
                list1 = list1.next

            newItem = ListNode()
            finalList.next = newItem
            finalList = finalList.next


            # if you reached the empty on list1, then 
            if list1 == None:

                while list2.next != None :

                    finalList.val = list2.val
                    finalList.next = list2.next

            if list2 == None:

                while list1.next != None:

                    finalList.val = list1.val
                    finalList.next = list1.next
               
        return header
            
mySolution = Solution()

l1 = ListNode(1)
#l1.next = ListNode(2)
#l1.next.next = ListNode(4)

l2 = None

l3 = mySolution.mergeTwoLists(l1, l2)

while l3 != None:

    print(l3.val)
    l3 = l3.next
