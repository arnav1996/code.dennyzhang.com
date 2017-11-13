#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #brain
## Description:
##     https://leetcode.com/problems/assign-cookies/description/
##    ,-----------
##    | Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
##    | 
##    | Note:
##    | You may assume the greed factor is always positive. 
##    | You cannot assign more than one cookie to one child.
##    | 
##    | Example 1:
##    | Input: [1,2,3], [1,1]
##    | 
##    | Output: 1
##    | 
##    | Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
##    | And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
##    | You need to output 1.
##    | Example 2:
##    | Input: [1,2], [1,2,3]
##    | 
##    | Output: 2
##    | 
##    | Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
##    | You have 3 cookies and their sizes are big enough to gratify all of the children, 
##    | You need to output 2.
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: sqrt(num)
        ## Complexity:
        ## Sample Data:
        ##    1 2 7
        if num <= 1:
            return False
        import math
        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i != num/i:
                    sum += num/i
        return sum == num
