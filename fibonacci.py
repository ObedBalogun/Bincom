def fibonacci(n):
    seq = []
    for x in range(n-1):
        if not seq:
            seq.extend((x, x+1))
            continue
        else:
            result = seq[x]+seq[x-1]
            seq.append(result)
    return seq


print(fibonacci(10))