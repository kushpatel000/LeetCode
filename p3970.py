# 3970. Shortest Path With At Most K Consecutive Identical Characters [Medium]
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/ 

from typing import List
import test_suite as ts

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # print(f'{n=}')
        # print(f'{edges=}')
        # print(f'{labels=}')
        # print(f'{k=}')
        inf = float('inf')

        edge = dict()
        edge_weights = dict()
        for a, b, w in edges:
            if a not in edge: edge[a] = set()
            edge[a].add(b)
            edge_weights[(a,b)] = min( edge_weights.get((a,b), inf), w )
        # print(f'{edge=}')
        # print(f'{edge_weights=}')
        
        def dfs(path:list, consec:str, weight:int) -> int:
            l = path[-1]
            # print(path)
            if l == n-1: 
                # print(f'{path=}, {weight=}')
                return weight

            sub_res = inf
            for e in edge.get(l, set()):
                # no loops
                # print(f'Checking {l}->{e}')
                if e in path: continue
                # consecutive characters
                if labels[e] != consec[-1:]:
                    path.append(e)
                    new_weight = weight + edge_weights[(l,e)]
                    res = dfs(path, labels[e], new_weight)
                    sub_res = min(res, sub_res)
                    path.pop()

                
                elif len(consec) < k:
                    path.append(e)
                    new_weight = weight + edge_weights[(l,e)]
                    res = dfs(path, consec+labels[e], new_weight)
                    sub_res = min(res, sub_res)
                    path.pop()

            return sub_res

        res = dfs([0], labels[0], 0)
        if res == inf: return -1
        return res

    def shortestPath_dp(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        inf = float('inf')
        edge = dict()
        edge_weights = dict()
        for a, b, w in edges:
            if a not in edge: edge[a] = set()
            edge[a].add(b)
            edge_weights[(a,b)] = min( edge_weights.get((a,b), inf), w )

        best_paths = [dict() for _ in range(n)]
        best_paths[0][ labels[0] ] = 0

        # see the bfw
        todo = [0]
        while todo:
            new_todo = set()
            for src in todo:
                for dst in edge.get(src, []):
                    for prev_suffix, prev_weight in best_paths[src].items():
                        if prev_suffix[-1] == labels[dst] and len(prev_suffix) == k:
                            continue

                        new_suff = (prev_suffix if prev_suffix[-1] == labels[dst] else '') + labels[dst]
                        prev_sol = best_paths[dst].get(new_suff, inf)
                        new_sol  = prev_weight+edge_weights[(src,dst)]
                        if new_sol < prev_sol:
                            new_todo.add(dst)
                            best_paths[dst][new_suff] = new_sol

            todo = list(new_todo)

        if best_paths[n-1]:
            return min( best_paths[n-1].values() )
        return -1



    def shortestPath_dijkstra(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq

        inf = float('inf')
        edge = dict()
        edge_weights = dict()
        for a, b, w in edges:
            if a not in edge: edge[a] = set()
            edge[a].add(b)
            edge_weights[(a,b)] = min( edge_weights.get((a,b), inf), w )
        # print(f'{n=}')
        # print(f'{edges=}')
        # print(f'{labels=}')
        # print(f'{k=}')
        # print(edge_weights)

        best_paths = [[inf]*(k+1) for _ in range(n)]
        
        # print(best_paths)
        best_paths[0][1] = 0

        todo = list()
        heapq.heapify(todo)
        # tuple key: (weight, node, prefix)
        heapq.heappush(todo, (0,0,1))

        while todo:
            prev_weight, src, prev_suffix = heapq.heappop(todo)
            if src == n-1: continue

            for dst in edge.get(src,[]):
                if labels[src] == labels[dst] and prev_suffix == k:
                    continue

                new_suff = prev_suffix * (labels[src] == labels[dst]) + 1
                # print(f'{src=}, {dst=}, {labels[src]=}, {labels[dst]=}, {prev_suffix=}, {new_suff=}')
                prev_sol = best_paths[dst][new_suff]
                new_sol  = prev_weight+edge_weights[(src,dst)]
                if new_sol < prev_sol:
                    heapq.heappush(todo, (new_sol, dst, new_suff))
                    best_paths[dst][new_suff] = new_sol

            # print(f'{todo=}')

        v = min( best_paths[n-1] )
        if v == inf:
            return -1
        return v
    


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.shortestPath,
        # sol.shortestPath_dp,
        sol.shortestPath_dijkstra 
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True,
        # repeat = 2,
        # number = 1000
    )