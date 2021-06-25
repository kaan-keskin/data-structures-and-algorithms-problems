from math import log, modf, floor
 
def p(L, n, pwr=2):
    L = int(abs(L))
    digits_count_for_L = floor(log(L, 10))
    log10pwr = log(pwr, 10)
    power_of_number, found_digits = -1, 0
    while found_digits < n:
        power_of_number += 1
        leading_digits = floor(10**(modf(power_of_number * log10pwr)[0] + digits_count_for_L))
        if leading_digits == L:
            found_digits += 1
    return power_of_number
 
if __name__ == '__main__':
    for L, n in [(12, 1), (12, 2), (123, 45), (123, 12345), (123, 678910)]:
        print(f"p({L}, {n}) =", p(L, n))
