# write the function is_anagram
def is_anagram(test, original):
    grp1 = list(test.lower())
    grp2 = list(original.lower())
    grp1.sort()
    grp2.sort()
    g2_o = len(grp2)

    for x in grp1:
        y = grp2[0]
        if x == y:
            grp2.reverse()
            grp2.pop()
            grp2.reverse()

    if len(grp1) == g2_o and grp2 == []:
        print('T')
        return True
    else:
        print('F')
        return False

is_anagram("Creative","Reactive")
