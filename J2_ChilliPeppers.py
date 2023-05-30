N = int(input()) #number of peppers to add to the chilli

if N < 0: #checking the N is non-negative
    raise ValueError()

#Each pepper name mapped to its SHU rating
peppers_SHU_dict = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}
T = 0 #total SHU level of chilli

for i in range(N):
    T += peppers_SHU_dict[str(input())]
    
print(T)
