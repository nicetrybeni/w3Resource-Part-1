# print the the first 2characters or 1 in a group

def substring_copy(text, n):
    flen = 6

    if flen > len(text):
        flen = len(text)

    substr = text[:flen]

    result = ""

    for i in range(n):
        result = result + substr

    return result 

print(substring_copy("JOSEPH",3))