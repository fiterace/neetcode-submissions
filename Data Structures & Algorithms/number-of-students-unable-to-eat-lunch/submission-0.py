from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches.reverse()
        stud = deque(students)
        next_stud = []
        while True:
            next_stud = []
            start = len(stud)
            while len(stud):
                top = stud.popleft()
                if (sandwiches[-1] != top):
                    next_stud.append(top)
                else:
                    sandwiches.pop()
            stud = deque(next_stud)
            if(len(next_stud) == start):
                break
        return len(next_stud)

            