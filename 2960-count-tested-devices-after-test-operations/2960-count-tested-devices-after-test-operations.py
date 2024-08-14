class Solution(object):
    def lower_battery(self, remaining):
        output = []
        for element in remaining:
            if element >= 1:
                output.append(element - 1)
            else:
                output.append(element)
        return output          
                
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        output = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                output += 1
                batteryPercentages = batteryPercentages[:i] + self.lower_battery(batteryPercentages[i:])
        return output