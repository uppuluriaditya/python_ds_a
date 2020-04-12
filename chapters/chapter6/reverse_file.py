from stack import ArrayStack

def reverse_file(filename):
    S = ArrayStack(1024)
    original = open(filename)
    for line in original:
        S.push(line.strip("\n"))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

if __name__ == "__main__":
    reverse_file('text_file.txt')