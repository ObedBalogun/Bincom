def fibonacci():
    seq_length = int(input('Please input the length of the fibonacci sequence you want'))
    seq = []
    for x in range(seq_length-1):
        if not seq:
            seq.extend((x, x+1))
            continue
        else:
            result = seq[x]+seq[x-1]
            seq.append(result)
    return seq


print(fibonacci())