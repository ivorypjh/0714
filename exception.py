try:
    var = int(input("수를 입력하세요 : "))
    if var == 1:
        # 강제로 예외 발생
        raise ValueError("강제로 예외 발생")
    # 2인 경우에 강제로 중단
    assert var != 2
    result = 100 / var
    print(result)

except ValueError as e:
    print("잘못된 데이터 입력")
    print(e)

except ZeroDivisionError as z:
    print("0으로는 나눌 수 없음")
    print(z)

else:
    print("예외가 발생하지 않은 경우 출력")

finally:
    print("무조건 수행되는 구문")