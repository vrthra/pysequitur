from grammar import Grammar
g = Grammar()
g.train_string(['x', 'a', 'b', 'c', 'd', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'g', 'h', 'i'])
print(g.print_grammar())
