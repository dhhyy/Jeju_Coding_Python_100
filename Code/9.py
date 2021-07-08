# 문제9 : sep과 end를활용한 출력방법

# 다음 소스 코드를 완성하여 날짜와 시간을 출력하시오.

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end= ' ')
print(hour, minute, second, sep=':')

# >> 출력
# 2019/04/26 11:34:27

# sep 정리
# sep옵션을 사용하여 띄어쓰기(공백) 말고 다른 문자 삽입 가능
# end 정리
# 문장이 끝날 때, 옵션을 정해줄 수 있음