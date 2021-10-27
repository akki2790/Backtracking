# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(s,openc,closec):
            if len(s) == 2*n:
                res.append(s)
            if openc < n:
                helper(s+"(",openc+1,closec)
            if closec < openc:
                helper(s+")",openc,closec+1)
        helper("",0,0)
        return res
