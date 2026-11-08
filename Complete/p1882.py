# 1882. Process Tasks Using Servers [Medium]
# https://leetcode.com/problems/process-tasks-using-servers 

#  You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​
#  and m​​​​​​ respectively. servers[i] is the weight of the i^​​​​​​th​​​​ server,
#  and tasks[j] is the time needed to process the j^​​​​​​th​​​​ task in seconds.
#  Tasks are assigned to the servers using a task queue. Initially, all servers are
#  free, and the queue is empty.
#  At second j, the j^th task is inserted into the queue (starting with the 0^th
#  task being inserted at second 0). As long as there are free servers and the
#  queue is not empty, the task in the front of the queue will be assigned to a
#  free server with the smallest weight, and in case of a tie, it is assigned to a
#  free server with the smallest index.
#  If there are no free servers and the queue is not empty, we wait until a server
#  becomes free and immediately assign the next task. If multiple servers become
#  free at the same time, then multiple tasks from the queue will be assigned in
#  order of insertion following the weight and index priorities above.
#  A server that is assigned task j at second t will be free again at second t +
#  tasks[j].
#  Build an array ans​​​​ of length m, where ans[j] is the index of the server the
#  j^​​​​​​th task will be assigned to.
#  Return the array ans​​​​.
#  Example 1:
#  Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
#  Output: [2,2,0,2,1,2]
#  Explanation: Events in chronological order go as follows:
#  - At second 0, task 0 is added and processed using server 2 until second 1.
#  - At second 1, server 2 becomes fre1e. Task 1 is added and processed using server
#  2 until second 3.
#  - At second 2, task 2 is added and processed using server 0 until second 5.
#  - At second 3, server 2 becomes free. Task 3 is added and processed using server
#  2 until second 5.
#  - At second 4, task 4 is added and processed using server 1 until second 5.
#  - At second 5, all servers become free. Task 5 is added and processed using
#  server 2 until second 7.
#  Example 2:
#  Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
#  Output: [1,4,1,4,1,3,2]
#  Explanation: Events in chronological order go as follows:
#  - At second 0, task 0 is added and processed using server 1 until second 2.
#  - At second 1, task 1 is added and processed using server 4 until second 2.
#  - At second 2, servers 1 and 4 become free. Task 2 is added and processed using
#  server 1 until second 4.
#  - At second 3, task 3 is added and processed using server 4 until second 7.
#  - At second 4, server 1 becomes free. Task 4 is added and processed using server
#  1 until second 9.
#  - At second 5, task 5 is added and processed using server 3 until second 7.
#  - At second 6, task 6 is added and processed using server 2 until second 7.
#  Constraints:
#  servers.length == n
#  tasks.length == m
#  1 <= n, m <= 2 * 10^5
#  1 <= servers[i], tasks[j] <= 2 * 10^5

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        print(f'{servers=}')
        print(f'{tasks=}')

        import heapq

        # initialize the server heap
        operating_servers = list() # key: (task_complete_time, server weight, server id)
        free_servers = list() # key: (server weight, server id)
        for i, w in enumerate(servers):
            heapq.heappush(free_servers, (w, i))
        

        current_time = 0
        ids = list()
        for j, q in enumerate(tasks):
            current_time = max(j, current_time)
            while operating_servers and operating_servers[0][0] <= current_time:
                t, w, i = heapq.heappop(operating_servers)
                heapq.heappush(free_servers, (w,i))

            if not free_servers:
                current_time = operating_servers[0][0]
                t, w, i = heapq.heappop(operating_servers)
                heapq.heappush(free_servers, (w,i))
        

            w, i = heapq.heappop(free_servers)
            ids.append(i)
            heapq.heappush(operating_servers, (current_time+q, w, i))

        return ids


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.assignTasks
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )