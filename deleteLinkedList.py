#defination for singly linked list
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self,node):
        """
        :type node : ListNode
        :rtype : void do not return anything , modify node in-place instead

        """

        if node == None:
            pass
        else:
            next_node = node.next
            #Savs refrence to the next node
            #nedded to copy data and update links

            node.val = next_node.val
            #overrit current node's value 
            #make current node look like the next node

            
            node.next = next_node.next
            #remove the next node from the  chain
            #meomory will be grabaged colleted
    

def print_list(head):
    while head:
        print(head.val , end=" ->")
        head = head.next
    print("None")

#test cases
#__test_case_1
# head = ListNode(1)

# head.next = ListNode(2)

# node_to_delete = ListNode(3)
# head.next.next = node_to_delete
# node_to_delete.next = ListNode(4)
#_text_Case_2
# head = ListNode(10)
# node_to_delete = ListNode(20)
# head.next = node_to_delete
# node_to_delete.next = ListNode(30)
#_test_cases_3 
# head = ListNode(5)

# head.next = ListNode(6)
# node_to_delete = ListNode(7)
# head.next.next = node_to_delete
# node_to_delete.next = ListNode(8)
#_test_Cases 4
# head = ListNode(3)
# node_to_delete = head



print("Before deletion:")

print_list(head)

Solution().deleteNode(node_to_delete)

print("After deletion")

print_list(head)

