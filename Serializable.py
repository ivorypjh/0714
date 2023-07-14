class DTO:
    def __init__(self, name = 'default', num = 0) -> None:
        self.__name = name
        self.__num = num

    # getter
    @property
    def num(self):
        return self.__num
    @property
    def name(self):
        return self.__name
    
    # setter
    @num.setter
    def num(self, num):
        self.__num = num
    @name.setter
    def name(self, name):
        self.__name = name

    # 인스턴스를 print 함수에 대입했을 때 호출되는 메서드 - 오버라이딩
    # 출력을 편리하게 만들기 위해서 재정의 - 디버깅이 목적
    def __str__(self) -> str:
        return str(self.__name) + " : " + str(self.__num)

# 파일에 기록할 데이터(인스턴스) 생성
data1 = DTO("park", 1)
data2 = DTO("lee", 2)
print(data1, data2, sep="\n")

datas = [data1, data2]

# 데이터를 기록하기 위해 import
import pickle
try:
    with open('./0714/resource/data.dat', 'wb') as file:
        # file 에 데이터를 serializable
        # 일반적인 방식으로는 읽어낼 수 없음
        pickle.dump(datas, file)
except Exception as e:
    print("예외 발생")
    print(e)

try:
    with open('./0714/resource/data.dat', 'rb') as file:
        # serializable 된 데이터를 읽기 - Deserializable
        # 읽어와서 변수에 list 형태로 저장
        result = pickle.load(file)
        for item in result:
            print(item)
except Exception as e:
    print("예외 발생")
    print(e)