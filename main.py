import os
import random
import sys
from pathlib import Path
from datetime import date

class Constants:
    locktype = 3


lock_code = ""
lock_pos = -1
lock_dat = 0
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`']


def encode(stringToEncode: str) -> str:
    global lock_pos
    global lock_dat
    global lock_code
    global values
    # Convert the string to a list so that we can edit the values of the string. (python strings are immutable)
    stringToEncodeList = list(stringToEncode)
    #print(f"stringToEncode: {stringToEncode}")
    if lock_code != '':
        # From 0 to the length of stringToEncodeList
        for i in range(0, len(stringToEncodeList)):
            #print(f"LOCK_CODE: {lock_code[lock_pos]}")
            lock_pos += 1


            if lock_pos >= len(lock_code):
                lock_pos = 0

            #print(lock_pos)
            #print(f"'Encoding: {stringToEncodeList[i]}' Lockchar: {lock_code[lock_pos]}")
            # Check to see if each character in the stringToEncode is a valid char in the ascii table if not make it " "
            #print(f"stringToEncode[{i}] = {stringToEncode[i]}: Stingtoencodelist[i] = {ord(stringToEncodeList[i])}")

            if (ord(stringToEncodeList[i]) in range(0, 32)) or (ord(stringToEncodeList[i]) in range(128, 256)):
            #if stringToEncodeList[i] not in range(32, 128):
                stringToEncodeList[i] = " "
                #print(f"Skipping: Blanks space")

            #print(f"this_dat = ord(Stingtoencodelist[i]) & 15 = {ord(stringToEncodeList[i]) & 15}")
            this_dat = ord(stringToEncodeList[i]) & 15
            #print(f"this_dat {this_dat}...")

            #print(f"LOCK_DAT = {lock_dat} : LOCK_CODE[LOCK_POS] = {lock_code[lock_pos]} : ord(LOCK_CODE[LOCK_POS]) = {ord(lock_code[lock_pos])}")
            #print(f"Xoring: {ord(stringToEncodeList[i])} {lock_code[lock_pos]} {lock_dat}")
            stringToEncodeList[i] = chr((ord(stringToEncodeList[i]) ^ (lock_code[lock_pos] ^ lock_dat)) + 1)
            #print(f"Became: {ord(stringToEncodeList[i])}")
            #print(f"Value after the xors {stringToEncodeList[i]}")
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
        s1 = ""
    else:
        k = 0
        for i in range(len(s1) - 1, 0, -1):
            if s1[i] == ';':
                k = i
        if k > 0:
            s1 = lstr(s1, k)

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
    if len(s) > 0 and s[0] != ";":
        s = encode(s)
    return s


def main():
    global lock_pos
    global lock_dat
    global lock_code
    global values
    lock_pos = -1
    lock_dat = 0
    # Make sure that the command entered is "main.py robot.at2" if not close the program
    if len(sys.argv) != 2:
         print("Usage: main.py <robot[.at2]> [locked[.atl]]")
         exit()

    # Get the current file path including .txt or .at2 w/e
    filePath = sys.argv[1]
    filePath = Path(filePath).stem + ".txt"
    outFilePath = (Path(filePath).stem + ".atl")
    currentDate = date.today().strftime("%d/%m/%Y")


    # Read from this file and store the contents in a variable called contents
    with open(filePath, mode="r", encoding="utf-8") as file:
        contents = file.read()
        #print(contents)

    # Write to this file
    with open(outFilePath, mode="w", encoding="utf-8") as file:

        # copy comment header
        print(";------------------------------------------------------------------------------", file=file)
        i = 0
        commentsComplete = False
        contentsList = contents.splitlines()
        #print(contentsList)
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
                #print(s)
                #print(f"S STRIPPED: {s}")
                if len(s) != 0 and s[0] == ";":
                    print(s, file=file)
                #print(s)
                i = i + 1
                #print(i)

        # lock header
        print(";------------------------------------------------------------------------------", file=file)
        print(f"; {Path(outFilePath).stem.upper()} Locked on {currentDate}", file=file)
        print(";------------------------------------------------------------------------------", file=file)
        # lock_code = ""
        # k = random.randint(20, 41)
        # for i in range(1, k):
        #     lock_code = lock_code + chr(random.randint(65, 96))

        # empty.at2
        #lock_code = "[ABTIBPJ[[XUWVDDP^T^^EUSAS]FVQJYZUZZ^OM"
        # RANDMAN3 LOCK lock_code = "WF_\\U\\DHNN^IPNYMQ^IE\\GTE^\\B\\SPBQNU_"
        #circles
        lock_code = "]QEU^TT_FWD[_XN]\\CMZVHXUH__ILZDWWM["
        #Randman3
        #lock_code = "WF_\\U\\DHNN^IPNYMQ^IE\\GTE^\\B\\SPBQNU_"
        #Sniper
        #lock_code = "^ZIHRXORFD_TIZNFIP^EA"
        #Tracker
        #lock_code = "HZAHR_Q\\VXT`MZ]\\LWSKL[DXVGJ]QQ[WO[UMU"
        #print(lock_code)
        print(f"#LOCK{Constants.locktype} {lock_code}", file=file)

        # decode lock-code
        lock_code_list = list(lock_code)
        #print(lock_code_list)
        for i in range(0, len(lock_code_list)):
            #print(lock_code[i])
            lock_code_list[i] = ord(lock_code_list[i]) - 65
            # print(lock_code_list[i])
        # This is not in the original convert lockcode to 0-31 values
        # print(f"LC LIST: {lock_code_list}")
        newCode = ""
        for i in range(0, len(lock_code_list)):
             newCode += str(lock_code_list[i])
        # print(f"newLC: {newCode}")
        lock_code = lock_code_list
        #print(lock_code)
        # lock_code1 = ''.join(str(lock_code_list))
        # print(lock_code1)
        print(f"Encoding {filePath}...")

        # Encode robot
        s = s.strip()
        if len(s) > 0:
            sUpper = s.upper()
            newLine = write_line('', sUpper)
            print(newLine, file=file)

        for line in contentsList:
            s1 = line
            s = ""
            s1 = s1.upper()
            s1 = s1.strip()
            newLine = write_line(s, s1)

            if len(newLine) > 0:
                print(newLine, file=file)
        print(f"Done. Used LOCK Format #{Constants.locktype}.")
        print(f"Only ATR2 v2.08 or later can decode.")
        print(f"Locked robot saved as {outFilePath}")

    #my_string = "this is a string"
    #for word in my_string.split():
     #   print(word)


if __name__ == "__main__":
    main()
