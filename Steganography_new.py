import base64

from PIL import Image


class PNG_RGBA_INFO(object):
    def __init__(self, img):
        self.__width = img.size[0]
        self.__height = img.size[1]
        self.__pixels_list = img.getdata()  # [(r,g,b,a),(r,g,b,a),...,(r,g,b,a)]
        self.__cleared_pixels_list = []
        self.__rgba_list = []
        self.__str_01 = ''
        self.__str_01_len = 0

    def clearLSB(self):
        self.__cleared_pixels_list = []
        for i in range(self.__width * self.__height):
            L = []
            for j in range(4):
                if j != 3:
                    if self.__pixels_list[i][j] % 2 == 1:
                        L.append(self.__pixels_list[i][j] - 1)  # lsb set 0
                    else:
                        L.append(self.__pixels_list[i][j])  # lsb == 0
                else:
                    L.append(self.__pixels_list[i][j])  # append alpha
            self.__cleared_pixels_list.append(L)

    def generateSTR01(self, string):
        self.__str_01 = ''
        for s in string:
            self.__str_01 += bin(ord(s))[2:].rjust(8, '0')
        self.__str_01_len = len(self.__str_01)


    def lsb_encrypt(self, mod):
        steg_mod = {'R': 0, 'G': 1, 'B': 2}[mod]  # mod 0/1/2 meaning r/g/b
        if not self.__str_01:  # empty str_01 ''
            raise RuntimeError('Empty self.__str_01,did you forget to call generateSTR01()?')
        if self.__str_01_len > len(self.__cleared_pixels_list):
            raise RuntimeError('Encrypt str is too long')
        for i in range(self.__str_01_len):
            if self.__str_01[i] == '1':
                self.__cleared_pixels_list[i][steg_mod] += 1



    def generateRGBALIST(self, use_origin_rgba=False):  # self.__rgba_list = [r,g,b,a,r,g,b,a,...,r,g,b,a]
        self.__rgba_list = []
        if use_origin_rgba:
            pixels_list = self.__pixels_list
        else:
            pixels_list = self.__cleared_pixels_list
        for i in range(self.__width * self.__height):
            for j in range(4):
                self.__rgba_list.append(pixels_list[i][j])


    def rebuildPNG(self, path='./'):
        if not self.__rgba_list:  # empty list []
            raise RuntimeError('Empty self.__rgba_list,did you forget to call generateRGBALIST()?')
        Image.frombytes('RGBA', (self.__width, self.__height), bytes(self.__rgba_list)).save(path)


    def getEncryptedInfo(self, mod='R'):
        byte_str_01 = ''
        secret_str = ''
        decrypt_mod = {'R': 0, 'G': 1, 'B': 2}[mod]  # mod 0/1/2 meaning r/g/b
        for i in range(self.__width * self.__height):
            if self.__pixels_list[i][decrypt_mod] % 2 == 0:
                byte_str_01 += '0'
            else:
                byte_str_01 += '1'
        for i in range(len(byte_str_01) // 8):
            one_byte = byte_str_01[i * 8:i * 8 + 8]
            secret_str += chr(int(one_byte, base=2))            # print(chr(int('01100001',base = 2)))      print(bin(ord('a')))
        return secret_str




def encrypt(png_file_path, output_file_path, str_to_be_hidden, mod='R', b64=True):
    my_img = Image.open(png_file_path)
    png_rgba = PNG_RGBA_INFO(my_img)  # 初始化一个PNG_RGBA_INFO对象
    png_rgba.clearLSB()  # 清空全文件lsb
    if b64:
        str_to_be_hidden = str(base64.b64encode(str_to_be_hidden.encode('utf-8')), 'utf-8')
    png_rgba.generateSTR01(str_to_be_hidden)  # 传入待encrypt字符串
    png_rgba.lsb_encrypt(mod)  # 开始在self.__cleared_pixels_list上用self.__str_01进行lsb隐写
    png_rgba.generateRGBALIST()  # 准备生成新PNG
    png_rgba.rebuildPNG(output_file_path)
    print('Done')


def decrypt(png_file_path, b64=True):
    my_img = Image.open(png_file_path)
    png_rgba = PNG_RGBA_INFO(my_img)
    secret_str = png_rgba.getEncryptedInfo('R')
    if b64:
        secret_str = str(base64.b64decode(secret_str), 'utf-8')
    print(secret_str)
