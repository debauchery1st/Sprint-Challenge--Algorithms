'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word_counts = {}


def count_th(word):
    # TBC
    mem = word_counts.get(word) or [0, 0]  # check the memo for this word
    count, pos = mem  # 'th' count and current position
    rest = word[pos:]  # letters after this position
    if len(rest) < 2:  # if we have less than 2 letters,
        return count  # return the count of 'th'
    # if we have 2 or more letters
    a, b = rest[0], rest[1]  # take the first 2
    if a == "t" and b == "h":
        count += 1  # add one to the count if they match our target.
        word_counts[word] = [count, pos+2]  # advance 2 postions
    else:
        # if they don't match our target,
        word_counts[word] = [count, pos+1]  # advance 1 position
    return count_th(word)  # recurse
