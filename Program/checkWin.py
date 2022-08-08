def checkWin(imageObjects):
    gridSize = 3
    Xs = set()
    Os = set()
    
    for XO in imageObjects:
        if XO.value == "x":
            Xs.add(XO.indeces)
        else:
            Os.add(XO.indeces)

    # First check for wins on X and then check for wins on O
    # zippedXO is a list of 2 lists, with the child list each holding x and y values respectively
    for zippedXO in list(zip(*Xs)), list(zip(*Os)):
        # Check if any moves have been made at all
        if zippedXO:

            # Check for horizontal or vertical wins
            for i in zippedXO:
                if i.count(i[0]) == gridSize:
                    return True
            # Check for diagonal wins
            if sorted(zippedXO[0]) == list(range(gridSize)):
                return True
        
            
