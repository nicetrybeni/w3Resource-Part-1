# check if vowel or not 

def is_vowel(char):
    all_vowels = 'aeiou'

    return char in all_vowels

print(is_vowel('c'))  # Output: False (character 'c' is not a vowel)
print(is_vowel('e'))  # Output: True (character 'e' is a vowel)