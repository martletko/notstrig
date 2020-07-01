import math
import sys
import time
import os
import multiprocessing
import psutil


def Atkin_Habr(start: int, b: int, step: int):
    is_primes = dict((key, False) for key in range(b+1))
    sqrt = int(math.sqrt(b)) + 1
    start_time = time.time()

    for x in range(start, sqrt, step):
        for y in range(1, sqrt):
            x2 = x*x
            y2 = y*y
            n = 4 * x2 + y2
            if (n <= b and (n % 12 == 1 or n % 12 == 5)):
                is_primes[n] = not (is_primes[n])

            n -= x2
            if n <= b and n % 12 == 7:
                is_primes[n] = not (is_primes[n])

            n -= 2 * y2
            if (x > y and n <= b and n % 12 == 11):
                is_primes[n] = not (is_primes[n])
    new_time = time.time()
    if new_time - start_time > 1:
        print("считаем")

    for n in range(5, sqrt, 2):
        if is_primes[n]:
            s = n*n
            for k in range(s, b, s):
                is_primes[k] = False

    return is_primes


if __name__ == "__main__":
    if len(sys.argv) == 2:
        border = sys.argv[1]
        if str.isnumeric(border) is False:
            print('wrong input')
            sys.exit()
    else:
        print('wrong input')
        sys.exit()
    border_int = int(border)
    if border_int < 10000001:
        start_time = time.time()
        sqrt = int(math.sqrt(border_int)) + 1

        is_primes_mock = dict((key, False) for key in range(border_int + 1))

        with multiprocessing.Pool(processes=3) as pool:
            results = pool.starmap(Atkin_Habr, [(1, border_int, 3),
                                                (2, border_int, 3),
                                                (3, border_int, 3)])
            for result in results:
                for num1 in result:
                    if result[num1]:
                        is_primes_mock[num1] = not is_primes_mock[num1]

        for n in range(5, sqrt, 2):
            if is_primes_mock[n]:
                s = n*n
                for k in range(s, border_int, s):
                    is_primes_mock[k] = False

        primes = [2, 3]

        pr_name = 'primes.txt'
        with open(pr_name, "w", encoding='utf8') as file:
            file.write('2\n')
            file.write('3\n')
            for num in is_primes_mock:
                if is_primes_mock[num]:
                    tmp = str(num) + '\n'
                    file.write(tmp)
            print("done writing")

        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        start_time = time.time()
        sqrt = int(math.sqrt(border_int)) + 1
        primes = Atkin_Habr(1, border_int, 1)
        pr_name = 'primes.txt'
        with open(pr_name, "w", encoding='utf8') as file:
            file.write('2\n')
            file.write('3\n')
            for num in primes:
                if primes[num]:
                    tmp = str(num) + '\n'
                    file.write(tmp)
            print("done writing")
