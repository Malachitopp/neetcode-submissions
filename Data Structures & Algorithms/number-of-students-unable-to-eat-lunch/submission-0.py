class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        counter = 0
        while students and counter < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                counter = 0 
            else:
                students.append(students.popleft())
                counter += 1
            
        return len(students)
            
            


