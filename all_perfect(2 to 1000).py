def all_perfect() -> None:
    for n in range(2, 1001):
        sum = 1  # 1 is always a divisor
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                sum =sum + i
        if sum == n:
            print(n, "is a Perfect Number")

all_perfect()
