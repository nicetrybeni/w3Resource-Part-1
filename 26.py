# print a character based on number

def word_multiplier(items):
    for n in items:
        output = ""
        times = n
        
        while times > 0:
            output += "*"
            times = times - 1

        print(output)

word_multiplier([2])

