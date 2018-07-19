
# Leetcode: Find Bottom Left Tree Value     :BLOG:Basic:

---

Find Bottom Left Tree Value  

---

Similar Problems:  

-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Given a binary tree, find the leftmost value in the last row of the tree.  

    Example 1:
    Input:
    
        2
       / \
      1   3
    
    Output:
    1

    Example 2:
    Input:
    
            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7
    
    Output:
    7
    Note: You may assume the tree (i.e., the given root node) is not NULL.

Note:  
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/find-bottom-left-tree-value)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-bottom-left-tree-value/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/find-bottom-left-tree-value
    ## Basic Ideas: level-order traversal
    ##              Check the first element of every layer
    ##              Return the item of deepest level
    ##
    ## Complexity: Time O(n), Space O(n)
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findBottomLeftValue(self, root):
    	"""
    	:type root: TreeNode
    	:rtype: int
    	"""
    	queue = []
    	queue.append(root)
    	res = None
    	while len(queue) != 0:
    	    length = len(queue)
    	    first_element = queue[0]
    	    res = first_element
    	    for i in xrange(length):
    		node = queue[0]
    		del queue[0]
    		if node.left:
    		    queue.append(node.left)
    		if node.right:
    		    queue.append(node.right)
    	return res.val
