class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Count frequency of each number
        freq = [0] * (len(nums) + 1)
        for num in nums:
            freq[num] += 1
        
        # Create 2D array
        result = []
        # Continue until all numbers are used
        while max(freq) > 0:
            current_row = []
            # Check each possible number
            for i in range(1, len(freq)):
                # If number still has frequency > 0, add to current row
                if freq[i] > 0:
                    current_row.append(i)
                    freq[i] -= 1
            # Add the row to result if it's not empty
            if current_row:
                result.append(current_row)
        
        return result

# The lesson here is that we're splitting our array into unique entities -- if we have three ones and none of them can touch each other, we have to move each of them into separate "containment buckets". 
# The practical example here would be something like load-balancing or schedule optimization, where we only have a certain amount of CPU % or amount of time for each task. This is just a much more simplified 
# form of the problem where all we care about is uniqueness. 