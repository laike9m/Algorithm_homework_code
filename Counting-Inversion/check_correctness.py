# 用暴力法计算结果,检验其他方法的正确性
# 包含自己的暴力算法(结果不一样)和从
# http://codereview.stackexchange.com/questions/12922/inversion-count-using-merge-sort
# 复制下来的算法。别人的算法和我的分治法结果相同

from time import clock

def brute_force(A):
    inversions = 0
    for i in A:
        for j in A[i+1:]:
            if i > j:
                inversions += 1
    return inversions
    

def merge_sort(li):
    if len(li) < 2: return li 
    m = int(len(li)/2) 
    return merge(merge_sort(li[:m]), merge_sort(li[m:])) 


def merge(l, r):
    global count
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result



if __name__ == '__main__':
    with open('Q5.txt') as f:
        A = [int(l) for l in f.readlines()]
    
    global count 
    count = 0
    start = clock()
    #inversions = brute_force(A)
    merge_sort(A)
    end = clock()
    print('Inversions: %s\n' % count)
    print('time used: %s second' % str(end-start))