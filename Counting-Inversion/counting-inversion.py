# 计算序列中逆序对的个数
from time import clock

def sort_and_count(A):
    if len(A) > 1:
        L = A[:int(len(A)/2)]
        R = A[int(len(A)/2):]
        count_l, L = sort_and_count(L)
        count_r, R = sort_and_count(R)
        C, A = merge_and_count(L, R)
        RC = count_l + count_r + C
        return (RC, A)
    else:
        return (0, A)
    
def merge_and_count(L, R):
    RC, i, j = 0, 0, 0
    A = []
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            A.append(R[j])
            j += 1
            RC += len(L) - i
        else:
            A.append(L[i])
            i += 1
    else:
        if i == len(L):
            A.extend(R[j:])
        else:
            A.extend(L[i:])
            
    return (RC, A)
            

if __name__ == '__main__':
    with open('Q5.txt') as f:
        A = [int(l) for l in f.readlines()]
    
    start = clock()
    inversions, _ = sort_and_count(A)
    end = clock()
    print('Inversions: %s\n' % inversions)
    print('time used: %s second' % str(end-start))