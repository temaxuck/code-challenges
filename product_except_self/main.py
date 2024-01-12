from typing import List


class Solution:

    """
    # A better solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1]
        back = [1]
        i = 0
        N = len(nums)-1
        j = N

        while i<N and j>0:
            front.append(front[i]*nums[i])
            back.append(back[i]*nums[j])
            i+=1
            j-=1
        n = len(front)
        return [front[i]*back[n-i-1] for i in range(n)]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        zero_count = 0

        answer = [1 / num if num != 0 else 0 for num in nums]

        # product for list with zero and for list without zero
        product = [1, 1]

        for i in range(nums_len):
            if nums[i] == 0:
                zero_count += 1
                product[0] = 0
                if zero_count > 1:
                    return [0] * nums_len

                continue
            else:
                product[0], product[1] = product[0] * nums[i], product[1] * nums[i]

        for i in range(nums_len):
            if answer[i] == 0:
                answer[i] = product[1]
            else:
                answer[i] = int(product[0] * answer[i])

        return answer


print(Solution().productExceptSelf([1, 2, 0, 3]))
# print(hash(tuple([1, 2, 0, 3])))
