# Job 1.4 :

def is_valid_word(word):
    return word.isalpha() and word.islower()

def rearrange_word(word):
    if not is_valid_word(word):
        return "Please enter a valid word !"

    l = list(word)
    
    for i in range(len(l) - 2, -1, -1):
        if l[i] < l[i + 1]:
            break
    else:
        return "No possible rearrangement"

    for j in range(len(l) - 1, i, -1):
        if l[j] > l[i]:
            break
    l[i], l[j] = l[j], l[i]

    l[i+1:] = reversed(l[i+1:])

    return ''.join(l)

usersword = input("Enter your word : ")
neword = rearrange_word(usersword)
print("your word after modification is", neword)


