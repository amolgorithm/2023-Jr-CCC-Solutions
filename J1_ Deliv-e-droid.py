P = int(input()) #number of packages delivered
C = int(input()) #number of collisions

if P < 0 or C < 0: #checking that both P and C are both non-negative.
    raise ValueError()
    
#50 points for each package delivered, -10 points for every collision, and 500 points if the number of packages delivered is greater that the number of collisions.
F = P * 50 - C * 10 + (500 if P > C else 0)

print(F)
