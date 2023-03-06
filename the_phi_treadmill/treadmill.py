from math import sqrt
from utils import merge_3, round_to_even_values, trunc_to_n_decimals

PHI = (1 + sqrt(5)) / 2


class Treadmill:
    def __init__(self, only_even_values: bool):
        self.only_even_values = only_even_values

    def get_speeds(self, speeds):
        return (
            [*round_to_even_values(trunc_to_n_decimals(speeds))]
            if self.only_even_values
            else [*trunc_to_n_decimals(speeds)]
        )

    def calculate_8_speeds(self, min_speed):
        arr0 = [min_speed * PHI**n for n in range(5)]
        arr1 = [(arr0[i] + arr0[i + 1]) / 2 for i in range(4)]
        return self.get_speeds([x for n in zip(arr0, arr1) for x in n])

    def calculate_13_speeds(self, min_speed):
        arr0 = [min_speed * PHI**n for n in range(5)]
        arr1 = [(3 * arr0[i] + arr0[i + 1]) / 4 for i in range(4)]
        arr2 = [(arr0[i] + 3 * arr0[i + 1]) / 4 for i in range(4)]
        return self.get_speeds([*merge_3(arr0, arr1, arr2)])


if __name__ == "__main__":
    print(Treadmill(False).calculate_8_speeds(3.3))
    print(Treadmill(False).calculate_13_speeds(3.3))
