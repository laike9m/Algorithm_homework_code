# 实现Karatsuba算法,并设计了和传统算法的比较

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
            x1 = x[:int(len_x/2)]
            x0 = x[int(len_x/2):]
            y1 = y[:int(len_y/2)]
            y0 = y[int(len_y/2):]
            x0, x1, y0, y1 = map(lambda x: x.lstrip('0') if x!='0' else '0', [x0, x1, y0, y1])
            x1y1 = Karatsuba(x1, y1)
            x0y0 = Karatsuba(x0, y0)
            # 这一步出错,原因是相加之后位数不同了
            p = Karatsuba(str(eval(x1)+eval(x0)), str(eval(y0)+eval(y1)))
            cx1y1 = eval(x1) * eval(y1)
            cx0y0 = eval(x0) * eval(y0)
            cp = (eval(x1)+eval(x0))*(eval(y0)+eval(y1))
            if cx1y1 != x1y1:
                pass
            if cx0y0 != x0y0:
                pass
            if cp != p:
                pass
            return 10**len_x * x1y1 + x0y0 + 10**int(len_x/2) * (p - x1y1 - x0y0)



if __name__ == '__main__':
    x = input('请输入x: ')
    y = input('请输入y: ')
    while len(y) != len(x):
        y = input('位数必须相同,请重新输入y: ')
    
    result = Karatsuba(x, y)
    correct_result = eval(x) * eval(y)
    print('result: %s\n' % result)
    print('correct result: %s\n' % correct_result)