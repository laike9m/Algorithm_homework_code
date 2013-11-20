'''
实现对纯英文文本文件的huffman编解码,会将编码方式输出到文件
几个部分: 字符频率统计, 编码器, 二进制文件写入, 解码器
'''

class Huffman():
    
    def __init__(self):
        self.file_list = None
        self.char_frequency = {}    # 每个文件对应该字典中一个k-v, v是{char:fre}的字典
    
    def read_files(self, *filename):
        self.file_list = filename
    
    
    def frenquency_count(self):
        for file in self.file_list:
            charset = set(open(file).read())
            print(charset)
        
    
    def huffman_encode(self):
        for file in self.file_list:
            pass
        
        
    def write_to_binary(self):
        for file in self.file_list:
            pass
    
    
    def huffman_decode(self):
        'read from binary files and restore them to original txt files'
        pass


if __name__ == '__main__':
    h = Huffman()
    h.read_files('Aesop_Fables.txt', 'graph.txt')
    h.frenquency_count()