# Programming for the Puzzled -- Puzzle 1
# You Will All Conform
# By Caliber_X

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']    #Ex 3

def pleaseConfirm(caps):
    
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps += ['END']
    
    for i in range(1, len(caps)):
        
        if caps[i] != caps[start]:

            # each interval is a tuple with 3 elements (start, end, type)
            if caps[start] != 'H':  #exclude H elements in intervals list
                intervals.append((start, i - 1, caps[start]))

            if caps[start] == 'F':
                forward += 1
            elif caps[start] == 'B':
                backward += 1

            start = i
    
    print(intervals)
    print(forward, backward)

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'

    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print ("Person at position", t[0], "flip your cap!")
            else:
                print("People in positions", t[0], "through", t[1], "flip your caps!")

 
def pleaseConfirmSinglePass(caps):

    caps += caps[0]

    for i in range(1, len(caps)):

        if caps[i] != caps[i - 1]:

            if caps[i] != caps[0]:
                start = i
            else:
                if start != i-1 :
                    print("People in positions", start , "through", i - 1, "flip your caps!")
                else:
                    print("People in position", start ,"flip your cap!")
        
        
pleaseConfirm(cap3)
# pleaseConfirmSinglePass(cap2)