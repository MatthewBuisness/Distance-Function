import math
FinalDistance=0
def distance(startX,startY,goalX,goalY):
    if startX==goalX and startY==goalY:
        FinalDistance=0
        return FinalDistance
    if startX>goalX:
        throwawayvar=1
        if startY>goalY:
            TempX=startX-goalX
            TempY=startY-goalY 
            TempX=int(TempX)*int(TempX)
            TempY=int(TempY)*int(TempY)
            TempTotal=TempX+TempY 
            FinalDistace=math.sqrt(TempTotal)
        elif goalY>startY:
            TempX=startX-goalX
            TempY=goalY-startY
            TempX=int(TempX)*int(TempX)
            TempY=int(TempY)*int(TempY)
            TempTotal=TempX+TempY 
            FinalDistace=math.sqrt(TempTotal)
    elif startX<goalX:
        throwawayvar=1
        if startY>goalY:
            TempX=goalX-startX
            TempY=startY-goalY 
            TempX=int(TempX)*int(TempX)
            TempY=int(TempY)*int(TempY)
            TempTotal=TempX+TempY 
            FinalDistace=math.sqrt(TempTotal)
        elif goalY>startY:
            TempX=goalX-startX
            TempY=goalY>startY 
            TempX=int(TempX)*int(TempX)
            TempY=int(TempY)*int(TempY)
            TempTotal=TempX+TempY 
            FinalDistace=math.sqrt(TempTotal)
            return FinalDistance
    elif startX==goalX:
        throwawayvar=1 
        if startY>goalY:
            FinalDistance=startY-goalY
        elif goalY>startY:
            FinalDistance=goalY-startY
    else:
        print("error, getting this error code shouldnt be possible lmao")