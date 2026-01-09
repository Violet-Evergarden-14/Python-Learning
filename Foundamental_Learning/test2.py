x = list(map(str, [i for i in range(1,27)]))
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

z = ['9', '12', '21']

translation = dict(zip(x, y))

m = []
for i in z:
    m.append(translation[i])


print(m)