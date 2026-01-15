class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self,head):

        if head == None:
            return None
        elif head != None and head.next == None:

            return None
        else:
            next_node = None
            temp = None
            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node
            return temp
def build_list(values):
    if not  values :
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def print_list(head):
    while head:
        print(head.val , end = "->")
        head = head.next
    print("None")


head = build_list([-1,-2,-3])
result = Solution().reverseList(head)
print_list(result)
