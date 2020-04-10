class Solution:
    def myAtoi(self, str1: str) -> int:
        temp = str1
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signs = ['+', '-']
        valid_char = nums + signs
        
        is_valid = False
        for i in str1:
            if i in nums:
                is_valid = True
        if(not is_valid):
            return 0
        
        for index, c in enumerate(str1):
            if(c == ' '):
                temp = str1[index+1:]
            else:
                break
           
        if(temp[0] in signs):
            for index, c in enumerate(temp[1:len(temp)], start=1):
                if(c not in nums):
                    temp = temp[:index]
                    break
            if(len(temp) == 1):
                return 0
        elif(temp[0] in nums):
            for index, c in enumerate(temp[1:len(temp)], start=1):
                if(c not in nums):
                    temp = temp[:index]
                    break
        else:
            return 0
        
        return max(min(int(temp), 2147483647), -2147483648)
