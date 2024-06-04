class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        result = []
        # populate prefix array
        pref_def = 1
        post_def = 1
#         step 1 calculate prefix
        for i in range(1, len(nums)):
            if i-2 >= 0:
                prefix[i-1] = prefix[i-2]*nums[i-1]
            else:
                prefix[i-1] = nums[i-1]
        print(prefix)
#         step 2 calculate postfix
        for i in range(len(nums)-1, -1, -1):
            if i+1 == len(nums):
                continue

            if i+2 == len(nums):
                postfix[i+1] = nums[i+1]
            else:
                postfix[i+1] = nums[i+1]*postfix[i+2]
        print(postfix)
#         step 3 calculate multiplication

        for i in range(len(nums)):
            pref = 1
            if i != 0:
                pref = prefix[i-1]
            post = 1
            if i+1 != len(nums):
                post = postfix[i+1]
            result.append(pref*post)

        return result
# v2 with constant memory


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
#         step 1 calculate prefix
        for i in range(1, len(nums)):
            if i-2 >= 0:
                prefix[i-1] = prefix[i-2]*nums[i-1]
            else:
                prefix[i-1] = nums[i-1]

#         step 2 calculate postfix
        post = 1
        for i in range(len(nums)-1, -2, -1):

            if i+1 == len(nums):
                continue
            if i+2 == len(nums):
                prefix[i+1] = prefix[i]*post

                post = nums[i+1]*post
            elif i+2 < len(nums):
                if i < 0:
                    prefix[i+1] = post*1
                    post *= nums[i+1]
                else:
                    prefix[i+1] = post*prefix[i]
                    post *= nums[i+1]
        return prefix
