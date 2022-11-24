str_1 = 'In a hole in the ground there lived a hobbit.'
str_2 = 'hole in the ground'

def IsSubstring(Pattern, Source):
    if str_2 in str_1:
        return 'YES'
    else:
        return "NO"

print(IsSubstring(str_1, str_2))