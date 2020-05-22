'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, c=0):
    # TBC
    if len(word) < 2:
        return c
    a, b = word[0], word[1]
    if a == "t" and b == "h":
        c += 1
        return count_th(word[2:], c)  # select everything after the first 2
    return count_th(word[1:], c)  # recurse
