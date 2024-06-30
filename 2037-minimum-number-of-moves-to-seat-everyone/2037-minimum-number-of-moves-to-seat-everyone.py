class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        arr_size = len(seats)
        output = 0
        for i in range(arr_size):
            output += abs(students[i] - seats[i])
        return output