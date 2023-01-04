import re

# part1
def file_fun(file_text):
    with open(file_text, "w+") as file:
        file.write("Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.\n")
        file.write("J.U.U.U Kmltin\n")
        file.write("mmps iks nmk eio; ---> hkmu\n")
        file.seek(0)  # מחזירים לקריאה הקובץ מההתחלה
        dic_file = {}
        for word in file:
            for char in word:
                if char.isalpha():  # Is the char latter if yes then count+1
                    char = char.lower()  # מתייחס לאותיות גדולות וקטנות אותו דבר
                    count = dic_file.get(char, 0)
                    count += 1
                    dic_file[char] = count
                    # chars=dic_file.keys()
    dic_file = (sorted(dic_file.items(), key=lambda item: item[1], reverse=True))
    print(type(dic_file))
    return (dic_file[0:4])


commonLetterDic = (file_fun("file_text.txt"))
print(commonLetterDic)
most_common = ['e', 't', 'o', 'r']

dic3 = {}
for i in range(0, 4):
    dic3[commonLetterDic[i][0]] = most_common[i]
    dic3[most_common[i]] = commonLetterDic[i][0]
print(dic3)

commonLetterList = list(dict(commonLetterDic).keys())

with open("C:/Users/DELL/PycharmProjects/hw_samana/project1/file_text.txt", "r") as file:
    data = file.read()


# part2
def correct_text(str1):
    correct_txt = ""
    for charcter in str1:
        charcter = charcter.lower()  # list_dic=list(dic3.keys)
        if charcter in most_common or charcter in commonLetterList:
            charcter = dic3[charcter]
        correct_txt = correct_txt + charcter
    return correct_txt


print(correct_text(data))


# part3

def file_path(path_file):
    with open(path_file + "/results.txt", "w+") as file:
        # file.write(data+"\n")
        # file.write("The encryption for the above text is:\n\n")
        file.write(correct_text(data))


file_path("C:/Users/DELL/PycharmProjects/hw_samana/project1/")


# part4
def result_func(path_file):
    with open("results.txt", "r") as file:
        max_data2 = " "
        regex = re.compile('[^a-zA-Z]')
        data2 = regex.sub(' ', correct_text(data)).split()
        for word in data2:
            if len(word) > len(max_data2):
                max_data2 = word

    return max_data2


print(result_func("C:/Users/DELL/PycharmProjects/hw_samana/project1/results.txt"))


def num_lines(path_file):
    with open("results.txt", "r") as file:
        NumOfLine = file.readlines()
    return len(NumOfLine)


print(num_lines("C:/Users/DELL/PycharmProjects/hw_samana/project1/results.txt"))

with open("results.txt", "a") as file:
    file.write((result_func("C:/Users/DELL/PycharmProjects/hw_samana/project1/results.txt") + " ") *
               num_lines("C:/Users/DELL/PycharmProjects/hw_samana/project1/results.txt"))
