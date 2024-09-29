def check_fibo(num: int) -> bool:
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

