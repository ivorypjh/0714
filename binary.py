with open('./0714/test.bin', 'wb') as file:
    file.write('테스트 1번'.encode())
with open('./0714/test.bin', 'rb') as file:
    content = file.read()
    print(content) # 코드가 출력됨
    print(content.decode()) # 테스트 1번