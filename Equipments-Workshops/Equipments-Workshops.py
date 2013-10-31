'''
BG company is ready to provide four same equipments to three workshops
W 1, W 2, W 3. The following table is the profit of each workshop under different allocation plans. Implement a program to decide how to allot the
equipments for maximum profit.

allot num  0  1  2  3  4
W1        38 41 48 60 66
W2        40 42 50 60 66
W3        48 64 68 78 78

solution:
OPT(i,n): i is phase(max workshop #),n is the amount of equipments
OPT(i,n) = max{Wi(k) + OPT(i-1,n-k)}  (0<=k<=n)
'''

def DP():
    
    # initialization
    
    OPT = [[None for i in range(5)] for j in range(4)]  # row 0 is not used
    
    W1 = [38, 41, 48, 60, 66]
    W2 = [40, 42, 50, 60, 66]
    W3 = [48, 64, 68, 78, 78]
    W = [None, W1, W2, W3]  
    
    for i in range(1,4):
        OPT[i][0] = sum([W[i][0] for i in range(1,i+1)])
    
    for n in range(0,5):
        OPT[1][n] = W[1][n]
    
    # DP
    
    for n in range(0,5):
        for i in range(2,4):    # i=1 has been calculated
            candidates = [ (W[i][k]+OPT[i-1][n-k]) for k in range(n+1)]
            OPT[i][n] = max(candidates)
            k = candidates.index(OPT[i][n])
    
    print(OPT[3][4])
    return W, OPT
    
    
def backtracking(W, OPT, i, n):
    
    if i == 1:
        result.append(n)
        return 
    
    candidates = [ (W[i][k]+OPT[i-1][n-k]) for k in range(n+1)]
    num_of_equipments_Wi = candidates.index(OPT[i][n])
    n = n - num_of_equipments_Wi  
    result.append(num_of_equipments_Wi)
    
    backtracking(W, OPT, i-1, n)
    
                
        
def prove_correctness():
    'brute force algo to verify the correctness of DP algo'
    
    W1 = [38, 41, 48, 60, 66]
    W2 = [40, 42, 50, 60, 66]
    W3 = [48, 64, 68, 78, 78]
    W = [None, W1, W2, W3] 
    max_sum = 0
    
    for i in range(5):
        for j in range(5-i):
            for k in range(5-i-j):
                sum = W[1][i] + W[2][j] + W[3][k]
                max_sum = sum if sum > max_sum else max_sum
    
    print(max_sum)
    
    

if __name__ == '__main__':
    global result    # store final results
    result = []
    W, OPT = DP()
    backtracking(W, OPT, 3, 4)
    print("W1: %s, W2: %s, W3: %s" % tuple(result[::-1]))
    
    prove_correctness()
    