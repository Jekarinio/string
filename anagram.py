def anagram(str1, str2):
    alist1 = list(str1)
    alist2 = list(str2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(str1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagram( 'abcde', 'edcba' ))