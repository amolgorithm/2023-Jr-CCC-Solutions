C = int(input()) #number of columns (for tiling)

if C < 0: #checking that C is non-negative
    raise ValueError()
    
row1 = str(input()) #wet(1) or dry(0), each tile in top row of tiles is inputed (with spaces in between, no. of numbers is C) (e.g. 0 1 0 1 0)
row2 = str(input()) #wet(1) or dry(0), each tile in bottom row of tiles is inputed (with spaces in between, no. of numbers is C) (e.g. 0 1 0 1 0)

if len(row1) != (C * 2 - 1) or len(row2) != (C * 2 - 1): #if top row number of characters not equal to C + no. spaces OR bottom row number of characters not equal to C + no. spaces
    raise ValueError()

row1 = row1.replace(" ", "") #all spaces are removed
row2 = row2.replace(" ", "") #all spaces are removed

tiles = [row1, row2] #the laneway tiles is top row + bottom row
M = 0 #minimum metres of tape needed for perimeters of all wet areas

for i in range(len(tiles)): #each row
    for j in range(len(tiles[i])): #each tile in row
        if tiles[i][j] == "1": #if the tile is a wet triangle
            M += 3     #M increase by three because that is perimeter of the wet triangle, which is an answer but not minimum, which will be reduced.
            
            if j > 0 and tiles[i][j-1] == "1": #if the tile behind in the row is also a wet triangle, (adjacent triangles),
                M -= 2 #reduce M by 2, because we are removing 1 meter from both perimeters of the adjacent wet triangles, which was overcounted by M when done += 3.
                
            if i == 0 and tiles[i+1][j] == "1" and j % 2 == 0: #if the tile below in the column is also a wet triangle, (adjacent triangles),
                M -= 2 #reduce M by 2, because we are removing 1 meter from both perimeters of the adjacent wet triangles, which was overcounted by M when done += 3.
        
print(M) #prints answer
