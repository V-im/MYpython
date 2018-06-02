import re
import os
import time


t = [2, 3, 4, 5, 6, 22, 42, 62, 82, 102, 103, 104, 105, 106, 126, 146, 166, 186, 206, 226, 225, 224, 223, 222,
     8, 9, 10, 11, 12, 32, 52, 72, 92, 108, 109, 110, 111, 112, 128, 148, 168, 188, 208, 228, 229, 230, 231, 232,
     14, 15, 16, 17, 18, 34, 38, 54, 58, 74, 78, 94, 98, 114, 118, 134, 138, 154, 158, 174, 178, 194, 198,
     214, 218, 234, 235, 236, 237, 238]


def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isdir(path):
        os.chdir(path)
        dir = os.listdir(path)
        print(os.getcwd())
        print(os.listdir())
        for file_name in dir:
            lists = file_name.split('.')  # 分割出文件与文件扩展名
            file_ext = lists[-1]  # 取出后缀名(列表切片操作)
            img_ext = ['bmp', 'jpeg', 'png', 'jpg', 'BMP', 'JPEP', 'PNG', 'JPG']
            if file_ext in img_ext:
                for tt in t:
                    try:
                        os.rename(file_name, ("%d.jpg") % tt)
                        print("%s已改名" % file_name)
                        i += 1
                        os.chdir("./")
                    except:
                        pass



img_add = input("请输入要查找地址：")
start = time.time()
i = 0
change_name(img_add)
c = time.time() - start
print('程序运行耗时:%0.2f' % (c))
print('总共处理了 %s 张图片' % (i))
