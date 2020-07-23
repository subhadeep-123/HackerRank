import itertools
for key, group in itertools.groupby(input()):
    print((len(list(group)), int(key)), end=' ')
