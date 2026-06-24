class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        frequency = defaultdict(int)

        for element in nums:
            frequency[element]  += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in frequency.items():
            buckets[value].append(key)

        output = []

        for i in reversed(buckets): 
                for number in i:
                    output.append(number)
                    if len(output) == k:
                         return output


        
