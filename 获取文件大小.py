
import os


# def getFileSize(filePath,size = 0): 定义获取文件大小的函数，初始文件大小是0

#     for root, dirs, files in os.walk(filePath): 

#         for f in files:

#             size += os.path.getsize(os.path.join(root, f))

#             print(f)

#     return size

# print(getFileSize('./yuanleetest'))



all_size = 0
def dir_size(dir_name):
    global all_size
    file_list = os.listdir(dir_name)
   # print(file_list)
    for file in file_list:
        file_path = os.path.join(dir_name,file)
        print(dir_name)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(size)
            all_size += size
            print(file_path)
        else:
            dir_size(dir_name)

print(dir_size('./yuanleetest'))