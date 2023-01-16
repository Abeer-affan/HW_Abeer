counter_freq=0
dic_words={}
def Word_counter(my_file):
    with open(my_file,"r+") as file:
        for line in file:
            split_lines= line.split()  # without this i have {every sentence: 1}
            for word in split_lines:
                counter_freq = dic_words.get(word, 0)
                dic_words[word] = counter_freq+ 1
    return dic_words

print(Word_counter( "My_id.txt"))
