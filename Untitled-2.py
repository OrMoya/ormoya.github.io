#def decode(message_file):

with open('coding_qual_input.txt') as f:
    lines = [line for line in f]
lines.sort(key=lambda line: int(line.split()[0]))


#Beginning of message is always 1, there the 0 index
decodedMessage = lines[0].split()[1]

pyramidLength = len(lines)
height = 0
for i in range(1, pyramidLength, height + 1):
    print(i)
    decodedMessage = decodedMessage + " " + (lines[i].split()[1])
    height += 1

print(decodedMessage)