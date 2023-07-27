'''
06.10 Poison: You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which
    can be used to detect poison. A single drop of poison will turn the test strip positive permanently.
    You can put any number of drops on a test strip at once and you can reuse a test strip as many times
    as you'd like (as long as the results are negative). However, you can only run tests once per day and
    it takes seven days to return a result. How would you figure out the poisoned bottle in as few days
    as possible?

    FOLLOW UP

    Write code to simulate your approach.
'''

import random
from typing import List, Optional

DAYS_FOR_RESULT = 7

class _TestStrip:
    def __init__(self) -> None:
        self.has_poison = False
        self.day_poisoned: Optional[int] = None

# Time: O(1) Space: O(1)
class World:
    def __init__(
        self, num_test_strips: int, num_bottles: int, poisoned_bottle_num: int
    ) -> None:
        self._num_test_strips = num_test_strips
        self._test_strips = [_TestStrip() for i in range(num_test_strips)]
        self._num_bottles = num_bottles
        self._poisoned_bottle_num = poisoned_bottle_num
        self._day = 0

    @property
    def num_bottles(self) -> int:
        return self._num_bottles

    @property
    def num_test_strips(self) -> int:
        return self._num_test_strips

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        if day < self._day:
            raise ValueError("day cannot be decreased")
        self._day = day

# Time: O(1) Space: O(1)
    def add_drop(self, bottle_num: int, test_strip_num: int) -> None:
        test_strip = self._test_strips[test_strip_num]
        if bottle_num == self._poisoned_bottle_num and not test_strip.has_poison:
            test_strip.has_poison, test_strip.day_poisoned = True, self.day

# Time: O(n) Space: O(1)
    def positive_test_strips(self) -> List[int]:
        res: List[int] = []
        for test_strip_num, test_strip in enumerate(self._test_strips):
            if (
                test_strip.has_poison
                and self.day - test_strip.day_poisoned >= DAYS_FOR_RESULT
            ):
                res.append(test_strip_num)
        return res

# Time: O(n * n) Space: O(1)
def find_poison(world: World) -> int:
    for i in range(world.num_bottles):
        for j in range(world.num_test_strips):
            if i & (1 << j):
                world.add_drop(bottle_num=i, test_strip_num=j)
    world.day += DAYS_FOR_RESULT
    return sum(1 << i for i in world.positive_test_strips())

# Time: O(n * n) Space: O(1)
def test_find_poison():
    poisoned_bottle_num = random.randrange(1000)
    world = World(
        num_bottles=1000, num_test_strips=10, poisoned_bottle_num=poisoned_bottle_num
    )
    assert find_poison(world) == poisoned_bottle_num
    return poisoned_bottle_num, world.day

# Time: O(n * n) Space: O(1)
def example():
    poisoned_bottle_num, days = test_find_poison()
    print("Found poison in bottle number", poisoned_bottle_num, "in", days, "days.")

if __name__ == "__main__":
    example()