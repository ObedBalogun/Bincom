def fibonacci():
    seq =[]
    #   iterate through a range of 50 values (0-49)
    for x in range(50):
        #   if list is empty extend the list with values at x and x+1 (0,1)
        if not seq:
            seq.extend((x,x+1))
            continue
        #   if list isn't empty append sum of current values of list[x] and list[x-1]
        else:
            result = seq[x] + seq[x-1]
            seq.append(result)
        #   return sum of all values in list
    return sum(seq)

print(fibonacci())