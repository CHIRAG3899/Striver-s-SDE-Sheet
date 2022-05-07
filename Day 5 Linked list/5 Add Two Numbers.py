#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# 
#
#Example 1:
#
#
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#Example 2:
#
#Input: l1 = [0], l2 = [0]
#Output: [0]
#Example 3:
#
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        string1 = string2 = ""
       
        while(l1):
            string1+=str(l1.val)
            l1= l1.next
            
        while(l2):
            string2+=str(l2.val)
            l2 = l2.next
        
        string1 = string1[::-1]
        string2 = string2[::-1]
        value = int(string1)+int(string2)
        
        l3 = dummy= ListNode()
       
        for i in range(len(str(value))):
            dummy.next= ListNode(str(value)[-(i+1)])
            dummy = dummy.next
            
        return l3.next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _ = l1.val + l2.val
        digit, tenth = _ % 10, _ // 10
        answer = ListNode(digit)
        if any((l1.next, l2.next, tenth)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += tenth
            answer.next = self.addTwoNumbers(l1, l2)    
        return answer