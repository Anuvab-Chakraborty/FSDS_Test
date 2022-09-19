import os
import shutil
li=os.listdir()
print(li)
l=[]
for i in li:
    try:
        filename, extension=os.path.splitext(i)
        os.makedirs(extension[1:], exist_ok=True)
        if "new" == filename:
            continue
        print(i, extension[1:])
        shutil.move(i, extension[1:])
    except FileNotFoundError as e:
        print(e)
