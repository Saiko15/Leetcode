class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] *n
        stk = []

        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stk
            while stk and temperatures[stk[-1]] < curr_temp:
                prev_day = stk.pop()
                answer[prev_day] = curr_day - prev_day
            stk.append(curr_day)

        return answer
            