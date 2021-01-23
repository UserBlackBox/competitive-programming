# https://binarysearch.com/problems/Friend-Groups

class Solution:
    def solve(self, friends):
        groups = 0
        visited = [False]*len(friends)
        while not all(visited):
            try:
                visit = [visited.index(False)]
                groups += 1
            except ValueError:
                break
            while True:
                temp = []
                for i in visit:
                    visited[i] = True
                    for j in friends[i]:
                        if not visited[j]:
                            temp.append(j)
                if len(temp) == 0:
                    break
                visit = temp
        return groups

