# 2023 Junior CCC (Canadian Computing Challenge)  Solutions and Explanations

Link to problems: [2023 Junior CCC Problems](https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/juniorEF.pdf)

Commented solution code is added in repository.
<br><br>
## Explanations
### J1 - Deliv-e-droid:
- If we get 50 points for each package delivered and there are P packages delivered, then we are getting P * 50 points.
- If we lose 10 points for each collision and there C collisions, then we are losing C * 10.
- If we get 500 bonus points only when there are more packages delivered than collisions, we are getting those 500 points only when P > C. So, we could have a one-line if statement for that, to express whether or not we receive those 500 points: `500 if P > C else 0 ` <- This if statement will give 500 points if P > C and 0 if not. We are using a one-line if statement because it will be easier when we are "totalling" up the points.
- Now, we total up the points: `P * 50 - C * 10 + (500 if P > C else 0)`
<br>

### J2 - Chilli Peppers:

- We are given a table where every pepper is mapped to its SHU rating, which is essentially a map/dictionary when translated to coding. It is a dictionary where the each pepper name (string) is mapped to its SHU rating (integer). And we implement this dictionary in the code, as it will be used later.
- Let N be the input value of how many peppers will be added.
- Let T be the total SHU level of the chilli after adding the peppers. This can be initially set to a null value like 0.
- We are creating a for loop that loops N number of times, so that we can add the SHU rating of each input pepper to T. To do this, we are doing: ` T += peppers_SHU_dict[str(input())]` <- peppers_SHU_dict[str(input())] returns the mapped integer value for the pepper name, which is str(input()). This will only work if the inputted string is exactly the same as the pepper name string in the dictionary, as there is no check occurring to verify str(input()) as a valid key in the dictionary.
- After all the SHU ratings are accumulated into T, we obtain our final answer, which we then print.
<br>

### J4 - Trianglane:
The ultimate formula to find out the minimum metres of tape is the total sum of the perimeters of each wet triangle tiles minus 2 metres from each two adjacent triangles. This is because: when we get the total sum of the perimeters of each wet triangle tiles, that is a possible number of metres of tape that can be used, but it is not the *minimum*. So, we need to *minimize* our total sum. To do this, we have to remove unnecessary tape. Tape becomes unnecessary when it is inside two wet triangle tiles, as the perimeter is already covered by tape, so the inside is completely unnecessary. But how do we know if the tape is inside two wet triangle tiles? Well, if we carefully study images of these such tiles, we recognize that the inside tape is the common side shared between two adjacent wet triangle tiles. So, we have to subtract the length of each common side between two adjacent wet triangles from the total perimeter sum? Close, not exactly. We have to subtract **TWICE** the length of each common side between two adjacent wet triangles from the total perimeter sum. This is because, our perimeter sum has that common side length twice when we add the adjacent wet triangle perimeters, as that common side length is added once for one triangle, and another time for the other triangle. So, now, we know our algorithm, and we just formulate that into code.
 - (Explanation for code is commented in file)
 - Quick note:  In the file, we have a statement `if i == 0 and tiles[i+1][j] == "1" and j % 2 == 0:`, where we have j % 2 == 0. The reason for that is because the j value has to be even for the adjacent triangle tiles to have a common side instead of a common vertex. Drawing down such tiles will aid in understanding this.
