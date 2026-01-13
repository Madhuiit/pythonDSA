#defination for singly linked list
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self,head):
        """
        :type head : ListNode
        :rtype : bool
       
        """

        if head == None:
            return False
        else:
            fast = head
            slow = head

            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    break
            if fast == None or fast.next == None:
                return False
            elif fast == slow:
                return True
            



def create_linked_list(values,pos):
    """

    values : list of node values
    pos : index where tail   connects (-1 means no cycle)

    """

    if not values:
        return None
    nodes = [ListNode(v) for v in values]


    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]




#test cases
# head = None
# print(Solution().hasCycle(head))

# head = ListNode(1)
# print(Solution().hasCycle(head))

# head = ListNode(1)
# head.next = head
# print(Solution().hasCycle(head))

# head = create_linked_list([1,2,3,4],-1)

# print(Solution().hasCycle(head))
# head = create_linked_list([1,2,3,4],0)

# print(Solution().hasCycle(head))



