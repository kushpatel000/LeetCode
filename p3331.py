# 3331. Find Subtree Sizes After Changes [Medium]
# https://leetcode.com/problems/find-subtree-sizes-after-changes 

#  You are given a tree rooted at node 0 that consists of n nodes numbered from 0
#  to n - 1. The tree is represented by an array parent of size n, where parent[i]
#  is the parent of node i. Since node 0 is the root, parent[0] == -1.
#  You are also given a string s of length n, where s[i] is the character assigned
#  to node i.
#  We make the following changes on the tree one time simultaneously for all nodes
#  x from 1 to n - 1:
#  Find the closest node y to node x such that y is an ancestor of x, and s[x] ==
#  s[y].
#  If node y does not exist, do nothing.
#  Otherwise, remove the edge between x and its current parent and make node y the
#  new parent of x by adding an edge between them.
#  Return an array answer of size n where answer[i] is the size of the subtree
#  rooted at node i in the final tree.
#  Example 1:
#  Input: parent = [-1,0,0,1,1,1], s = "abaabc"
#  Output: [6,3,1,1,1,1]
#  Explanation:
#  The parent of node 3 will change from node 1 to node 0.
#  Example 2:
#  Input: parent = [-1,0,4,0,1], s = "abbba"
#  Output: [5,2,1,1,1]
#  Explanation:
#  The following changes will happen at the same time:
#  The parent of node 4 will change from node 1 to node 0.
#  The parent of node 2 will change from node 4 to node 1.
#  Constraints:
#  n == parent.length == s.length
#  1 <= n <= 10^5
#  0 <= parent[i] <= n - 1 for all i >= 1.
#  parent[0] == -1
#  parent represents a valid tree.
#  s consists only of lowercase English letters.

###############################################################################
###############################################################################

from typing import List
import test_suite as ts
import tqdm

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        N = len(parent)
        new_parents = parent[:]
        # print(f'{parent=}')
        # print(f'{s=}')

        for x in range(N):
            y = parent[x]
            while y >= 0 and s[y] != s[x]:
                y = parent[y]
            if y>=0:
                new_parents[x] = y
                # print(f'{x=}, {s[x]=}, {y=}, {s[y]=}')
            # else:
            #     print(f'{x=}, no ancestor')

        counts = [0] * N
        for i in range(N):
            p = i
            while p >= 0:
                counts[p] += 1
                p = new_parents[p]

        # print(f'{new_parents=}')
        # print(f'{counts=}')
        return counts

    def findSubtreeSizes_v2(self, parent: List[int], s: str) -> List[int]:
        N = len(parent)

        children = [list() for _ in s]
        for x in range(1,N):
            children[parent[x]].append(x)
        size, last = [1]*N, dict()

        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1)
            last[c] = x
            for child in children[x]:
                dfs(child)
            last[c] = above
            if x:
                size[above if  above>=0 else parent[x]] += size[x]

        dfs(0)
        return size


        


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.findSubtreeSizes,
        sol.findSubtreeSizes_v2,
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[:-1],
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )