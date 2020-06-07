class Solution:
    def reconstructQueue(self, people):
        people.sort(key= lambda x:x[1])
        print(people)


if __name__ == '__main__':
    obj = Solution()
    ip = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    obj.reconstructQueue(ip)
