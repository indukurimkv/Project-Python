import numpy as np

def checkWin(imageObjects):
    gridSize = 3
    Xs = []
    Os = []

    for XO in imageObjects:
        if XO.value == "x":
            Xs.append(np.array(XO.indeces))
        else:
            Os.append(np.array(XO.indeces))
    
    for XO in Xs, Os:
        if len(XO) < gridSize:
            continue     

        p1, p2, p3 = 0, 0, 0
        while p1 < len(XO):
            if len(set((p1,p2,p3))) == gridSize:
                slope1 = XO[p2] - XO[p1]
                slope1 = slope1[1]/slope1[0]
                slope2 = XO[p3] - XO[p2]
                slope2 = slope2[1]/slope2[0]
                if slope1 == slope2:
                    return True
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


        
            
