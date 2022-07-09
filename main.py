import Steganography

if __name__ == '__main__':
    print('I put my story here, interested?')


# “我不知道您为什么要自己造轮子” -- StackOverflow
# 起因是我想学png的lsb隐写，然后我把png文件格式从头到尾学了一遍，最终我发现我需要提取IDAT数据块的RBG信息
# 但是我发现我不会，直到我知道Python自带库可以整，那我就算完全不知道png文件格式我也能写这个lsb隐写工具
# 这就和我想学Python反序列化但是却把PVM学了一遍的道理是一样的，没必要
# 但是倘若不是png的lsb隐写，例如修改length数据等等就需要仔细了解png文件格式了
# PIL仅支持Python2，Pillow是Python3版的PIL
