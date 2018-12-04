import random
import os
os.chdir(r'C:\Users\picc\Desktop\新建文件夹\spideremp\images')
files = os.listdir()
print(files)
file = random.randint(0,len(files))
print(files[file])