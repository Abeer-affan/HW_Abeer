n= int(input("please input a num : "))
def read_n_line(_file):
    with open(_file,"r+") as file:
        file.seek(0)
        line_list = file.readlines()
        print(line_list)
        for text in line_list[0:n]:
            print (text)
read_n_line("My_id.txt")

