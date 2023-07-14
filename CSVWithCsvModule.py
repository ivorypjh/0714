import csv
"""
data = []
with open('./0714/경기도 가평군_산사태 취약지역 현황_20230713.csv', 'r') as file:
    # 줄 단위로 읽어서 list를 만들어주는 reader 객체를 생성
    # 기본적인 읽어오기와 다르게 \n 이 남지 않음
    rdr = csv.reader(file)
    for line in rdr:
        data.append(line)
print(data)
"""
# csv 파일에 데이터 write
# read로 오픈하면 쓰기 권한이 없기 때문에 not writable 에러가 발생
# w 를 이용해서 write 로 오픈하면 기존의 내용을 지우고 덮어써서 기록하는게 문제
# 이어서 작성하려면 'a' 를 사용해줘야 함
with open('./0714/test.csv', 'a', encoding='utf-8') as file:
    wr = csv.writer(file)
    wr.writerow(['서울', '서대문구'])
    wr.writerow(['서울', '서초구'])