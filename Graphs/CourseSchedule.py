"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.



"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        print(graph)

        inDegrees=[0]*numCourses
        for prereq, c in prerequisites:
            inDegrees[prereq]+=1

        print(inDegrees)

        queue=deque()

        for course in range(numCourses):
            if inDegrees[course] ==0:
                queue.append(course)
        print(queue)
        count=0
        while queue:
            noreqCourse=queue.popleft() #0
            count+=1
            for prereq in graph[noreqCourse]:
                inDegrees[prereq]-=1
                if inDegrees[prereq]==0:
                    queue.append(prereq)
        return count==numCourses
