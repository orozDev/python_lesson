lettes = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
    'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
    'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b',
    'n', 'm',
]

n = input()

if n in lettes:
    space = lettes.index(n)
    if space+1 >= len(lettes):
        print('q')
    else:
        print(lettes[space+1])
