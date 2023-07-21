
def encode(strs):
    result = ""
    for s in strs:
        result += str(len(s)) + '#' + s

    return result


def decode(encoded):
    res, i = [], 0

    while i < len(encoded):
        j = i

        while encoded[j] != '#':
            j += 1

        length = int(encoded[i:j])

        res.append(encoded[j+1: j+1+length])
        i = j+1+length

    return res


enc = encode(["kaushik", "4#Test", "Kishore", "Dummy4#Dummy", "###Test"])

print(enc)
print(decode(enc))
