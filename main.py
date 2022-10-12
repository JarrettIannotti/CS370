# import numpy as np
#
# test =np.zeros(shape=(3, 3))
# test[0, 1] = 5
# print(test)
import dis

if ord("A") in range(0, 31) or ord("A") in range(65, 255):
    print("YO")

'''
8 4 2 1
0 0 1 0
0 0 1 1
'''
print(2 & 3)

'''
8 4 2 1
0 0 1 0
0 0 1 1
'''
print(2 ^ 3)

values = []

for i in range(0, 32):
    values.append(chr(i + 65))
print(values)




def parse(string, i, previousDict):
    print(f"STRING: {string}")
    if i == len(string):
        if string in previousDict[string]:
            previousDict[string](string[i], string[i-1])
            return

    elif string in previousDict[string]:
        i += 1
        previousDict = previousDict[string][string[i]]
        print(previousDict)
        parse(string[i], i, previousDict)


def newParseIdea(string):

    # our ex string is ["mov", "ax", "10"]
    # if the string in the first index is in commands it will go into here
    if string[0] in commands:
        # if the string in the first index is "mov" we will move forward assuming the syntax is correct for mov
        if string[0] == "mov":
            # the first string if the syntax for mov is correct will be a register. So we check if it is a register
            if string[1] in registers:
                # the 2nd item in the list should be a number so check if it is a number
                if string[2].isnumeric():
                    # if it is a number we will call commads["mov"](value, register) which will call our mov func
                    commands[string[0]](string[2], string[1])

        # this is just a 2nd example we would have all the commands in here listed as ifs like this
        if string[0] == "add":
            if string[1] in registers:
                pass

ax = 0
bx = 0
cx = 0
dx = 0
def mov(value, register):
    # use the global variables for ax, bx, cx, and dx
    global ax, bx, cx, dx
    # if the register is ax put value into ax
    if register == "ax":
        ax = value
        print(f"WE MADE IT TO {register}, its value is: {ax}")



myDict = {
    "test":
        {"anothaone":
             {"andonemore":
                  "yo"}
         },
    "test2": "Just checking",
    "mov": mov,
}


# any command such as mov or add go here
commands = {
    "mov": mov,
}


# these are our "fake" registers
registers = {
    "ax": ax,
    "bx": bx,
    "cx": cx,
    "dx": dx,
}

# if "andonemore" in myDict["test"]["anothaone"]:
#     print(myDict["test"]["anothaone"])

# this is the string we will pass into the function to parse (it is just one example line)
string = "mov ax 10"
# split the string into individual words so that we can figure out each word individually
# .split also removes white spaces
stringList = string.split()

#print(parse(stringList, 0, myDict))

# Pass the stringList to new parse idea
newParseIdea(stringList)



'''
Articles on making your own simple compiler in python
https://medium.com/@pasi_pyrro/how-to-write-your-own-c-compiler-from-scratch-with-python-90ab84ffe071
https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df

Example C parser made in python
https://github.com/Hyper5phere/simple-c-compiler/blob/master/modules/cparser.py 

Youtube playlist on making your own programming lang with python
https://www.youtube.com/watch?v=Eythq9848Fg&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD
'''
