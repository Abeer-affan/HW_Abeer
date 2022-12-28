#Abeer Affan

#ex1
my_dic={"name,Last_name" :"Abeer Affan", "age":"28", "phone numbe": "0548389626"}
print(my_dic)

#ex2
def replace_func(list):
    try :
        list[5]="@"
    except IndexError :
        return " your list is shorter than 5"
    else:
        return (list)
print(replace_func(["a","a",5,8,6,5,8,4]))
print(replace_func(["c",5,2])

#ex3
def replace_funassert(list):
    try:
        assert len(list)>=6 , "your list is shorter than 5 "
        list[5]= "@"
        return list
    except AssertionError as a msg:
        return msg
#ex4
def new_dic(dict,key,value):
    dict[key]= value
    return dict

#ex5
n=int( input("Write a number"))
sum_dic= { }
for x in range  (1,n+1):
    d[x]=x+3
print sum_dic

#ex6
def script_dic(*dictionaries ):
    last_dic = {}
    for d in dictionaries:
        last_dic.update(d)
    return last_dic
print(script_dic({1:10, 2:20} ,{ 3:30, 4:40},{5:50, 6:60}))



#ex7
def count_func(string1) :
    count_dic={ }
    for letter in string1:
        count_dic[letter]=count_dic.get(letter,0)+1
    return count_dic

#ex8
dic1={'a':2,'b':4,'c':3}
dict2={'a':3,'b':-2 ,'d':5}
dic3={}
key_dic1=list(dic1.keys())
key_dic2= list(dict2.keys())
for key in key_dic1:
    if key in key_dic2:
        dic3[key]= (dic1[key]+dict2[key])
        key_dic2.remove(key)
    else:
        dic3[key] =dic1[key]
for key in key_dic2:
    dic3[key]=key_dic2[key]
print(dic3)
print(key_dic2)


