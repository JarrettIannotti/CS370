'''
It requires a string called 's' and returns a string
it uses the 3 integer variables i, j, k
It checks if the lock code is not ""(empty)
	if it is not empty then it begins a loop from i:=1 to len(s)
		increase lock_pos by 1
		check if lock_pos is greater than len(lock_code)
			if it is then set lock_pos to 1
		check if the ascii value of s[i] is between 0-31 or 128-255
			if it is then set s[i] equal to ' '(a space)
		set this_dat equal to the ascii value of s[i] and 15?????(this is checking if s[i] is 15 then set it to true??? otherwise set it to false??? tried this it does something else i get Error: Incompatible types: got "ShortInt" expected "Boolean" ask in class what this is. i think this is a bitwise operation but idk why it wont work for me
		set s[i] equal to the character at ascii value of ((ascii s[i] xor ascii lock_code[lock_pos] xor lock_dat) + 1) i think this is more bitwise stuff ask in class NOTE THE +1 is after the entire statement
		set lock_dat equal to this_dat
	return encoded s

Wrote this from like 12:30 to 4:24 :(
'''
import os
import random
import sys


class Constants:
    locktype = 3


lock_code = ""
lock_pos = -1
lock_dat = 0
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`']


# TODO: lock_pos starts at 1 in pascal (indices are at 1) but 0 here, idk, figure it out
def encode(stringToEncode: str) -> str:
    global lock_pos
    global lock_dat
    global lock_code
    global values
    # Convert the string to a list so that we can edit the values of the string. (python strings are immutable)
    stringToEncodeList = list(stringToEncode)
    print(f"stringToEncode: {stringToEncode}")
    if lock_code != '':
        # From 0 to the length of stringToEncodeList
        for i in range(0, len(stringToEncodeList)):
            lock_pos += 1
            if lock_pos >= len(lock_code):
                lock_pos = 0
            # Check to see if each character in the stringToEncode is a valid char in the ascii table if not make it " "
            print(f"stringToEncode[{i}] = {stringToEncode[i]}: Stingtoencodelist[i] = {ord(stringToEncodeList[i])}")

            if (ord(stringToEncodeList[i]) in range(0, 32)) or (ord(stringToEncodeList[i]) in range(128, 256)):
                # if (ord(stringToEncodeList[i] not in range(32,128)))
                stringToEncodeList[i] = " "
            '''
            current output for this_dat
            stringToEncode[0] = J: Stingtoencodelist[i] = 74
            ord(Stingtoencodelist[i]) & 15 = 10
                 64 32  16  8  4  2  1
            74 = 1  0   0   1  0  1  0
            15 = 0  0   0   1  1  1  1
                 0  0   0   1  0  1  0 = 10
            correct
            '''
            print(f"this_dat = ord(Stingtoencodelist[i]) & 15 = {ord(stringToEncodeList[i]) & 15}")
            this_dat = ord(stringToEncodeList[i]) & 15

            '''
            current output for ord(lock_code[lock_pos]) xor lock_dat
            stringToEncode[0] = J: Stingtoencodelist[i] = 74
            LOCK_DAT = 0 : LOCK_CODE[LOCK_POS] = Y : ord(LOCK_CODE[LOCK_POS]) = 89
                 64 32  16  8  4  2  1
            89 = 1  0   1   1  0  0  1
            0 =  0  0   0   0  0  0  0
                 1  0   1   1  0  0  1 = 89
                 
            current output for (ord(stringToEncodeList[i]) xor (ord(lock_code[lock_pos]) xor lock_dat)
                 64 32  16  8  4  2  1
            74 = 1  0   0   1  0  1  0
            89 = 1  0   1   1  0  0  1
                 0  0   1   0  0  1  1 = 19
                 19+1 = 20 
                 chr 20 = DC4
            '''
            print(f"LOCK_DAT = {lock_dat} : LOCK_CODE[LOCK_POS] = {lock_code[lock_pos]} : ord(LOCK_CODE[LOCK_POS]) = {ord(lock_code[lock_pos])}")
            stringToEncodeList[i] = chr((ord(stringToEncodeList[i]) ^ (ord(lock_code[lock_pos]) ^ lock_dat)) + 1)
            print(f"Value after the xors {stringToEncodeList[i]}")
            lock_dat = this_dat
            # print(f"stringToEncode: {stringToEncodeList[i]}")
    stringToEncode = str(''.join(stringToEncodeList))
    return stringToEncode


def lstr(s1, l) -> str:
    if len(s1) <= l:
        return s1
    else:
        return s1[0:l]


def prepare(s, s1: str) -> str:
    global lock_pos
    global lock_dat
    global lock_code
    global values
    # Remove comments
    if len(s1) == 0 or s1[0] == ";":
        pass
    else:
        k = 0
        for i in range(len(s1) - 1, 0, -1):
            if s1[i] == ';':
                k = i
        if k > 0:
            s1 = lstr(s1, k - 1)

    '''
    example to change excess white space to make it readable
    s2 = ''
    sawWs = False
    for c in s1:
        if !c.isSpace() and c != ',':
            s += c
            sawWs = False
        elif:
            if !sawWs
                s += ' '
                sawWs = True
    '''
    # Remove excess spaces
    s2 = ""
    for i in range(len(s1)):
        if s1[i] not in [' ', '\t', '\b', ',']:
            s2 = s2 + s1[i]
        elif s2 != "":
            s = s + s2 + " "
            s2 = ""

    if s2 != "":
        s = s + s2
    return s


def write_line(s, s1: str):
    global lock_pos
    global lock_dat
    global lock_code
    global values
    s = prepare(s, s1)
    s2 = ""
    # write line
    if len(s) > 0:
        s = encode(s)
    return s


def main():
    global lock_pos
    global lock_dat
    global lock_code
    global values
    lock_pos = -1
    lock_dat = 0
    # i dont think we need this but w/e
    # if len(sys.argv) < 1 or len(sys.argv) > 2:
    #     print("Usage: ATRLOCK <robot[.at2]> [locked[.atl]]")
    #     exit()

    # Read from this file and store the contents in a variable called contents
    with open("filename.txt", mode="r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)

    # Write to this file
    with open("filename2.txt", mode="w", encoding="utf-8") as file:

        # copy comment header
        print(";------------------------------------------------------------------------------", file=file)
        i = 0
        commentsComplete = False
        contentsList = contents.splitlines()
        print(contentsList)
        # restructure this so that it will show the proper line
        while not commentsComplete:
            # if line != "":
            # len(line[i]) != 0 and
            s = contentsList[i]
            s = s.strip()
            if len(s) != 0 and s[0] != ';':
                commentsComplete = True
                contentsList = contentsList[i+1:]
                break
            else:
                # Get the current line and remove leading and trailing whitespace
                print(s)
                print(f"S STRIPPED: {s}")
                if len(s) != 0 and s[0] == ";":
                    print(s, file=file)
                print(s)
                i = i + 1
                print(i)

        # lock header
        print(";------------------------------------------------------------------------------", file=file)
        # TODO: Add f"{nopathfilename} locked on date" here
        print("; Filename :) ", file=file)
        print(";------------------------------------------------------------------------------", file=file)
        # lock_code = ""
        # # TODO: Figure out of these randoms are inclusive? (do they include 21 and 32). how do they work?
        # k = random.randint(20, 41)
        # for i in range(1, k):
        #     lock_code = lock_code + chr(random.randint(65, 96))

        lock_code = "IYBSCYRPYOPTHE_IQBSX[EWMGB[J[\CKG"
        print(lock_code)
        print(f"#LOCK{Constants.locktype} {lock_code}", file=file)

        # TODO: This is nt working right, its returning blanks, above functions may be busted
        # decode lock-code
        lock_code_list = list(lock_code)
        print(lock_code_list)
        for i in range(0, len(lock_code_list)):
            print(lock_code[i])
            lock_code_list[i] = ord(lock_code_list[i]) - 65
            # print(lock_code_list[i])
        # This is not in the original convert lockcode to 0-31 values
        # print(f"LC LIST: {lock_code_list}")
        # newCode = ""
        # for i in range(0, len(lock_code_list)):
        #     newCode += str(values[lock_code_list[i]])
        # print(f"newLC: {newCode}")
        # lock_code = newCode
        print(lock_code)
        # lock_code1 = ''.join(str(lock_code_list))
        # print(lock_code1)
        print("Encoding *INSERT FILE 1 NAME HERE*...")

        # Encode robot
        s = s.strip()
        if len(s) > 0:
            sUpper = s.upper()
            write_line('', sUpper)
        for line in contentsList:
            s1 = line
            s = ""
            s1 = s1.upper()
            s1 = s1.strip()
            newLine = write_line(s, s1)

            print(newLine, file=file)
        print(f"Done. Used LOCK Format #{Constants.locktype}.", file=file)
        print(f"Only ATR2 v2.08 or later can decode.", file=file)
        print("Locked robot saved as '*FILE NAME GOES HERE*'", file=file)

    my_string = "this is a string"
    for word in my_string.split():
        print(word)


if __name__ == "__main__":
    main()
