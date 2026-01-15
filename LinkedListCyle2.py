class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def detectCyle(self,head):
        """
        :type head : ListNode
        :rtype : ListNode
        """

        if head == None:
            return head
        else:
            fast =  head
            slow =  head

            has_cycle = False
            while fast != None and fast.next != None:
                slow =  slow.next
                fast = fast.next.next

                if fast == slow:
                    has_cycle = True
                    break
            if has_cycle == False:
                return None
            slow = head
            while fast != slow:
                fast = fast.next
                slow =  slow.next
            return slow
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def build_cycle_list(values,pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]
def run_tests():
    tests = [
        ("Empty list", None, None),

        ("Single node, no cycle",
         build_list([1]), None),

        ("Single node, self-cycle",
         (lambda: (lambda n: (setattr(n, "next", n), n)[1])(ListNode(1)))(), 1),

        ("No cycle",
         build_list([1, 2, 3, 4]), None),

        ("Cycle at head",
         build_cycle_list([1, 2, 3, 4], 0), 1),

        ("Cycle in middle",
         build_cycle_list([1, 2, 3, 4, 5], 2), 3),

        ("Two nodes cycle",
         build_cycle_list([1, 2], 0), 1),

        ("Cycle at tail",
         build_cycle_list([10, 20, 30, 40], 3), 40),
    ]

    sol = Solution()

    for name, head, expected in tests:
        result = sol.detectCyle(head)
        result_val = result.val if result else None
        print(f"{name:25} | Expected: {expected} | Got: {result_val}")


# ---------- Run All Tests ----------
run_tests()



