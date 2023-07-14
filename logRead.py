import csv
from collections import Counter

"""
# 성공 횟수(200) 세기
cnt = 0
with open('./0714/resource/log.txt', 'r', encoding='utf-8') as file:
    # 한글이 없는 로그 파일이므로 encoding을 넣지 않아도 됨.
    rdr = csv.reader(file)
    for item in rdr: # 줄 단위로 읽기
        result = str(item).split() # split을 통해 list 생성
        # 9번째에 위치한 성공 여부와 '200'을 비교
        if result[8] == '200':
            cnt += 1
print(cnt)
"""

"""
# ip 별 접속 횟수 세기
cnt = Counter()
with open('./0714/resource/log.txt', 'r', encoding='utf-8') as file:
    for item in file: # 줄 단위로 읽기
        result = item.split() # split을 통해 list 생성
        cnt[result[0]] += 1

for ip in cnt:
    print(ip,'\t :', cnt[ip])
"""

# ip 별 트래픽 합계
cnt = Counter()
with open('./0714/resource/log.txt', 'r', encoding='utf-8') as file:
    for item in file: # 줄 단위로 읽기
        result = item.split() # split을 통해 list 생성
        try:
            cnt[result[0]] += int(result[9]) # 트래픽만큼 더하기
        except Exception as e: # 숫자 대신에 - 등이 들어가 있는 예외 처리
            print(e) # int로 바꿀 수 없는 잘못된 트래픽이 있는 경우 출력
            cnt[result[0]] += 0
# 결과 출력
for ip in cnt:
    print(ip,'\t :', cnt[ip])
# 가장 많은 트래픽을 보낸 ip 상위 5개
print(cnt.most_common(5))
