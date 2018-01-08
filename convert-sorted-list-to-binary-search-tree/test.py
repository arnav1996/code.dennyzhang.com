#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
##
##    ,-----------
##    | Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
##    | 
##    | For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
##    | 
##    | 
##    | Example:
##    | 
##    | Given the sorted linked list: [-10,-3,0,5,9],
##    | 
##    | One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
##    | 
##    |       0
##    |      / \
##    |    -3   9
##    |    /   /
##    |  -10  5
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        ## Basic Idea: Binary Search
        ## Complexity: Time O(log(n)*n), Space O(1)
        ## Assumptions:
        ## Sample Data:

        ## Sample Data:
        node_count = self.getNodeCount(head)

        if node_count == 0:
            return None
        if node_count == 1:
            return TreeNode(head.val)

        # find the middle node
        before_mid_node = self.findNodeBeforeMiddle(head, node_count)
        # print("head.val:%d, before_mid_node: %d" % (head.val, before_mid_node.val))
        mid_node = before_mid_node.next
        before_mid_node.next = None
        head_node = TreeNode(mid_node.val)
        left_node = self.sortedListToBST(head)
        right_node = self.sortedListToBST(mid_node.next)
        head_node.left = left_node
        head_node.right = right_node
        return head_node

    def getNodeCount(self, head):
        res = 0
        p = head
        while p:
            p = p.next
            res = res + 1
        return res

    def findNodeBeforeMiddle(self, head, node_count):
        # print("findNodeBeforeMiddle. head.val: %d, node_count: %d" % (head.val, node_count))
        index_count = node_count/2 - 1
        p = head
        while index_count != 0 and p:
            p = p.next
            index_count = index_count - 1
        return p
