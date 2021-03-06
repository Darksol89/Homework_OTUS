import pytest

@pytest.mark.parametrize("a, b, c",
                         {
                             (1, 2, 3),
                             (2, 3, 5),
                             (1, 1, 4),
                             (0, 1, 1)
                         })
def test_sum(a, b, c):
    """
    Если сложить 2 + 2 получится 4
    """
    assert a + b == c