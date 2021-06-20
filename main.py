import math


total = 1000000
m50 = 10
m10 = 25
m5 = 30
m1 = 100
def sys(n, total):
    f = False
    if n < total:
        f = True
    return f
def money(n, total, m50, m10, m5, m1):
    while n > 0:
        while total > 0:
            if math.floor(n / 50000) > 0 and m50 > 0:
                a = math.floor(n / 50000)
                if m50 >= a:
                    total = total - a * 50000
                    n = n - a * 50000
                    m50 = m50 - a
                    break
                elif m50 > 0:
                    total = total - m50 * 50000
                    n = n - m50 * 50000
                    m50 = m50 - m50
                    break
            elif math.floor(n / 10000) > 0 and m10 > 0:
                a = math.floor(n / 10000)
                if m10 >= a:
                    total = total - a * 10000
                    n = n - a * 10000
                    m10 = m10 - a
                    break
                elif m10 > 0:
                    total = total - m10 * 10000
                    n = n - m10 * 10000
                    m10 = m10 - m10
                    break
            elif math.floor(n / 5000) > 0 and m5 > 0:
                a = math.floor(n / 5000)
                if m5 >= a:
                    total = total - a * 5000
                    n = n - a * 5000
                    m5 = m5 - a
                    break
                elif m5 > 0:
                    total = total - m5 * 5000
                    n = n - m5 * 5000
                    m5 = m5 - m5
                    break
            elif math.floor(n / 1000) > 0 and m1 > 0:
                a = math.floor(n / 1000)
                if m1 >= a:
                    total = total - a * 1000
                    n = n - a * 1000
                    m1 = m1 - a
                    break
                elif m1 > 0:
                    total = total - m1 * 1000
                    n = n - m1 * 1000
                    m1 = m1 - m1
                    break




    return total, m50, m10, m5, m1















while(True):
    bardash = int(input('Enter :'))
    if bardash <= 250000 and bardash >= 1000 and bardash <= total:
        total, m50, m10, m5, m1 = money(bardash, total, m50, m10, m5, m1)
        print('The rest of the bank:', total)
        print('The rest of the bank 50000:', m50)
        print('The rest of the bank 10000:', m10)
        print('The rest of the bank 5000:', m5)
        print('The rest of the bank 1000:', m1)
    else:
        print('out of range!')




