from typing import List
import math


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        fleets = 0
        while len(time) > 1:
            lead = time.pop()
            if lead < time[-1]:
                fleets += 1  # If lead arrives sooner, it can't be caught
            else:
                time[-1] = lead  # Else, fleet arrives at later time 'lead'
        return fleets + bool(time)  # Add remaining car, if it exists

        # n = len(position)

        # cars = sorted(
        #     [(p, s) for p, s in zip(position, speed)],
        #     key=lambda x: x[0],
        # )
        # stack = [cars[0]]

        # for i in range(1, n):
        #     prev_pos, prev_speed = stack[-1]
        #     curr_pos, curr_speed = cars[i]

        #     prev_time = math.ceil((target - prev_pos) / prev_speed)
        #     curr_time = math.ceil((target - curr_pos) / curr_speed)

        #     if curr_time >= prev_time:
        #         stack.pop()

        #     # print(stack, curr_pos, curr_speed, curr_time)

        #     stack.append((curr_pos, curr_speed))

        # i = 1

        # while len(stack) > 1:
        #     changed = False
        #     prev_pos, prev_speed = stack[i - 1]
        #     curr_pos, curr_speed = stack[i]

        #     prev_time = math.ceil((target - prev_pos) / prev_speed)
        #     curr_time = math.ceil((target - curr_pos) / curr_speed)

        #     if curr_time >= prev_time:
        #         stack.pop()
        #         changed = True

        #     if not changed:
        #         break

        # return len(stack)


print(Solution().carFleet(10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4]))
print(
    Solution().carFleet(
        target=13, position=[10, 2, 5, 7, 4, 6, 11], speed=[7, 5, 10, 5, 9, 4, 1]
    )
)  # answer is
print(Solution().carFleet(target=10, position=[0, 4, 2], speed=[2, 1, 3]))  # passed
print(Solution().carFleet(target=10, position=[6, 8], speed=[3, 2]))  # passed
print(
    Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
)  # passed
