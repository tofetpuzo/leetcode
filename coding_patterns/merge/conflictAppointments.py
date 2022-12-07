from typing import List


def conflictAppointments(appointments: List[List[int]]):
    appointments.sort()
    start = appointments[0][0]
    end = appointments[0][1]
    sf = ""
    
    for i in range(1, len(appointments)):
        interv = appointments[i]
        if end >= interv[0]:
            sf += '{0} and {1} conflict \n'.format(
                [start, end], [interv[0], interv[1]])
        else:
            start = interv[0]
            end = interv[1]
    return sf
        
    # return start_output, end_output
    # [1, 5]

# [[1, 5], [2, 6], [3, 7], [4, 100], [5, 6], [10, 15]]
#   ^
appointments = [[1, 5], [3, 7], [2, 6], [10, 15], [5, 6], [4, 100]]

print(conflictAppointments( appointments))
# [2,6] Conflicts with [1,5]
# [3,7] Conflicts with [1,5]
# [5,6] Conflicts with [3,7]
# [4,100] Conflicts with [1,5]