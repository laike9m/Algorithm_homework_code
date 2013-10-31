# 实现序列比对的Needleman-Wunsch算法
import re

def alpha(xi, yj):
    if xi == yj:
        return 0
    else:
        return 1


def sequence_alignment(X, Y):
    m = len(seq1)
    n = len(seq2)
    OPT = [[None for j in range(n+1)] for i in range(m+1)] # m+1 rows, n+1 columns
    
    for i in range(m+1):
        OPT[i][0] = delta * i
    
    for j in range(n+1):
        OPT[0][j] = delta * j
        
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            case1 = alpha(X[i-1], Y[j-1]) + OPT[i-1][j-1]   # out X,Y starts from 0, not 1
            case2 = delta + OPT[i-1][j]
            case3 = delta + OPT[i][j-1]
            OPT[i][j] = min([case1, case2, case3])

    return OPT, m, n


def backtracking(OPT, seq1, seq2, i, j):
    
    if i == 0 and j == 0:
        return
    
    current = OPT[i][j] 
    
    if OPT[i-1][j] + delta == current:
        
        best_alignment.append((seq1[i-1], '-'))
        backtracking(OPT, seq1, seq2, i-1, j)
    
    elif OPT[i-1][j-1] + alpha(seq1[i-1], seq2[j-1]) == current:
        
        best_alignment.append((seq1[i-1], seq2[j-1]))
        backtracking(OPT, seq1, seq2, i-1, j-1)
    
    elif OPT[i][j-1] + delta == current:
        
        best_alignment.append(('-', seq2[j-1]))
        backtracking(OPT, seq1, seq2, i, j-1)
    
    else:
        print('backtracking error!')
        return
        

if __name__ == '__main__':
    
    global delta
    delta = 2
    
    with open('Gene1_Seq.txt') as gene1, open('Gene2_Seq.txt') as gene2:
        seq1 = gene1.read()
        seq2 = gene2.read()
        seq1 = re.sub('\n', '', seq1)
        seq2 = re.sub('\n', '', seq2)
    
    OPT, m, n = sequence_alignment(seq1, seq2)
    
    global best_alignment
    best_alignment = []
    backtracking(OPT, seq1, seq2, m, n)
    print(best_alignment)