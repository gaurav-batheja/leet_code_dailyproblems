# You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the time taken to paint n different walls respectively. There are two painters available:

# A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.
# A free painter that paints any wall in 1 unit of time at a cost of 0. But the free painter can only be used if the paid painter is already occupied.
# Return the minimum amount of money required to paint the n walls.
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        postfix_times = time.copy()

        for i in range(len(postfix_times) - 2, -1, -1):
            postfix_times[i] += postfix_times[i +1]

        visited = {}

        def dp(index, time_painted):
            if index == len(cost):
                return 0 if time_painted >= 0 else float("inf")

            if time_painted >= len(cost) - index:
                return 0

            if time_painted + postfix_times[index] < 0:
                return float("inf")

            if (index, time_painted) in visited:
                return visited[(index, time_painted)]
            
            visited[(index, time_painted)] = min(
                dp(index + 1, time_painted - 1),
                cost[index] + dp(index + 1,
                time_painted + time[index]))
            return visited[(index, time_painted)]
        
        return dp(0, 0)
