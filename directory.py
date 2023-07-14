import os
"""
print(os.getcwd()) # 상대 경로를 사용할 때의 기준이 되는 경로
os.chdir('./0714') # 디렉토리 아래의 0714 로 변경
print(os.getcwd()) # C:\vscode\0714
"""

try: 
    """
    # 읽기용으로 파일 열기
    file = open('./0714/data.txt', 'w', encoding='utf-8')
    # 파일에 문자열 입력
    file.write("문자열 입력")
    # 문자열이 list로 있을 때
    lines = ["abc", "park", "bdfs"]
    file.writelines(lines) # abcparkbdfs
    """
    
    readFile = open('./0714/data.txt', 'r', encoding='utf-8')
    line = readFile.readline() # 1줄 읽기
    print(line)
    for lines in readFile: # 줄 단위로 읽기
        print(lines)
    allFile = readFile.read() # 전체 읽기
    print(allFile)
    """
    with open('./0714/data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            """
except Exception as e:
    print("파일 처리 중 예외 발생", e)
#finally : 
    # file.close()
    # readFile.close()
