# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getLPSArrary(p):
            arr = [0] * len(p)
            j = -1
            for i in range(1, len(p)):
                print("i:", i, "j:", j)
                while j != -1 and p[j + 1] != p[i]:
                    j = arr[j]
                if p[j+1] == p[i]:
                    j += 1
                arr[i] = j
            return arr
        def findStr(s, p):
            arr = getLPSArrary(p)
            j = -1
            print("2 i:", i, "j:", j)
            for i in range(len(s)):
                print("2 i:", i, "j:", j)
                while j != -1 and p[j + 1] != p[i]:
                    j = arr[j]
                if p[j+1] == s[i]:
                    j += 1
                if j == len(p):
                    return True
            return False
        def serializeTree(cur) -> str:
            if cur == None:
                return "Null"
            return "," + str(cur.val) + "," + serializeTree(cur.left) + "," + serializeTree(cur.right)
        print("start")
        rootStr = serializeTree(root)
        subRootStr = serializeTree(subRoot)
        res = findStr(rootStr, subRootStr)

        return res
