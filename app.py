import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))
def trans(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),3))>0:
        c=input("Did you mean %s ?" % (get_close_matches(w,data.keys())[0]))

        if c == 'y':
            return data[get_close_matches(w,data.keys())[0]]

        else:
            return "Sorry word cannot be found!"


    else:
        return "Sorry meaning cannot be found!"




ch='y'
print("\tWelcome to dicionary ")
while ch=='y':
    w=input("Ent the word of which you want to find meaning of:")
    m=trans(w)
    if type(m)==list:
        for i in m:
            print(i)
    else:
        print(m)


    ch=input("Do you want to contiue:")
