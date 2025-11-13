han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    print('Line:', line)
    if line == '':
        continue
    wds = line.split()
    print('Words:',wds)
    # if len(wds) < 1: # guardian pattern
        # continue
    if wds[0] != 'From':
        continue
    print(wds[2])
