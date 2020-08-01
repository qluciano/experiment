from src.util.goodies import fib


def test_fib_handles_base_cases():
    assert fib(0) == 1
    assert fib(1) == 1


def test_fib_holds_recurrence_relation(bound=100):
    for n in range(2, bound):
        assert fib(n) == fib(n - 1) + fib(n - 2)
