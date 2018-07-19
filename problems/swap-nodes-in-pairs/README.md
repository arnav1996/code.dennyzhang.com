
# Leetcode: Swap Nodes in Pairs     :BLOG:Basic:

---

Swap Nodes in Pairs  

---

Given a linked list, swap every two adjacent nodes and return its head.  

For example,  
Given 1->2->3->4, you should return the list as 2->1->4->3.  

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/swap-nodes-in-pairs)  

Credits To: [leetcode.com](https://leetcode.com/problems/swap-nodes-in-pairs/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/swap-nodes-in-pairs
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def swapPairs(self, head):
    	"""
    	:type head: ListNode
    	:rtype: ListNode
    	"""
    	## Idea: pointer Each time move 2 steps
    	## Complexity: Time O(n), Space O(1)
    	## Assumptions:
    	##     One element, returns itself
    	##     If odd number of elements, don't change for the last element
    	## Data Sample:
    	##      1 -> 2 -> 3 -> 4 -> 5 -> 6
    	##                .    .
    	##           p    q    r
    	if (head is None) or (head.next is None):
    	    return head
    
    	# swap the first 2 nodes
    	p = head
    	q = head.next
    	r = q.next
    
    	# change head
    	head = q
    	q.next = p
    	p.next = r
    
    	q = p.next
    	while(q and (q.next is not None)):
    	    r = q.next
    	    # swap q and r
    	    tmp = r.next
    	    p.next = r
    	    r.next = q
    	    q.next = tmp
    	    # move for 2 steps
    	    p = p.next.next
    	    q = p.next
    	return head
