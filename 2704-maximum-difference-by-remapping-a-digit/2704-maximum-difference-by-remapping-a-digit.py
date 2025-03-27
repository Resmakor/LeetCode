class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        maxim, minim, maxim_remap, minim_remap = "", "", '', num[0]
        for i in range(len(str(num))):
            if str(num)[i] == '9':
                continue
            else:
                maxim_remap = str(num)[i]
                break
        for i in range(len(str(num))):
            if num[i] == maxim_remap:
                maxim += '9'
            else:
                maxim += str(num)[i]
            if num[i] == minim_remap:
                minim += '0'
            else:
                minim += num[i]
        maxim.lstrip('0')
        minim.lstrip('0')
        return int(maxim) - int(minim)
            
            