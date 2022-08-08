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
            for i in zippedXO:
                if i.count(i[0]) == 3:
                    return True

            if len(zippedXO[0]) == 3 and sorted(zippedXO[0]) == list(range(gridSize)):
                return True
        
            
