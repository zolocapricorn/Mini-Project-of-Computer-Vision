import os

totalFiles = 0
paths = 'E:/Github/Computer-Vision/Mini-Project/CUB_200_2011/images'
for bases, dirs, files in os.walk(paths):
    for Files in files:
        totalFiles += 1
    print(bases.split("\\")[-1])
