class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        output = 0
        arr_size = len(arr)
        for i in range(arr_size):
            for j in range(i + 1, arr_size):
                for k in range(j + 1, arr_size):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        output += 1
        return output