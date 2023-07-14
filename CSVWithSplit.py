# csv 파일을 읽어서 list로 변환
# 마지막 데이터에는 \n 이 추가됨
# 마지막 데이터는 \n 을 제거해줘야 함.
data = []
with open('./0714/경기도 가평군_산사태 취약지역 현황_20230713.csv', 'r') as file:
    for line in file:
        arr = line.split(',')
        data.append(arr)
print(data)