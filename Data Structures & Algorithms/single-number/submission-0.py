class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Xor -> 1 ^ 1= 0 , 1^0=1
        result=0
        for num in nums:
            result^=num
        return result