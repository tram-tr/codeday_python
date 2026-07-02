def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


def main():
    for i in range(1, 101):
        print(i)
        res = fizzbuzz(i)
        if res != str(i):
            print(res)


if __name__ == "__main__":
    main()
