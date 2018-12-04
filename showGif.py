import pygame
from sys import exit
from PIL import Image
background_image = r'C:\Users\picc\Desktop\10.jpg'
mouse_image = r'C:\Users\picc\Desktop\23.jpg'

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建了一个窗口
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE, 32)
# 设置窗口标题
pygame.display.set_caption("小黄鸭")

# 加载并转换图像
background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()
sign = ''' | '''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            exit()
    # screen.blit(background, (0, 0))  # 画上背景图

    # screen.blit(font.render('测试数据', True, (0, 0, 0)), (600, 100))

    x, y = pygame.mouse.get_pos()  # 获得鼠标位置
    # 计算光标左上角位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    # 画上光标
    # screen.blit(mouse_cursor, (x, y))
    bg_color=(255,255,204)
    k = 0
    for i in range(0, 37):
        fontlist = []
        textlist = []
        picAddr = r'C:\Users\picc\Desktop\Gifsplit\导出\{}.jpg'.format(i)
        image = Image.open(picAddr)
        image = image.convert("L")
        image = image.resize((160, 80), Image.ANTIALIAS)
        width = image.size[0]
        heigh = image.size[1]
        # sign = ''' 123456789abcdefghijklmnopqrstuvwxyz*@#$%&!()|[]{}^.- '''
        pic = ''
        all = ''
        # valist = image.load()
        for h in range(0, heigh):
            all = ''
            pic = ''
            for w in range(0, width):
                val = round(image.getpixel((w, h)) / 256 * len(sign))
                if val >= len(sign):
                    val = val - 1
                pic = pic + sign[val]
            # print(pic)
            k = + k
            all = pic + '\n' + all
            font = pygame.font.SysFont("MicrosoftYaHei", 14)
            screen.blit(font.render(all, True, (0, 0, 0)), (50, 0+10*h))
            # 刷新画面
        pygame.display.update()
        # screen.fill(bg_color)
        screen.blit(background, (0, 0))  # 画上背景图

        # image.show()
        # print(sign[36])
