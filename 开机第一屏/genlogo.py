import io

offset0 = 0x3000
offset1 = 0x4000
offset2 = 0xE79FAE
offset3 = 0x73EFD8
offset4 = 0x15B4F84
 
#以二进制格式打开一个文件只用于写入。
#如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
#如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
outpt = open("logo_new.img", "wb")

#range()：生成小于0xDCCFFF(十进制14471167)的随机数。
emptyContent =  [0 for i in range(0xDCCFFF)]

magic = [0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
                0x2B, 0x00, 0x00, 0x00, 0xC1, 0x01, 0x00, 0x00, 0xEF, 0x01, 0x00, 0x00,
                0xDE, 0x07, 0x00, 0x00, 0x26, 0x00, 0x00, 0x00, 0x96, 0x01, 0x00, 0x00,
                0x2E, 0x00, 0x00, 0x00, 0xEF, 0x05, 0x00, 0x00, 0xEF, 0x05, 0x00, 0x00]

#bytearray()方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
outpt.write(bytearray(emptyContent))

#seek() 方法用于移动文件读取指针到指定位置。
#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
outpt.seek(offset0)
outpt.write(bytearray(magic))

#“rb”以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
outpt.seek(offset1)
img = open("01.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset2)
img = open("02.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset3)
img = open("03.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset4)
img = open("04.bmp", "rb")
outpt.write(img.read())

outpt.close()
