def binary_digit(num, digit) : # num의 이진수 digit자리가 1임을 판별
    q = num
    for i in range(digit+1) :
        q =q//2

    if q == 1 :
        return True
    else :
        return False

power = int (input('질문 횟수를 입력하세요. (자연수) : '))
number = 0

for d in range(power) :

    for n in range(2**power) :
        if binary_digit(n,d) :
            print(n, end = ' ')

    ans = input('- 생각한 숫자가 있나요? (Y/N): ')

    if ans == 'Y' or ans == 'y' :
        number += 2**d


print ('number :', number)
