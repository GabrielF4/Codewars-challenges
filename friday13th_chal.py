def kill_count(counselors, jason):
    return [person[0] for person in counselors if person[1] < jason]

counselors = [["Tiffany", 4],["Jack", 6],["Megan", 7],["Tyler", 3]]

print(kill_count(counselors, 7))