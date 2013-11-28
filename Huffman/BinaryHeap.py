# code to implement a Min Heap

class HeapElement:
    def __init__(self, char, freq):
        self.char = char
        self.value = freq
        

class MinHeap:
    
    def __init__(self, elem_list):
        self.A = elem_list  # A[0] is None, elems start from A[1]
        self.heap_size = 0
        self.length_A = len(self.A)


    def LEFT(i):
        return 2 * i 
    
    
    def RIGHT(i):
        return 2*i + 1
    
    
    def build_min_heap(self):
        self.heap_size = len(A)
        for i in range(1, int(length_A/2)+1)[::-1]:
            min_heapify(A, i)
    
    
    def min_heapify(self, i):
        l = LEFT(i)
        r = RIGHT(i)
        smallest = None
        
        if l <= self.heap_size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        
        if r <= self.heap_size and self.A[r] < self.A[i]:
            smallest = r
        
        if smallest != i:
            self.A[smallest], self.A[i] = self.A[i], self.A[smallest]
            self.min(self.A, smallest)
             
            
        







if __name__ == '__main__':
    print('  A  ')
    print(' / \ ')
    print('B   C')