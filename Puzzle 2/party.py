#Programming for the Puzzled -- Srini Devadas
#yThe Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Brute force algorithm implemented here

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]

def bestTimeToParty(schedule):
    #Find start time and end time
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)

    #compute count of celebrities at each time
    count = celebrityDensity(schedule, start, end)
    
    ##    print (count)
    maxcount = 0
    #Range over times to find the time when the maximum celebrities are around.
    for i in range(start, end + 1):
        if count[i] > maxcount:
            maxcount = count[i]
            time = i

    ##    maxcount = max(count[start:end + 1])
    ##    time = count.index(maxcount)

    #Output the best time to party.
    #Note that the \ means the statement continues on the next line.
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')


def celebrityDensity(sched, start, end):

    #Initialize a list of length end + 1 to all 0's
    count = [0] * (end + 1)
    # i ranges over different times
    for i in range(start, end + 1):
        count[i] = 0
        for c in sched:
            #Check if celebrity c is around at time i
            if c[0] <= i and c[1] > i:
                count[i] += 1
                
    return count
                

bestTimeToParty(sched)   