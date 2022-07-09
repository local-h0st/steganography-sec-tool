import Steganography

if __name__ == '__main__':
    my_secret = 'Hello, I am PureLov3, this is a test for my Steganography tool, this text line is supposed to be hidden in a png file, unless you use my tool, you won\'t find it : )'
    file_input = 'images/car.png'
    file_output = './img_edited/car_with_secret.png'
    Steganography.encrypt(file_input, file_output, my_secret, mod='R')

    file_to_be_decrypted = './img_edited/car_with_secret.png'
    Steganography.decrypt(file_to_be_decrypted)





# “我不知道您为什么要自己造轮子” -- StackOverflow
# 起因是我想学png的lsb隐写，然后我把png文件格式从头到尾学了一遍，最终我发现我需要提取IDAT数据块的RBG信息
# 但是我发现我不会，直到我知道Python自带库可以整，那我就算完全不知道png文件格式我也能写这个lsb隐写工具
# 这就和我想学Python反序列化但是却把PVM学了一遍的道理是一样的，没必要
# 明天继续
# 但是倘若不是png的lsb隐写，例如修改length数据等等就需要仔细了解png文件格式了
# PIL仅支持Python2，Pillow是Python3版的PIL
