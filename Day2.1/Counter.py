class Counter:
    def __init__(self, data):
        self.data = data
        self.bad_level = -1

    def safe(self):
        safe_count = 0
   
        for level in self.data:
            if self.isIncreasing(level) or self.isDecreasing(level):
                if self.adjacency(level):
                    print(level)
                    safe_count+=1
                else:
                    if self.remove(level):
                        print(level)
                        safe_count+=1
            else:
                if self.remove(level):
                    print(level)
                    safe_count+=1
        return safe_count
    
    def remove(self, lst):
        copy = list(lst)
        del copy[self.bad_level]
        if self.isDecreasing(copy) or self.isIncreasing(copy):
            if self.adjacency(copy):
                #print(copy)
                return True
            else:
                return False
        else:
            return False
        
    def adjacency(self, lst):
        valid_difference = [1,2,3]
        for i in range(1, len(lst)):
            if abs(lst[i] - lst[i-1]) > 3:
                self.bad_level = i-1
                return False
        return True

    def isIncreasing(self, lst):
        stack = []
        for i in lst:
            if stack and i <= stack[-1]:
                self.bad_level = lst.index(i)
                # print("NOT INCREASING")
                # print(lst)
                return False
            
            stack.append(i)
        return True
    
    def isDecreasing(self, lst):
        stack = []
        for i in lst:
            if stack and i >= stack[-1]:
                self.bad_level = lst.index(i)
                return False
            stack.append(i)
        return True