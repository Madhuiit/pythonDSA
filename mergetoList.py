#defination for singly linked list
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeTwoList(self,l1,l2):
        """
        :type l1 : ListNode
        :type  l2 : LisNode
        :rtype : ListNode
        
        """
        if l1 == None and l2 == None:
            return None
        elif l1 != None and l2 == None:
            return l1
        elif l2 != None and l1 == None:
            return l2
        else:
            dummy = ListNode(0)

            p = dummy

            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1 != None:
                p.next = l1
            if l2 != None:
                p.next = l2
            return dummy.next
        
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)

        curr = curr.next
    return head


def print_list(head):
    while head:
        print(head.val, end = "->")

        head = head.next
    print("None")

#test cases
#_test_cases_1
# l1 = None
# l2 =None
#Test_cases_2
# l1 = None
# l2 = build_list([1,2,3])
#test_cases_3
# l1 = build_list([2,4,6])
# l2 = None
#test_Case_4
# l1 = build_list([1,3,5])
# l2 = build_list([2,4,6])
#test_cases_5
# l1 = build_list([1,2,4])
# l2 = build_list([1,3,4])

#test_Cases_6
# l1 = build_list([-5,-3,0])
# l2 = build_list([-4,-2,1])
#test_cases_7
# l1 = build_list([1,2])
# l2 = build_list([3,4,5,6])

#test_Cases_8





result = Solution().mergeTwoList(l1,l2)
print_list(result)