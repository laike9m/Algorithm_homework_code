# 实现Karatsuba算法,并设计了和传统算法的比较

import time

def Karatsuba(x, y):
    if x == '0' or y == '0':
        return 0
    else:
        x = x.lstrip('0')
        y = y.lstrip('0')
        len_x, len_y = len(x), len(y)
        if len_x == 1 or len_y == 1:
            return eval(x) * eval(y)
        else:
            shorter_len = len_x if len_x < len_y else len_y
            l = int(shorter_len/2)
            x1 = x[:-l]
            x0 = x[-l:]
            y1 = y[:-l]  # 保证x0和y0的长度相同
            y0 = y[-l:]
            x0, x1, y0, y1 = map(lambda x: x.lstrip('0') if x.count('0')!=len(x) else '0', [x0, x1, y0, y1])
            x1y1 = Karatsuba(x1, y1)
            x0y0 = Karatsuba(x0, y0)
            p = Karatsuba(str(eval(x1)+eval(x0)), str(eval(y0)+eval(y1)))
            return 10**(2*l) * x1y1 + x0y0 + 10**l * (p - x1y1 - x0y0)


def grade_school(x, y):
    
    result = 0
    len_y = len(y) - 1
    len_x = len(x) - 1
    
    for i in range(len_x + 1):
        for j in range(len_y + 1):
            result += eval(x[i]) * eval(y[j]) * 10**(len_y + len_x - i - j)
    
    return result



if __name__ == '__main__':
    while True:
        x = input('请输入x: ')
        y = input('请输入y: ')
        while len(y) != len(x) or not x.isnumeric() or not y.isnumeric():
            print('必须输入数字,位数必须相同,请重新输入！\n')
            x = input('请输入x: ')
            y = input('请输入y: ')
        
        start1 = time.clock()
        result_k = Karatsuba(x, y)
        end1 = time.clock()
        
        start2 = time.clock()
        correct_result = eval(x) * eval(y)
        end2 = time.clock()
        
        start2 = time.clock()
        result_g = grade_school(x, y)
        end2 = time.clock()
        
        print('\nK result: %s, time used: %s' % (result_k, end1 - start1))
        print('\nG result: %s, time used: %s' % (result_g, end2 - start2))
        print('\nC result: %s' % correct_result)
        if input('继续？(Y/N): ').lower() == 'n':
            break 