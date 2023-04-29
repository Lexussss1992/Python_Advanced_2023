sentence = input()
lst = []
[lst.append(letter) for letter in sentence]
tpl = tuple(lst)
dict = {}

for i in tpl:
    dict[i] = tpl.count(i)

for letter, count in sorted(dict.items()):
    print(f'{letter}: {count} time/s')