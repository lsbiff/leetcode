class Solution:
    def sumZero(self, n: int) -> List[int]:
        edges = n // 2
        l = []
          
        for i in range(-1*(edges), 0):
            l.append(i)
            
        for i in range(1, edges + 1):
            l.append(i)
            
        
        if n % 2  == 1:
            l.append(0)
        
        return l
    
            