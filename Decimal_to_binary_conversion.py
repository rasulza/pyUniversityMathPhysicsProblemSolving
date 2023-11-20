
def decimal_to_binery(decimal_num):
    binery_num = ''

    while decimal_num != 0:
        division_num = decimal_num // 2
        multiplication_num = division_num * 2
        remainder = decimal_num - multiplication_num
        binery_num += str(remainder)
        decimal_num = division_num

    return binery_num[::-1]

          
result = decimal_to_binery(int(input("inter number: ")))
print(result)