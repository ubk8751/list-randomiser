from random import shuffle
l = []
def main():
    make_list("list.txt")
    for _ in range(10):
        do_the_shuffle()
    l1, l2 = split()
    print("l len: " + str(len(l)))
    d = len(l1) + len(l2)
    print("split len: " + str(d))
    for l in [l1, l2]:
        for itm in l:
            print(itm)
        print("\n")


def make_list(file_name:str = "list.txt"):
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

def do_the_shuffle():
    shuffle(l)

def split():
    l1 = l[0:len(l)//2]
    l2 = l[len(l)//2:len(l)]
    return l1,l2

if __name__ == "__main__":
    main()