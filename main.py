def newParseIdea(string):
    '''
    string : (instruction | ) (ax|bx|cx|dx|port) (INT number)
    '''
    # our ex string is ["mov", "ax", "10"]
    # if the string in the first index is in commands it will go into here
    if string[0] in commands:
        # if the string in the first index is "mov" we will move forward assuming the syntax is correct for mov
        if string[0] == "mov":
            commands[string[0]](string[1], string[2])
        # [OPO N1 N2] Outputs N2 to port N1
        elif string[0] == "opo":
            print("in opo")
            commands[string[0]](string[1], string[2])
        elif string[0] == "ipo":
            commands[string[0]](string[1], string[2])
        elif string[0] == "mod":
            commands[string[0]](string[1], string[2])
        elif string[0] == "neg":
            commands[string[0]](string[1])


ax = 0
bx = 0
cx = 0
dx = 0

p_throttle = 2
p_steering = 0
p_weapon = 3
p_scanarc = 0
p_scan = 0
p_random = 10


# [MOV V N] Sets V = N
def mov(v, n):
    if v in registers:
        if n in registers:
            registers[v] = registers[n]
        elif n in constants:
            registers[v] = constants[n]
        elif n.isnumeric():
            registers[v] = n
    elif v in constants:
        if n in registers:
            constants[v] = registers[n]
        elif n in constants:
            constants[v] = constants[n]
        elif n.isnumeric():
            constants[v] = n


# [OPO N1 N2] Outputs N2 to port N1
def opo(n1, n2):
    if n1 in constants:
        if n2 in constants:
            constants[n1] = constants[n2]
            print(f"TEST:{constants[n1]}")
        elif n2.isnumeric():
            print(f"TEST:{constants[n1]}")
            constants[n1] = n2


# [IPO N V] Inputs number from port N, result into V
def ipo(n, v):
    if n in constants:
        if v in constants:
            constants[v] = constants[n]
            print(constants[v])
        elif v.isnumeric():
            constants[v] = n
        elif v in registers:
            registers[v] = constants[n]


# [MOD V N] MOD's V & N, result stored in V (modulus)
def mod(v, n):
    if v in constants:
        if n in constants:
            constants[v] = int(constants[v]) % int(constants[n])
        elif n.isnumeric():
            constants[v] = int(constants[v]) % int(n)
        elif n in registers:
            constants[v] = int(constants[v]) % int(registers[n])
    elif v in registers:
        if n in constants:
            registers[v] = int(registers[v]) % int(constants[n])
        elif n.isnumeric():
            registers[v] = int(registers[v]) % int(n)
        elif n in registers:
            registers[v] = int(registers[v]) % int(registers[n])


# [NEG V] Negates V: V = 0-V (aka "two's compliment")
def neg(v):
    if v in constants:
        constants[v] = int(constants[v]) * -1
    if v in registers:
        registers[v] = int(registers[v]) * -1


# any command such as mov or add go here
commands = {
    "mov": mov,
    "opo": opo,
    "ipo": ipo,
    "mod": mod,
    "neg": neg,
}

# these are our "fake" registers
registers = {
    "ax": ax,
    "bx": bx,
    "cx": cx,
    "dx": dx,
}

constants = {
    "p_scanarc": p_scanarc,
    "p_throttle": p_throttle,
    "p_steering": p_steering,
    "p_scan": p_scan,
    "p_weapon": p_weapon,
    "p_random": p_random,
}

# this is the string we will pass into the function to parse (it is just one example line)
string = "mov                ax                10"
# split the string into individual words so that we can figure out each word individually
# .split also removes white spaces
stringList = string.split()
print(stringList)

# Pass the stringList to new parse idea
newParseIdea(stringList)
newParseIdea(["opo", "p_throttle", "p_weapon"])
print(f"p_throttle: {p_throttle}")
newParseIdea(["mod", "p_random", "2"])
print(p_random)
newParseIdea(["neg", "p_random"])
print(p_random)
