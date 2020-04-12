from stack import ArrayStack

def is_matched_html(raw: str):
    S = ArrayStack(1024)

    j = raw.find('<')

    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', j+1)
    return S.is_empty()

if __name__ == "__main__":
    html_string = "<html><head>Hello</head></html>"
    print(is_matched_html(html_string))
