class Solution:

    def counter_freq(self, num: str) -> int:

        if len(num) == 1:
            return ([str(1), (num[0])])
        else:
            streak = 1
            result = []
            for i in range(1, len(num)):
                old = num[i - 1]
                cur = num[i]
                if cur == old:
                    streak += 1
                    if i == len(num) - 1:
                        result.append(str(streak))
                        result.append(old)

                else:
                    result.append(str(streak))
                    result.append(old)
                    if i == len(num) - 1:
                        result.append(str(1))
                        result.append(cur)
                    else:
                        streak = 1
        return result

    def countAndSay(self, n: int) -> str:
        return_number = ['1']
        for i in range(n - 1):
            return_number = instance.counter_freq(''.join(return_number))

        return_number = ''.join(return_number)
        #return_number = int(return_number)
        return return_number

class Solution1:
    iterate_count = 0
    return_val = '1'

    def counter_freq(self, num: int) -> str:
        #print("Received number " + str(num))
        Solution1.iterate_count += 1
        #print("Iterate count is " + str(Solution1.iterate_count))
        temp_results = ''

        inBuffer = False
        if (Solution1.iterate_count == num):
            #print("Match found")
            return Solution1.return_val
        else:
            if len(Solution1.return_val) == 1:
                Solution1.return_val = '11'
                return self.counter_freq(num)

            #print("Return val :" + Solution1.return_val)
            old_val = Solution1.return_val[0]
            #print("old val is :" + old_val)


            streak = 1

            for i in range(1,len(Solution1.return_val)):
                if old_val == Solution1.return_val[i]:
                    streak += 1
                    if i == len(Solution1.return_val)-1:
                        temp_results = temp_results + str(streak) + old_val
                        inBuffer = False

                else:
                    temp_results = temp_results + str(streak) + old_val
                    old_val = Solution1.return_val[i]
                    streak = 1
                    inBuffer = True
            if inBuffer:
                temp_results = temp_results + str(streak) + old_val
            Solution1.return_val = temp_results
            return self.counter_freq(num)

    def countAndSay(self, n: int) -> str:
        return self.counter_freq(n)














if __name__ == '__main__':
    instance = Solution1()
    #iterate_num = 4


    print(instance.countAndSay(3))