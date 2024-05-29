'''
* 내장함수 map()
- map()은 첫번째 인수로 함수를 지정하고, 두 번째 인수로
리스트를 지정하면 해당 리스트 내부 요소값을 일괄적으로
첫번째 인수로 지정한 함수에 인수로 전달합니다.
'''

def calc_stepsum(begin,end,step=1):
    sum = 0
    for n in range(begin,end+1,step):
        sum += n
    return sum 

print(calc_stepsum(1,10))
print(calc_stepsum(1,10,2))

# 기본값이 지정된 매개변수를 오른쪽으로 몰아 주셔야 합니다.
def calc_sum(end,begin=0,step=1):
    sum = 0
    for n in range(begin,end+1,step):
        sum += n
    return sum 

print(calc_sum(100))