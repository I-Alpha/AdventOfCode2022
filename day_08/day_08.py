
lines = list(map(lambda x: x.strip("\n"), open("day_08/input.txt").readlines()))
  
class Cell():
    def __init__(self, i, j, height, grid=None):
        self.grid = grid
        self.grid_len = 0
        self.i = i
        self.j = j
        self.height=height
        self._visible_x = False
        self._visible_y = False
        self.neighbours =[]        
        self.score  = 1
     
    def is_visible(self):
        return self._visible_x or self._visible_y
    
    def is_visible_x(self):
        return self._visible_x
    
    def is_visible_y(self):
        return self._visible_y
    
    def set_visible_x(self, is_vis):
        if is_vis !=False:
            self._visible_x = is_vis

    def set_visible_y(self, is_vis):
        if is_vis ==False:
            return
        self._visible_y = is_vis
    
    def check_rows(self): 
        right = self.grid[self.i][self.j+1:]
        left = self.grid[self.i][self.j-1::-1]
        self._visible_x = all(self.height > cell.height for cell in right) or  all(self.height > cell.height for cell in left)
        
        sc=0    
        for i in right:
            sc +=1
            if i.height>=self.height:
                break
        sx=0
        for i in left:
            sx+=1
            if i.height>=self.height:
                break
        self.score *= sx * sc
                
    def check_cols(self):   
        cols_down=[]
        cols_up = []     
        
        for t in range(1,self.grid_len): 
            if self.i+ t > self.grid_len - 1:
                break
            cols_down += [self.grid[self.i+t][self.j]]
        
        t= 1
        while self.i - t >= 0: 
            cols_up+= [self.grid[self.i - t][self.j]]
            t+=1

        self._visible_y=all(item.height < self.height for item in cols_down) or all(item.height < self.height for item in cols_up)
        
        sc=0
        for i in cols_up:
            sc +=1    
            if i.height>=self.height:
                break
        
        sx=0
        for i in cols_down:
            sx+=1
            if i.height>=self.height:
                break
        self.score *= sx * sc
        
    def compute_visibility(self): 
        if self.is_visible():
            return True
        self.check_cols()
        self.check_rows()
    
def start_grid(lines):
    cell_list = {}
    grid_len = len(list(lines[0]))
    grid =[[] for _ in range(grid_len)] 
    
    def initialise_grid(i,j,height): 
        cell = Cell(i,j,height,grid)
        if cell.i == 0 or cell.i == grid_len-1:
            cell._visible_x = True
        if cell.j == 0 or  cell.j == grid_len-1:
            cell._visible_y = True
        grid[i].append(cell)
        cell_list[(i,j)] = cell  
    
    for i,row in enumerate(lines): 
        for j,height in enumerate(list(row)):
            initialise_grid(i,j,int(height))
            
    list(map(lambda x: x.compute_visibility(), cell_list.values( ))) 

    cell_count =0
    highest_score=0
    for i in cell_list.values():
        if i.is_visible():
            cell_count+=1
        if highest_score < i.score:
            highest_score = i.score
    return cell_count, highest_score

ans = start_grid(lines)

def part1():
    return ans[0]

def part2():
    return ans[1]

print(f"\n{part1()=} \
        \n{part2()=}\n")  # formatted print 