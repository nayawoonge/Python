#입력 정수 판별하기
n = int(input('정수 입력 : '))

result = '입력된 정수는 100~1000 사이에 없습니다'

if n >= 100 and n <= 1000 :
  result = '입력된 정수는 100~1000 사이에 있습니다'

print('입력된 정수 : %d' %n)
print('%s' %result)