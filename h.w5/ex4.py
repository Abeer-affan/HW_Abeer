def longest_word(_file):
    with open(_file,"r") as file:
        words=file.read().split()
        long_word=len(max(words, key=len))
        for word in words:
            if len(word)==long_word:
             print(word)
    return (word)
longest_word("My_id.txt")