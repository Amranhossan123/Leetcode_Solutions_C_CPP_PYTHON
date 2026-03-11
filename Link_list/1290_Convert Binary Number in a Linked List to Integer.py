
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        head_list=[]
        total_result=0
        temp=head
        while(temp!=None):
            head_list.append(temp.val)
            temp=temp.next
        limit=len(head_list)
        j=0
        for i in range(limit-1,-1,-1):
            total_result+=head_list[i]*(2**j)
            j+=1
        return total_result
    
node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)

node1.next = node2
node2.next = node3

head = node1


head = node1

# -------- run solution --------
sol = Solution()
result = sol.getDecimalValue(head)

print("Decimal value:", result)      
        