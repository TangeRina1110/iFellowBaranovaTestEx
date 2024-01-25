def Double(st):
    dup = []
    for i in range(len(st)):
        if st[i] not in dup:
            for j in range(i+1, len(st)):
                if st[i] == st[j]:
                    dup.append(st[i])
                    break
    return (dup)

word = "abbcdddefffgggg"
print(Double(word))
