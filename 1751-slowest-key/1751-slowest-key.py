class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        output = {keysPressed[0]}
        curr_time, max_time = releaseTimes[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            curr_time = releaseTimes[i] - releaseTimes[i - 1]
            print(curr_time, releaseTimes[i], releaseTimes[i - 1])
            if curr_time > max_time:
                output.clear()
                output.add(keysPressed[i])
                max_time = curr_time
            elif curr_time == max_time:
                output.add(keysPressed[i])
        return max(output)


