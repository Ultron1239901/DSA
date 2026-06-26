def twosum(self, nums,target):
        n = len(nums)
        result= {}
        for i,num in enumerate(nums):
            need = target - num
            if need in result:
                  return [result[need],i]
            result[need] = i 

