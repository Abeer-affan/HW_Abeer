
def script_dic(*dictionaries ):
    last_dic = {}
    for d in dictionaries:
        last_dic.update(d)
    return last_dic
print(script_dic({1:10, 2:20} ,{ 3:30, 4:40},{5:50, 6:60}))


