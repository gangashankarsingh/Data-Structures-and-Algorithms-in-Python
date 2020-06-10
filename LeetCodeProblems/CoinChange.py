
import time
class Solution:

    def __init__(self):
        self.solution_count = 0

    def binary_search(self,list_vals: [int], search_val: int, low_index: int,high_index: int) -> int:

        if low_index == high_index:
            return low_index
        else:
            mid_index = (low_index + high_index)//2


        if list_vals[mid_index] == search_val:
            return mid_index
        elif list_vals[mid_index] < search_val:
            temp_val = list_vals[mid_index + 1]
            if temp_val == search_val:
                return  mid_index+1
            elif temp_val > search_val:
                return  mid_index
            else:
                low_index = mid_index + 1
                return self.binary_search(list_vals,search_val,low_index,high_index)
        else:
            temp_val = list_vals[mid_index-1]
            if temp_val <= search_val:
                return  mid_index-1
            else:
                high_index = mid_index-1
                return self.binary_search(list_vals, search_val, low_index, high_index)

    def get_coefficients(self, max_denominations: [int] , required_coins: [int] , amount: int) -> [int] :



        total_possible_combinations = 1
        for val in max_denominations:
            total_possible_combinations = total_possible_combinations * (val + 1)
        #print("Total possible combinations are : " + str(total_possible_combinations))

        result_coefficients = [0] * len(max_denominations)
        length_all_currencies = len(max_denominations)
        #last_bit = result_coefficients[length_all_currencies-1]


        while total_possible_combinations >0 :
            move_next_bit = True
            temp_sum = 0
            for index in range(len(max_denominations)-1,-1,-1):

                if move_next_bit:
                    if result_coefficients[index] == max_denominations[index]:
                        result_coefficients[index] = 0
                        move_next_bit = True
                    else:
                        result_coefficients[index] += 1
                        move_next_bit = False


                temp_sum += result_coefficients[index]*required_coins[index]
                if temp_sum > amount:
                    break
            if temp_sum == amount:
                self.solution_count += 1
                print("Found a solution")
            #print(result_coefficients)
            total_possible_combinations -= 1



    def change(self, amount: int, coins: [int]) -> int:

        if amount == 0:
            return 1

        if len(coins) == 0:
                return 0

        coins = list(set(coins))
        coins.sort(reverse=True)

        if coins[0] > amount:
            return 0
            #print("No currency can be used")
        else:
            last_index = (self.binary_search(coins,amount,0,len(coins)-1))
            #return self.iterate_find_change(amount,coins[0:last_index+1])
            max_denominations = []
            req_coins =  coins[0:last_index+1]
            for i in req_coins:
                max_denominations.append(amount//i)
            #print(req_coins)
            #print(max_denominations)
            all_coefficients = [0] * len(req_coins)
            #print(all_coefficients)


            self.get_coefficients(max_denominations,req_coins,amount)
            return self.solution_count




if __name__ == '__main__':
    start_time = time.time()

    obj = Solution()

    print(obj.change(100,[3,5,7,8,9,10,11]))

    elapsed_time = time.time() - start_time
    print("Time taken is " + str(elapsed_time))


