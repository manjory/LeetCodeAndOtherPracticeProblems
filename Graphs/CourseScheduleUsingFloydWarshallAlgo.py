"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.


"""

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # this problem should use Floyd Warshall algorithm to ensure transitive closure

        #there is a need to calculate reachability which is done as follows:
        reachability=[[False] * numCourses for _ in range(numCourses)]

        for prereq,course in prerequisites:
            reachability[prereq][course]=True

        #Floyd-Warshall to compute transitive closure:
        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    if reachability[i][k] and reachability[k][j]:
                        reachability[i][j]=True

        return [reachability[u][v] for u,v in queries]

