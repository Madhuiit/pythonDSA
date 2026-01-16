#defination for singly linked list


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self,head):
        if head == None:
            return True
        elif head != None and head.next == None:
            return True
        
        else:
            fast = head
            slow = head
            stack = []
            while fast != None and fast.next != None:
                stack.append(slow.val)
                slow = slow.next
                
                fast = fast.next.next

            if fast!= None:
                slow = slow.next
            while slow != None:
                if slow.val  != stack.pop():
                    return False
                else:
                    slow = slow.next
            return True
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

print(Solution().isPalindrome(head))


        
         


    