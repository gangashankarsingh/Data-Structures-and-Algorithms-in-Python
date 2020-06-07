import random
import copy


class Solution:




    def get_index(self,num: int):

        if num <= self.w[0]:
            return 0

        low = 0
        high = len(self.w)

        while low != high:
            mid = ( low + high )//2
            if self.w[mid] == num:
                return mid
            elif self.w[mid] < num:
                if self.w[mid+1] >= num:
                    return mid+1
                else:
                    low = mid+1
            else:
                if self.w[mid-1] == num:
                    return mid-1
                elif self.w[mid-1] < num:
                    return mid
                else:
                    high = mid-1

        return low



    def __init__(self, w):
        self.w = w
        for i in range(1,len(self.w)):
            self.w[i] = self.w[i-1] + self.w[i]
        self.last_val = self.w[len(self.w)-1]






    def pickIndex(self) -> int:
        num = random.randint(1, self.last_val)


        print("Number is num " + str(num))
        #print("Now the list is " + str(self.index_copy))
        return self.get_index(num)





# Your Solution object will be instantiated and called as such:
if __name__ == '__main__':
    w = [3, 14, 1, 7]
    obj = Solution(w)
    print(obj.w)
    for i in range(10000):
        print(obj.pickIndex())