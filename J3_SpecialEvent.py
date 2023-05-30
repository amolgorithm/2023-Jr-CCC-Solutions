N = int(input()) #number of interested people

if N < 0: #checking that N is non-negative
    raise ValueError()

days = ["", "", "", "", ""] #list to hold people's availability for each day

#For each interested person,
for i in range(N):
    availability = str(input()) #availability for each day is inputed (e.g. "YY.Y.")
    
    for c in range(5): #for each day,
        if availability[c] == "Y": #if the availability is "Y", meaning available,
            days[c] += "Y" #that day appends a "Y"

largest = [[0, 0]]
for s in range(len(days)):
    stri = days[s]
    lenStr = len(stri)
    
    if lenStr == largest[0][0]:
        largest.append([lenStr, s])
    
    if lenStr > largest[0][0]:
        largest = [[lenStr, s]] #length value, index


T = [str(l[1] + 1) for l in largest]
print(", ".join(T))
