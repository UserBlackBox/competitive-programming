# https://dmoj.ca/problem/dwite07c3p2
# https://dmoj.ca/submission/2194172

for n in range(5):
    line = input()
    text = ""
    literal = ""
    skip = False
    for i in range(len(line)):
        if skip:
            skip = False
            continue

        if line[i] == '"':
            if literal == "":
                literal = "\""
                continue
            elif literal == "\"":
                literal = ""
                text += " "
        elif line[i] == "'":
            if literal == "":
                literal = "'"
                continue
            elif literal == "'":
                literal = ""
                text += " "
        elif line[i] == '/':
            try:
                if line[i-1] == '*' and literal == "/*":
                    literal = ""
                    text = text[:-1]
                    text += " "
            except IndexError:
                pass
            try:
                if line[i+1] == '/' and literal == "":
                    literal = "//"
                    skip = True
                    continue
            except:
                pass
            try:
                if line[i+1] == '*' and literal == "":
                    literal = "/*"
                    skip = True
                    continue
            except IndexError:
                pass
        
        if literal != "":
            text += line[i]
    text = text.strip()
    print(text)