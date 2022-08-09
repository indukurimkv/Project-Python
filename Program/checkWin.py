import numpy as np

def checkWin(imageObjects):
    gridSize = 3
    Xs = []
    Os = []

    # Sort marks into X and O
    for XO in imageObjects:
        if XO.value == "x":
            Xs.append(np.array(XO.indeces))
        else:
            Os.append(np.array(XO.indeces))
    
    for XO in Xs, Os:
        # Skip the rest of the function if three marks are not on board
        if len(XO) < gridSize:
            continue     

        p1, p2, p3 = 0, 0, 0
        while p1 < len(XO):
            # Find set of three positions
            if len(set((p1,p2,p3))) == gridSize:
                # Check for wins
                seg1 = XO[p1] - XO[p2]
                seg2 = XO[p2] - XO[p3]

                if all(seg1 == seg2):
                    return True
            # Find all possible permutations of the position array
            if p3 + 1 < len(XO):
                p3 += 1
            elif p2 + 1 < len(XO):
                p2 += 1
                p3 = 0
            else:
                p1 += 1
                p2 = 0
                p3 = 0
    return False


        
            
