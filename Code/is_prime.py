def is_prime(num:int) -> bool:

    for i in range(2, num - 1):
        if num % i == 0:
            return False

    return True

num = int(input('num = '))

print(f'Is prime?\n{is_prime(num)}')
