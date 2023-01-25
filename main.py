from random import shuffle
from math import ceil

def main(l:list = []):
    l1, l2, l3, l4, l5 = ([] for i in range(5))
    l = make_list("OG_list.txt", [])
    for _ in range(10):
        do_the_shuffle(l)
    
    s = split(5, [l1, l2, l3, l4, l5], l)
    print("list len: " + str(len(l)))
    d = 0
    for lst in s:
        d += len(lst)
    print("split len: " + str(d))
    print(write_file("split_list.txt", "divided_list.txt", s))
    


def make_list(file_name:str = "list.txt", l:list = []):
# Using readlines()
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        if "Notes:" in line or line == "\n":
            break
        elif "\n" in line:
            line = line[0:-1]
        count += 1
        if line not in (l):
            l.append(line)
    return l

def do_the_shuffle(l:list = []):
    shuffle(l)

def split(n:int = 2, lists:list=[], l:list = []):
    if lists == []:
        return lists
    step_size = len(l)//n
    s = 0
    e = step_size
    for i in range(len(lists)):
        s = i*step_size
        e = i*step_size + step_size
        lists[i] = l[s:e]
    if e < len(l):
        for i in range(len(lists)):
            if e >= len(l):
                break
            lists[i].append(l[e])
            e+=1
    return lists

def write_file(split_file:str = "split_list.txt", divided_file:str = "divided_list.txt", lsts:list = []):
    if lsts == []:
        return "Bruh, I need something to export!"
    tot_len = 0
    f = open(split_file, "w")
    for l in lsts:
        for itm in l:
            f.write(itm + "\n")
        EOL = "List length: " + str(len(l)) + "\n\n"
        tot_len += len(l)
        f.write(EOL)
    
    f.write("Total number of papapers: " + str(tot_len))
    return "File was created properly!? :D"
    

if __name__ == "__main__":
    l = []
    main(l)