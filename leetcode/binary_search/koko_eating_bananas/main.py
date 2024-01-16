from typing import List
import math


class Solution:
    def feasible(self, piles, h, speed) -> bool:
        return sum(math.ceil(pile / speed) for pile in piles) <= h

    # Time complexity: O(n log m) where m is the max(piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            speed = (l + r) // 2
            if self.feasible(piles, h, speed):
                r = speed
            else:
                l = speed + 1

        return l

    """
    # My implementation:
    # Sucks at large values...
    # Time inefficient: O(nlogn)    
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)

        avg_hours_per_pile = h // n
        max_pile = -1
        time = 0
        speed = 0

        while time <= h:
            curr_speed = math.ceil(piles[max_pile] / avg_hours_per_pile)
            total_time = [math.ceil(pile / curr_speed) for pile in piles]
            time = sum(total_time)

            # print(total_time, time, curr_speed, avg_hours_per_pile)
            # input()

            if time == h:
                return curr_speed

            if time < h:
                speed = curr_speed
                if max_pile == -n:
                    return speed
                max_pile -= 1
                continue

        return speed
    """


# Large values
print(
    Solution().minEatingSpeed(
        [
            873375536,
            395271806,
            617254718,
            970525912,
            634754347,
            824202576,
            694181619,
            20191396,
            886462834,
            442389139,
            572655464,
            438946009,
            791566709,
            776244944,
            694340852,
            419438893,
            784015530,
            588954527,
            282060288,
            269101141,
            499386849,
            846936808,
            92389214,
            385055341,
            56742915,
            803341674,
            837907634,
            728867715,
            20958651,
            167651719,
            345626668,
            701905050,
            932332403,
            572486583,
            603363649,
            967330688,
            484233747,
            859566856,
            446838995,
            375409782,
            220949961,
            72860128,
            998899684,
            615754807,
            383344277,
            36322529,
            154308670,
            335291837,
            927055440,
            28020467,
            558059248,
            999492426,
            991026255,
            30205761,
            884639109,
            61689648,
            742973721,
            395173120,
            38459914,
            705636911,
            30019578,
            968014413,
            126489328,
            738983100,
            793184186,
            871576545,
            768870427,
            955396670,
            328003949,
            786890382,
            450361695,
            994581348,
            158169007,
            309034664,
            388541713,
            142633427,
            390169457,
            161995664,
            906356894,
            379954831,
            448138536,
        ],
        943223529,
    )
)  # passed 2

# Small values
# print(Solution().minEatingSpeed([312884470], 312884469))  # passed 2
# print(Solution().minEatingSpeed([3, 6, 7, 11], 8))  # passed 4
# print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))  # passed 30
# print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6))  # passed 23
