def checkWin(imageObjects):
    gridSize = 3
    XXRange = set()
    XYRange = set()
    OXRange = set()
    OYRange = set()

    for xo in imageObjects:
        if xo.value == "x":
            XXRange.add(xo.indeces[0])
            XYRange.add(xo.indeces[1])
        if xo.value == "o":
            OXRange.add(xo.indeces[0])
            OYRange.add(xo.indeces[1])
    print(XXRange,XYRange,OXRange,OYRange)
    if len(XXRange) == gridSize:
        return True, "x"
    if len(XYRange) == gridSize:
        return True, "x"
    if len(OXRange) == gridSize:
        return True, "o"
    if len(OYRange) == gridSize:
        return True, "o"
