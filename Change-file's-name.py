import os

totalFiles = 0
lists = []
paths_find_folder_name = 'E:/Github/Computer-Vision/Mini-Project/CUB_200_2011/images'
for bases, dirs, files in os.walk(paths_find_folder_name):
    for Files in files:
        totalFiles += 1
    lists.append(bases.split("\\")[-1])



def main():
    for name in lists[1::]:
        print(name)
        paths = "E:/Github/Computer-Vision/Mini-Project/CUB_200_2011/images/" + name + "/"
        for count, filename in enumerate(os.listdir(paths)):
            dst = name[4::] + " " + "%04d" % (int(str(count+1))) + ".jpg"
            src = paths+filename
            dst = paths+dst
            os.rename(src, dst)
if __name__ == '__main__':
    main()
