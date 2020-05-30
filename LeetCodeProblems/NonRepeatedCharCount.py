from math import sqrt
from copy import deepcopy

class Solution2:

    def __init__(self):
        self.list_all_tokens = [chr(x) for x in range(32,128) ]

    def is_token_present_in_list(self,token) -> list:
       return token in self.list_all_tokens

    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest_length = 0
        for start in range(len (s)):
            count_length = 0
            copy_token = deepcopy(self.list_all_tokens)
            possible_length = len(s) - start
            if possible_length <= biggest_length:
                return biggest_length
            for char in s[start:len(s)]:
                #print("Found char " + char)

                #print("Index val is " + str(index))
                #print("Factor val is " + str(factor_val))
                if char not in copy_token:
                    #print("Found a repeat")
                    if count_length > biggest_length:
                        biggest_length = count_length
                    break
                else:
                    #print("Not a repeat")
                    copy_token.remove(char)
                    count_length += 1
                if count_length > biggest_length:
                    biggest_length = count_length
        return biggest_length




class Solution:
    def getPrimesUpto(num: int) -> list:
        counter = 0
        return_list = []
        num_test = 2
        while True:
            if Solution.isPrime(num_test):
                return_list.append(num_test)
                counter += 1
            if counter == num:
                return return_list
            num_test += 1

    def isPrime(num: int) -> bool:
        # print("Sqrt for " , str(num) , " is " + str(int(sqrt(num))))
        for factor in range(2, int(sqrt(num)) + 1):
            if num % factor == 0:
                return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        all_list = Solution.getPrimesUpto(96)


        biggest_length = 0
        for start in range(len (s)):
            count_length = 0
            multiplication_val = 1
            possible_length = len(s) - start
            if possible_length <= biggest_length:
                return biggest_length
            for char in s[start:len(s)]:
                #print("Found char " + char)
                index = ord(char) - 32
                factor_val = all_list[index]
                #print("Index val is " + str(index))
                #print("Factor val is " + str(factor_val))
                if multiplication_val % factor_val == 0:
                    #print("Found a repeat")
                    if count_length > biggest_length:
                        biggest_length = count_length
                    break
                else:
                    #print("Not a repeat")
                    multiplication_val = multiplication_val * factor_val
                    count_length += 1
                if count_length > biggest_length:
                    biggest_length = count_length
        return biggest_length

if __name__ == '__main__':
    s = "abcabcdss"
    print(Solution2().lengthOfLongestSubstring(s))