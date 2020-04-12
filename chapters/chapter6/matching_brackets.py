from stack import ArrayStack

def matching_brackets(expr):
    open_braces = '({['
    closed_braces = ')}]'

    S = ArrayStack(1024)
    for char in expr:
        if char in open_braces:
            S.push(char)
        elif char in closed_braces:
            if S.is_empty():
                return False
            if closed_braces.index(char) != open_braces.index(S.pop()):
                return False
    return S.is_empty()

if __name__ == "__main__":
    print(matching_brackets('()(()){([()])}'))

    print(matching_brackets('((()(()){([()])}))'))

    print(matching_brackets(')(()){([()])}'))

    print(matching_brackets('({[])}'))
            
