from webbrowser import open_new_tab

def open_file(file_name:str = "list.txt", l:list = []):
    # Using readlines()
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        if "List length" in line or line == "\n":
            continue
        elif "\n" in line:
            line = line[0:-1]
        count += 1
        if line not in (l):
            l.append(line)
    return l

def open_urls(l:list=[]):
    if l == []:
        return "nothing to do here"
    for itm in l:
        open_new_tab(itm)
    return "Done"

def main(l:list = []):
    l = open_file("test.txt", l)
    print(open_urls(l))

if __name__ == "__main__":
    l = []
    main(l)