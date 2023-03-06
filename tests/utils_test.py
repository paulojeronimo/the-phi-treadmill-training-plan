import pytest

from the_phi_treadmill.utils import merge_3, round_to_even_values, trunc_to_n_decimals

input_l = [1.11111, 2.22222, 3.33333]


@pytest.mark.parametrize(
    "input_l, decimals, expected",
    [
        (input_l, 1, [1.1, 2.2, 3.3]),
        (input_l, 2, [1.11, 2.22, 3.33]),
        (input_l, 3, [1.111, 2.222, 3.333]),
    ],
)
def test_trunc_to_n_decimals(input_l, decimals, expected):
    assert [*trunc_to_n_decimals(input_l, decimals)] == expected


@pytest.mark.parametrize(
    "input_l, decimals, expected",
    [
        (input_l, 1, [1.2, 2.3, 3.4]),
        (input_l, 2, [1.12, 2.23, 3.34]),
        (input_l, 3, [1.112, 2.223, 3.334]),
    ],
)
def test_round_to_even_values(input_l, decimals, expected):
    print(f"{expected=}")
    generated = [*round_to_even_values(input_l, decimals)]
    print(f"{generated=}")
    assert generated == expected


@pytest.mark.parametrize(
    "input_l, decimals, expected",
    [
        (input_l, 1, [1.2, 2.2, 3.4]),
        # <- TODO: FIX THE BUG WHEN RUNNING THIS!
        # (input_l, 2, [1.12, 2.22, 3.34]),
        (input_l, 3, [1.112, 2.222, 3.334]),
    ],
)
def test_trunc_and_round(input_l, decimals, expected):
    generated = round_to_even_values(
            trunc_to_n_decimals(input_l, decimals), decimals)
    assert [*generated] == expected


def test_merge_3():
    list1 = [1, 4, 7, 10, 13]
    list2 = [2, 5, 8, 11]
    list3 = [3, 6, 9, 12]
    expected = [*range(1, 14)]
    generated = [*merge_3(list1, list2, list3)]
    assert generated == expected
