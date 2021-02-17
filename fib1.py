from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

def fib1(n: int) -> int:
	if n not in memo:
		memo[n] = fib1(n-1) + fib1(n-2)
	return memo[n]


if __name__ == "__main__":
    print(fib1(5))
    print(fib1(50))
# Note that this example is purposefully wrong.
