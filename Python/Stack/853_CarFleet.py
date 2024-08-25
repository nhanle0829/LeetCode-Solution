class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(p, s) for p, s in zip(position, speed)]
        position_speed.sort(reverse=True)
        stack = []

        for p, s in position_speed:
            time_reach_target = (target - p) / s
            if stack and time_reach_target <= stack[-1]:
                time_reach_target = stack[-1]
                stack.pop()
            stack.append(time_reach_target)
        return len(stack)