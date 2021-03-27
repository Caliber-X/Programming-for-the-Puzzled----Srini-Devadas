# Programming for the Puzzled -- Puzzle 2
# The Best Time to Party
# By Caliber_X

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]

sched2 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),
          (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2),
          (9.5, 10.0, 4), (10.0, 11.0, 2),
          (10.0, 12.0, 3), (11.0, 12.0, 7)]

sched3 = [(6, 7), (7,9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8),
          (9, 10), (11, 12), (11, 13), (11, 14)]


# Author: Caliber_X
def bestTimeToParty(schedule):

    # Time Range

    # Initialization
    time_s = schedule[0][0]
    time_l = schedule[0][1]

    for time in range(1, len(schedule)):
        
        # Smallest time
        time_s = min(time_s , schedule[time][0])

        # Largest Time
        time_l = max(time_l , schedule[time][1])
    
    print(time_s, time_l)

    max_count = 0

    # Finding time with max overlaps/counts
    for i in range(time_s, time_l):
        
        # print(i)
        count = 0

        for time in schedule:
            
            # print(time[])
            if i >= time[0] and i < time[1]:
                count += 1

        if max_count < count:
            max_count = count
            perfect_time = i

    print('Best time to attend the party is at', perfect_time, \
            'o\'clock', ':', max_count, 'celebrities will be attending!')

def bestTimeToPartySmart(schedule):

    times =[]   # Time list
    for i in schedule:
        times.append((i[0], 'start'))
        times.append((i[1], 'end'))
    # print(times)
    # print(len(times) is (2*len(schedule)))

    # Bubble Sort
    length = len(times)
    for i in range(length-1):
        for j in range(i+1, length):
            # Sending Smallest Element at first
            if times[i][0] > times[j][0]:
                temp = times[i]
                times[i] = times[j]
                times[j] = temp
                # times[i], times[j] = times[j], times[i]     # Swap
    # times.sort()  # Using Sort function
    # print(times)  # Sorted Timelist

    count = 0
    max_count = 0
    for i in times:

        if i[1] == 'start':
            count += 1
        else:
            count -= 1

        if max_count < count:
            max_count = count
            perfect_time = i[0]

    print('Best time to attend the party is at', perfect_time, \
          'o\'clock', ':', max_count, 'celebrities will be attending!')

def ex1(schedule, ystart, yend):

    times =[]   # Time list
    for i in schedule:
        times.append((i[0], 'start'))
        times.append((i[1], 'end'))
    # print(times)
    # print(len(times) is (2*len(schedule)))

    times.sort()  # Using Sort function
    # print(times)  # Sorted Timelist

    count = 0
    max_count = 0
    for i in times:

        if i[1] == 'start':
            count += 1
        else:
            count -= 1

        if max_count < count and  i[0] >= ystart and i[0] < yend:
            max_count = count
            perfect_time = i[0]

    print('Best time to attend the party is at', perfect_time, \
          'o\'clock', ':', max_count, 'celebrities will be attending!')

def ex2(schedule):

    # Sort
    schedule.sort()
    # print(schedule)

    max_count = 0
    prv_time = -1
    for i in schedule:

        if i[0] != prv_time:
            prv_time = i[0]
            count = 0

            for j in schedule:

                if i[0] >= j[0] and i[0] < j[1]:
                    count += 1

                if i[0] < j[0]:
                    break

            if max_count < count:
                max_count = count
                perfect_time = i[0]

    print('Best time to attend the party is at', perfect_time, \
          'o\'clock', ':', max_count, 'celebrities will be attending!')

def ex3(schedule):

    # Sort
    schedule.sort()
    # print(schedule)

    max_weight = 0
    tot_count = 0
    prv_time = -1
    for i in schedule:

        if i[0] != prv_time:
            prv_time = i[0]
            weight = 0
            count = 0

            for j in schedule:

                if i[0] >= j[0] and i[0] < j[1]:
                    count += 1
                    weight += j[2]

                if i[0] < j[0]:
                    break

            if max_weight < weight:
                max_weight = weight
                tot_count = count
                perfect_time = i[0]

    print('Best time to attend the party is at', perfect_time, \
            'o\'clock', ':', tot_count, 'celebrities will be attending', \
            'with a maximum weight of', max_weight)


# OUTPUTS
# bestTimeToParty(sched)
# bestTimeToPartySmart(sched)
# bestTimeToPartySmart(sched2)
# bestTimeToPartySmart(sched3)
# ex1(sched2, 7.0, 9.0)
# ex1(sched2, 10.0, 12.0)
# ex2(sched)
# ex2(sched2)
# ex2(sched3)
ex3(sched2)