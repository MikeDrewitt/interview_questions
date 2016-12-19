#!/usr/bin/python

def simpleRomanToInt(char):
    if char == 'I':
        return 1
    elif char == 'V':
        return 5
    elif char == 'X':
        return 10
    elif char == 'L':
        return 50
    elif char == 'C':
        return 100
    elif char == 'D':
        return 500
    elif char == 'M':
        return 1000

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #numbers we need I1 V5 X10 L50 C100 D500 M1000
        # if one to the right is larger subtract that number

        string_list = list(s)
        count = 0

        for index in range(0, len(string_list)):
            char = string_list[index]
            num = simpleRomanToInt(char)

            try: 
                char_adj = string_list[index+1]
                num_adj = simpleRomanToInt(char_adj)

                if num_adj > num:
                    num = -1 * num
            except IndexError:
                pass

            count += num
        return count
        
