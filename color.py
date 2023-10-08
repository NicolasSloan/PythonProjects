mySentence = "loves the color"

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst


for i in color_function('Nic'):
    print(i)
