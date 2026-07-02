class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums: # 13, 25, 83, 77
            temp = []
            while num > 0: # 13 -> temp = [3, 1]
                temp.append(num % 10)
                num //= 10
            # Ikkada reverse logic start
            while temp: # temp empty ayye varaku
                ans.append(temp.pop()) # Last nunchi okati okati teesi ans lo veyadam
                                       # [3,1].pop() -> 1, tarvata 3 -> ans = [1,3]
            
        return ans