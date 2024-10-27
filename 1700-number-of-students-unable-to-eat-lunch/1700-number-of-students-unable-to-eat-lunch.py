class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counter = 0
        while True:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                counter = 0
            else:
                students.append(students[0])
                students = students[1:]
                counter += 1
            if counter == len(students):
                return len(students)