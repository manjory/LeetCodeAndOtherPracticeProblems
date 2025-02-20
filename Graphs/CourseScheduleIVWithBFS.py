"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

here is a BFS approach with time complexity O(N+E)

"""
from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build the graph (Adjacency List)
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        prereq_sets = [set() for _ in range(numCourses)]  # Stores all prerequisites for each course

        for prereq, course in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1

        # Step 2: Process Topological Order Using BFS
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:  # Add independent courses
                queue.append(course)

        while queue:
            prereq = queue.popleft()
            for course in graph[prereq]:
                prereq_sets[course] |= prereq_sets[prereq]  # Inherit prereqs
                prereq_sets[course].add(prereq)  # Add direct prereq

                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)

        # Step 3: Answer Queries in O(1)
        return [q[0] in prereq_sets[q[1]] for q in queries]

