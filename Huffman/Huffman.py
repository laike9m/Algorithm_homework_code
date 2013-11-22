'''
实现对纯英文文本文件的huffman编解码,会将编码方式输出到文件
几个部分: 字符频率统计, 编码器, 二进制文件写入, 解码器

this is the huffman-tree version

INPUT: 
    serveral txt files(name), under the same directory
        
OUTPUT: 
    filename_restore.txt(file restored from binary), 
    filename.b(compressed binary file)
    
'''

import pickle
import bitstring
from os.path import splitext
from collections import defaultdict

class Huffman():
    
    def __init__(self):
        self.file_list = None
        self.char_frequency = {}    # each file is a k-v, v is {char:freq} dict
        self.sorted_frequency = {}  # k-v, k is filename, v is sorted list of (char,freq) tuples
        self.text_as_bits = defaultdict(str)  # {filename:'10100010101010010100101', ...}
    
    def read_files(self, *filename):
        self.file_list = filename
    
    
    def frenquency_count(self):
        for file in self.file_list:
            with open(file) as f:
                content = f.read()
                charset = set(content)
                self.char_frequency[file] = {}
                for char in charset:
                    self.char_frequency[file][char] = content.count(char)
            self.sorted_frequency[file] = sorted(self.char_frequency[file].items(), key=lambda k:k[1])
        
    
    def huffman_encode(self):
        
        for file in self.file_list:
            char_code_dict = {k:'' for k in self.char_frequency[file].keys()} # store huffmancode of chars
            sorted_freq = self.sorted_frequency[file][:]
           
            while len(sorted_freq) > 1:
                # generate huffman code in reverse order
                for char in sorted_freq[0][0]: # [0] is char, [1] is freq
                    char_code_dict[char] += '0' 
                    
                for char in sorted_freq[1][0]:
                    char_code_dict[char] += '1'
                    
                new_tuple = (sorted_freq[0][0] + sorted_freq[1][0], sorted_freq[0][1] + sorted_freq[1][1])
                del sorted_freq[0:2]
                sorted_freq.append(new_tuple)
                sorted_freq = sorted(sorted_freq, key=lambda k:k[1])
            
            for k, v in char_code_dict.items(): # reverse
                char_code_dict[k] = v[::-1] # string doesn't have reverse method
                
            print(str(sorted(char_code_dict.items(), key=lambda k:len(k[1]) )))
            pickle.dump(char_code_dict, open(file+'.p', 'wb'))
        
                    
    def write_to_binary(self):
        'write to binary files with bitstring library'
        for file in self.file_list:
            char_code_dict = pickle.load(open(file+'.p', 'rb'))
            with open(file, 'rt') as f, open(file+'.b', 'wb') as bfile:
                content = f.read()
                text_as_bits = ''    
                for char in content:
                    text_as_bits += char_code_dict[char]    
                    # very slow if directly write ti self.text_as_bits[file]
                self.text_as_bits[file] = text_as_bits
                bits = bitstring.BitArray(bin=self.text_as_bits[file])
                bfile.write(bits.tobytes())
    
    
    def compare_two_onezero_files(self):
        
        for file in self.file_list:
            bits = bitstring.BitArray(filename=file+'.b')
            
            print("bits.bin length: %s\nself.text_as_bits[file] length: %s\n"\
                   % (len(bits.bin), len(self.text_as_bits[file])))
                 
            with open('compare_' + file, 'wt') as f:
                for c1, c2 in zip(bits.bin, self.text_as_bits[file]):
                    f.write('%s\t%s\n' % (c1, c2))
    
    
    def huffman_decode(self):
        'read from binary files and restore them to original txt files'
        for file in self.file_list:
            bits = bitstring.BitArray(filename=file+'.b')
            text_as_bits = bits.bin
            char_code_dict = pickle.load(open(file+'.p', 'rb'))
            huffman_code_set = set(char_code_dict.values())
            code_char_dict = {v:k for k ,v in char_code_dict.items()}
            restore_content = ''
            
            i = 1
            length = 10000
            while i:
                while text_as_bits[:i] not in huffman_code_set: # 前缀码
                    i += 1
                    if i >= length:
                        i = 0
                        break  # extra bits at the end should be ignored
                else:
                    restore_content += code_char_dict[text_as_bits[:i]]
                    text_as_bits = text_as_bits[i:] 
                    i = 1
                    length = len(text_as_bits)
                    print(length)
                
            with open(splitext(file)[0]+'_restore.txt', 'wt') as f_restore:
                f_restore.write(restore_content)
                


def verify_huffman_encode():
    #char_freq = {'A':24, 'B':12, 'C':10, 'D':8, 'E':8}
    
    # data come from http://nerdaholyc.com/a-simple-example-of-huffman-coding-on-a-string/
    char_freq = {'b': 3, 'e': 4, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1}
    
    sorted_freq = sorted(char_freq.items(), key=lambda k:k[1])
    char_code_dict = {k:'' for k in char_freq.keys()}
   
    while len(sorted_freq) > 1:
        
        for char in sorted_freq[0][0]: # [0] is char, [1] is freq
            char_code_dict[char] += '0' 
            
        for char in sorted_freq[1][0]:
            char_code_dict[char] += '1'
                
        new_tuple = (sorted_freq[0][0] + sorted_freq[1][0], sorted_freq[0][1] + sorted_freq[1][1])
        del sorted_freq[0:2]
        sorted_freq.append(new_tuple)
        sorted_freq = sorted(sorted_freq, key=lambda k:k[1])
        
    for k, v in char_code_dict.items(): # reverse
        char_code_dict[k] = v[::-1]
    
    print(str(sorted(char_code_dict.items(), key=lambda k:len(k[1]) )))


if __name__ == '__main__':
    #verify_huffman_encode()
    
    h = Huffman()
    mode = 1    # 1=whole process, 0=use the already-generated binary file
    
    if mode:
        h.read_files('Aesop_Fables.txt', 'graph.txt')
        h.frenquency_count()
        h.huffman_encode()
        h.write_to_binary()
        h.compare_two_onezero_files()
        h.huffman_decode()
    else:
        h.read_files('Aesop_Fables.txt', 'graph.txt')
        h.huffman_decode()
    
