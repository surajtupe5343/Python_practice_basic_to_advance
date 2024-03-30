s1 = input("Enter three words: ").split()
s2 = list(s1)
def reverse_words(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

print(reverse_words(s2))