import pytesseract
from PIL import Image
test = open(r'C:\Users\picc\Desktop\test.txt', 'w')
for i in range(100, 101):
    test.seek(0)
    picAddr = r'C:\Users\picc\Desktop\100.png'.format(i)
    image = Image.open(picAddr)
    image = image.convert("L")
    image = image.resize((144, 90),Image.ANTIALIAS)
    width = image.size[0]
    heigh = image.size[1]
    # sign = ''' 123456789abcdefghijklmnopqrstuvwxyz*@#$%&!()|[]{}^.- '''
    # sign = ''' ~!z#$%^&*()_+[]{}|\;':",./<>?-|'/^,;!=()1cij '''
    sign = ''' ,. '''
    pic = ''
    # valist = image.load()
    for h in range(0, heigh):
        pic = ''
        for w in range(0, width):
            val = round(image.getpixel((w,h))/256*len(sign))
            if val >= len(sign):
                val = val - 1
            pic = pic + sign[val]
        test.writelines(pic + '\r\n')
        # print(pic)
    # image.show()
    # print(sign[36])
    # test.write(pic)
    test.flush()
# threshold = 200
# table=[]print(
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = image.point(table, '1')
# image.show()
# result = pytesseract.image_to_string(image)
# print(result)