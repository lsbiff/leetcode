#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    #def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        if list1 == None and list2 == None:
            return None

        finalList = ListNode()
        header = finalList

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

            if list1 == None:

                while list2.next != None :

                    finalList.val = list2.val
                    finalList.next = ListNode()
                    finalList = finalList.next
                    list2 = list2.next

                finalList.val = list2.val

            if list2 == None:

                while list1.next != None:

                    finalList.val = list1.val
                    finalList.next = ListNode()
                    finalList = finalList.next
                    list1 = list1.next

                finalList.val = list1.val
               
        return header
            
mySolution = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
#l1.next.next = ListNode(4)

l2 = None

l3 = mySolution.mergeTwoLists(l1, l2)

while l3 != None:

    print(l3.val)
    l3 = l3.next
