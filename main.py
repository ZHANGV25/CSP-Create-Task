from sympy import symbols, solve #Uses sympy library from https://sympy.org as a simple solution for an algebra solver

'''
The following program solves for the different variables involved in physics kinematics equation
There are four kinematics equation, and five variables
We can get the forth value of each equation if we have three of the other four values
This program takes user input and plugs it into the right equation
The equation functions look for which value is needed, and solves for the value based on the information aquired
'''

#All four of the equations that are needed to solve for the variables
def eq1(vi, vf, a, t): #vf = vi + at
    #No displacement
    need = 0 #Which variable do you need?
    values = [vi, vf, a, t]
    for i in range(4):
        if(values[i] == "n"):
            need = i #Loops through, and if the one needed is found, keep track of which position on the list it is
    #Solve for the correct variable, based on which position in the list "need" is
    if (need == 0):
        vi = symbols('vi') #Creates the variable in which to solve for
        print(solve(vi+a*t-vf, vi)) #The first parameter for "solve" is the equation, which equals to zero. The second parameter is the variable to solve for
    elif (need == 1):
        vf = symbols('vf')
        print(solve(vi+a*t-vf, vf))
    elif (need == 2):
        a = symbols('a')
        print(solve(vi+a*t-vf, a))
    elif (need == 3):
        t = symbols('t')
        print(solve(vi+a*t-vf, t))

def eq2(vi, vf, d, t): #d = 0.5(vf+vi)t
    #No acceleration
    need = 0 #Which variable do you need?
    values = [vi, vf, d, t]
    for i in range(4):
        if(values[i] == "n"):
            need = i #Loops through, and if the one needed is found, keep track of which position on the list it is
    #Solve for the correct variable, based on which position in the list "need" is
    if (need == 0):
        vi = symbols('vi')
        print(solve(0.5*t*(vf+vi)-d, vi))
    elif (need == 1):
        vf = symbols('vf')
        print(solve(0.5*t*(vf+vi)-d, vf))
    elif (need == 2):
        d = symbols('d')
        print(solve(0.5*t*(vf+vi)-d, d))
    elif (need == 3):
        t = symbols('t')
        print(solve(0.5*t*(vf+vi)-d, t))

def eq3(vi, a, d, t): #d=vi*t+0.5at^2
    #No final velocity
    need = 0 #Which variable do you need?
    values = [vi, a, d, t]
    for i in range(4):
        if(values[i] == "n"):
            need = i #Loops through, and if the one needed is found, keep track of which position on the list it is
    #Solve for the correct variable, based on which position in the list "need" is
    if (need == 0):
        vi = symbols('vi')
        print(solve((vi*t)+(0.5*a*(t**2))-d, vi))
    elif (need == 1):
        a = symbols('a')
        print(solve((vi*t)+(0.5*a*(t**2))-d, a))
    elif (need == 2):
        d = symbols('d')
        print(solve((vi*t)+(0.5*a*(t**2))-d, d))
    elif (need == 3):
        t = symbols('t')
        print(solve((vi*t)+(0.5*a*(t**2))-d, t))

def eq4(vi, a, d, vf): #vf^2 = vi^2 + 2ad
    #No time
    need = 0 #Which variable do you need?
    values = [vi, a, d, vf]
    for i in range(4):
        if(values[i] == "n"):
            need = i #Loops through, and if the one needed is found, keep track of which position on the list it is
    #Solve for the correct variable, based on which position in the list "need" is
    if (need == 0):
        vi = symbols('vi')
        print(solve((vi**2) + (2*a*d) - (vf**2), vi))
    elif (need == 1):
        a = symbols('a')
        print(solve((vi**2) + (2*a*d) - (vf**2), a))
    elif (need == 2):
        d = symbols('d')
        print(solve((vi**2) + (2*a*d) - (vf**2), d))
    elif (need == 3):
        vf = symbols('vf')
        print(solve((vi**2) + (2*a*d) - (vf**2), vf))

#Method to convert to float
def convertToFloat(_input):
    try: #Try and except, skipping over the string
        _input = float(_input)
    except ValueError:
        pass
    return _input

running = True #Logic to determine whether or not to continue the loop
while running: #Main loop
    #Gives instructions to user
    print("Which quantities do you have?")
    print("Enter everything you know. Notate the value you need with \"x\". Notate anything you do not have with \"n\": ")

    inputs = [] #Create list to store raw inputs
    #Collects user inputs
    inputs.append(input("Acceleration: "))
    inputs.append(input("Initial Velocity: "))
    inputs.append(input("Final Velocity: "))
    inputs.append(input("Displacement: "))
    inputs.append(input("Time: "))

    #Loop through the input list, and convert all of the strings that are numbers into floats.
    for i in range(5):
        inputs[i] = convertToFloat(inputs[i])
    
    #Check which one to solve for
    #This assings which equation to use
    #The raw input is in the order of (a, vi, vf, d, t). 
    #This order is converted into whichever order is used in the functions themselves
    for i in range(5):
        if(inputs[i] == "x"): #If the input recieves "x" for that value, then that means the user does not have 
            if(i == 0): #No acceleration
                #vi, vf, d, t
                #d = 0.5(vf+vi)t
                eq2(inputs[1], inputs[2], inputs[3], inputs[4])
            elif(i == 1): #No initial velocity
                print("We always need initial velocity!") #All of the kinematics equation need initial velocity
            elif(i == 2): #No final velocity
                #vi, a, d, t
                #d=vi*t+0.5at^2
                eq3(inputs[1], inputs[0], inputs[3], inputs[4])
            elif(i == 3): #No displacement
                #vi, vf, a, t
                #vf = vi + at
                eq1(inputs[1], inputs[2], inputs[0], inputs[4])
            elif(i == 4): #No time
                #vf^2 = vi^2 + 2ad
                #vi, a, d, vf
                eq4(inputs[1], inputs[0], inputs[3], inputs[2])
    if (input("Continue? (y/n) ") != "y"):
        running = False
