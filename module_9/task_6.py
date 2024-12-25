import itertools

def all_variants(text):
    length = len(text)
    for a in range(length):
        for b in range(a, length):
            yield text[a:b + 1]

a = all_variants("abc")
for i in a:
    print(i)
