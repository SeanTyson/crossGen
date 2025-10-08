input_string = input("Enter a list of comma separated words \n")
print(input_string)
answer_words = input_string.split(',')

print(answer_words)

character_map = {}
i = 0 #word index
for word in answer_words:
    i += 1 
    j = 0 #character index for word
    for ch in word:
        j += 1 
        if ch.lower() not in character_map.keys():
            character_map[ch] = [(i,j)] 
        else:
            character_map[ch].append((i,j))

print(character_map)