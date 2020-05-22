'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word_counts = {}


def count_th(word):
    # TBC
    mem = word_counts.get(word) or [0, 0]
    count, pos = mem
    rest = word[pos:]
    if len(rest) < 2:
        # less than 2 characters
        return count
    a, b = rest[0], rest[1]
    if a == "t" and b == "h":
        count += 1
        word_counts[word] = [count, pos+2]
    else:
        word_counts[word] = [count, pos+1]
    return count_th(word)  # select everything after the first 2
