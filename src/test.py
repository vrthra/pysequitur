from grammar import Grammar
g = Grammar()
s = ['x', 'a', 'b', 'c', 'd', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'g', 'h', 'g', 'h', 'g', 'h', 'i']
print(s)
g.train_string(s)
my_g = g.get_grammar()
for k in my_g:
    print(k)
    print("  ", my_g[k])
print()
x = g.flatten()
print(x)
