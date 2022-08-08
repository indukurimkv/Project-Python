def checkWin(imageObjects):
    gridSize = 3
    Xs = set()
    Os = set()
    
    for XO in imageObjects:
        if XO.value == "x":
            Xs.add(XO.indeces)
        else:
            Os.add(XO.indeces)

    
    for zippedXO in tuple(zip(*Xs)), tuple(zip(*Os)):
        if zippedXO:

            # Check for horizontal or vertical wins
            for i in zippedXO:
                if i.count(i[0]) == 3:
                    return True
            # Check for diagonal wins
            if sorted(zippedXO[0]) == list(range(gridSize)):
                return True
        
            
