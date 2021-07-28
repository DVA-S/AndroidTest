#此脚本仅在红米 Note 7 上进行过测试。
import io

#图片位置（偏移量）
#未解锁BL时开机第一屏
offset1 = 0x4000

#系统损坏提示图
offset2 = 0xE79FAE

#fastboot提示图
offset3 = 0x73EFD8

#解锁BL时开机第一屏
offset4 = 0x15B4F84
 
#以二进制格式打开一个文件只用于写入。
#如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
#如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
outpt = open("logo_new.img", "wb")

#“rb”以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
outpt.seek(offset1)
img = open("01.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset3)
img = open("03.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset2)
img = open("02.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset4)
img = open("04.bmp", "rb")
outpt.write(img.read())

outpt.close()
