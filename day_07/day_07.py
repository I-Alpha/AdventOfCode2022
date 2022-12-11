lines = list(map(lambda x: x.strip("\n"), open("day_07/input.txt").readlines())) 

class Item():
    def __init__(self, name, parent, size = 0, ftype = None) -> None:
        self.size = size 
        self.name = name 
        self.parent = parent 
        if ftype == "directory":
            self.itemList = {} 
        self.itemType = ftype

    def get_size(self):
        if self.itemType == "directory":
            self.size = sum(  map(lambda x: x.get_size(), self.itemList.values())) 
        return self.size
    
    def get_dir_size(self, limit = False): 
        if self.itemType == "directory" :
            if limit:
                if self.size <= limit:
                    return self.size + sum(map(lambda x: x.get_dir_size(limit), self.itemList.values()))   
                else: 
                   return sum(map(lambda x: x.get_dir_size(limit), self.itemList.values()))   
            else:
                return self.size + sum(map(lambda x: x.get_dir_size(), self.itemList.values()))   
        else:
            return 0
    
    def get_dir_by_size(self, limit, dir_list =[] ):
        if self.itemType == "directory" :
            if self.size >= limit:
                dir_list.append(self)
            for i in self.itemList.values():
                i.get_dir_by_size(limit,dir_list)
        
            
class DirectoryTree():
    def __init__(self, lines) -> None:
        self.root = None
        self.total_disk_space=0
        self._initialize_(lines)
        
    def _initialize_(self, lines):
        current_dir = Item("/", 0, 0, "directory") 
        self.root = current_dir
        for line in lines[1:]:
            if "$ cd " in line:
                current_dir = self.handle_change_directory(current_dir, line)  
            elif "$ ls" not in line:
                self.handle_view_file(current_dir, line)
        self.total_size=self._update_dir_sizes() 
        self.total_disk_space =70000000 - self.total_size
        
    def handle_view_file(self, current_dir, line):
        if "dir " in line: 
            dir_name = line[4:]
            if dir_name not in current_dir.itemList:
                direc = Item(dir_name, current_dir,  0, "directory")
                current_dir.itemList[dir_name]=direc
        else:
            [file_size,file_name] = line.split(" ")
            if file_name not in  current_dir.itemList:
                f_item = Item(file_name, current_dir, int(file_size),"file")
                current_dir.itemList[file_name]=f_item

    def handle_change_directory(self, current_dir, line):
        if " .." in line:
            if current_dir.parent != None:
               current_dir = current_dir.parent
        else:
            dir_name = line[5:]
            current_dir = current_dir.itemList[dir_name]
        return current_dir
        
    def _update_dir_sizes(self):
        return self.root.get_size()
     
    def get_sum_of_dirs_with_limit(self, limit = 9999999999):
        return self.root.get_dir_size(limit)
    
    def get_dirs_with_limit(self, limit = 9999999999):
        dirList = []
        self.root.get_dir_by_size(limit,dirList)
        return dirList

def part1(lines):
    dir_tree = DirectoryTree(lines)
    return dir_tree.get_sum_of_dirs_with_limit(100000)
   
def part2(lines):
    dir_tree = DirectoryTree(lines)
    ans =dir_tree.get_dirs_with_limit(30000000-dir_tree.total_disk_space) 
    return ans[-1].size

print(f"\n{part1(lines)=} \
        \n{part2(lines)=}\n")  # formatted print 