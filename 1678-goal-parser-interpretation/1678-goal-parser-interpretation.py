class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command_size = len(command)
        output = ""
        i = 0
        while i != command_size:
            if command[i] == 'G':
                output += 'G'
                i += 1
            elif command[i] == "(":
                i += 1
                if command[i] == ")":
                    output += 'o'
                    i += 1
                elif command[i] == "a":
                    output += "al"
                    i += 3
        return output