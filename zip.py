import zipfile

"""
# 압축할 파일 목록 생성
filelist = ['./0714/resource/data.dat', './0714/resource/data.txt']
# 파일 목록의 파일들을 압축해서 zip 파일 생성.
with zipfile.ZipFile('./0714/resource.zip', 'w') as zipFile:
    for temp in filelist:
        zipFile.write(temp)
"""

# zip 파일 압축 해제
zipfile.ZipFile('./0714/resource.zip').extractall()
