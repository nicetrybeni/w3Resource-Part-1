# text times how many u want 

def times_text(text, n):
    result = ""

    for i in range(n):
        result = result + text

    return result

print(times_text("joseph",3))