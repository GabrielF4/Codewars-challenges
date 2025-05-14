def wave(people):

    return_arr = []

    for i in range(len(people)):
        if ' ' == people[i]:
            continue
        temp_people = list(people)
        temp_people[i] = temp_people[i].upper()
        return_arr.append("".join(temp_people))
    
    return return_arr

print(wave("hello"))
    