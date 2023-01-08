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
print(replace_func(["c",5,2]))

#ex3
def assert1_fun(list1):
    try:
        assert len(list1)>= 6, "your list is shorter than 5 "
        list1[5]= "@"
        return list1
    except AssertionError as msg:
        return msg
assert1_fun([1,2,3,4,5,6,8])

#ex4
def new_dic(dict,key,value):
    dict[key]= value
    return dict
print(new_dic({1:2,2:3,4:5},8,9))

#ex5
n=int(input("Write a number"))
sum_dic= {}
for x in range (1,n+1):
    sum_dic[x]=x+3
print (sum_dic)

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
print(count_func("HANNA"))

#ex8
dic1={'a':2,'b':4,'c':3}
dict2={'a':3,'b':-2,'d':5}
dic3={}
key_dic1=set(dic1.keys())
key_dic2= set(dict2.keys())
allkeys=key_dic1|key_dic2
print(allkeys)
for key in allkeys:
    if key in key_dic2 and key in key_dic1:
        dic3[key]= dic1[key]+dict2[key]
    elif key in key_dic1:
        dic3[key] =dic1[key]
    else:
        dic3[key]=dict2[key]

print(dic3)
