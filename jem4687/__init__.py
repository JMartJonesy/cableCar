from Model.interface import PlayerMove
from playerData import PlayerData
from Tile import *
"""
Cable Car: Student Computer Player

Complete these function stubs in order to implement your AI.
Author: Adam Oest (amo9149@rit.edu)
Author: Jesse Martinz (jem4687@rit.edu)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
"""

def init(playerId, numPlayers, startTile, logger, arg = "None"):
    """The engine calls this function at the start of the game in order to:
        -tell you your player id (0 through 5)
        -tell you how many players there are (1 through 6)
        -tell you what your start tile is (a letter a through i)
        -give you an instance of the logger (use logger.write("str") 
            to log a message) (use of this is optional)
        -inform you of an additional argument passed 
            via the config file (use of this is optional)
        
    Parameters:
        playerId - your player id (0-5)
        numPlayers - the number of players in the game (1-6)
        startTile - the letter of your start tile (a-j)
        logger - and instance of the logger object
        arg - an extra argument as specified via the config file (optional)

    You return:
        playerData - your player data, which is any data structure
                     that contains whatever you need to keep track of.
                     Consider this your permanent state.
    """
    
    # Put your data in here.  
    # This will be permanently accessible by you in all functions.
    # It can be an object, list, or dictionary
    playerData = PlayerData(logger, playerId, startTile, numPlayers)
    
    
    # This is how you write data to the log file
    playerData.logger.write("Player %s starting up" % playerId)
    # This is how you print out your data to standard output (not logged)
    print(playerData)
    
    return playerData

def move(playerData):  
    """The engine calls this function when it wants you to make a move.
    
    Parameters:
        playerData - your player data, 
            which contains whatever you need to keep track of
        
    You return:
        playerData - your player data, 
            which contains whatever you need to keep track of
        playerMove - your next move
    """
    
    playerData.logger.write("move() called")

    # Populate these values
    playerId = None # 0-5
    position = None # (row, column)
    tileName = None # a-j
    rotation = None # 0-3 (0 = north, 1 = east, 2 = south, 3 = west)
    
    return playerData, PlayerMove(playerId, position, tileName, rotation)

def move_info(playerData, playerMove, nextTile):
    """The engine calls this function to notify you of:
        -other players' moves
        -your and other players' next tiles
        
    The function is called with your player's data, as well as the valid move of
    the other player.  Your updated player data should be returned.
    
    Parameters:
        playerData - your player data, 
            which contains whatever you need to keep track of
        playerMove - the move of another player in the game, or None if own move
        nextTile - the next tile for the player specified in playerMove, 
                    or if playerMove is None, then own next tile
                    nextTile can be none if we're on the last move
    You return:
        playerData - your player data, 
            which contains whatever you need to keep track of
    """
    
    playerData.logger.write("move_info() called")
    dummy=transform(playerData.Dictionary[playerMove.tileName],playerMove.rotation)
    placedTile=Tile(playerMove.rotation,playerMove.tileName,dummy)
    playerData.board[playerMove.position[0]][playerMove.position[1]]=placedTile
    if nextTile!=None:
        newTile=Tile(0,nextTile,playerData.Dictionary[nextTile])
        playerData.currentTile=newTile
    return playerData

################################# PART ONE FUNCTIONS #######################
# These functions are called by the engine during part 1 to verify your board 
# data structure
# If logging is enabled, the engine will tell you exactly which tests failed
# , if any
def transform(diction,rot):
    dummy=[]
    for (en,ex) in diction:
        c=(en+rot)%4
        d=(ex+rot)%4
        dummy.append((c,d))
    return dummy

def tile_info_at_coordinates(playerData, row, column):
    """The engine calls this function during 
        part 1 to validate your board state.
    
    Parameters:
        playerData - your player data as always
        row - the tile row (0-7)
        column - the tile column (0-7)
    
    You return:
        tileName - the letter of the tile at the given coordinates (a-j), 
            or 'ps' if power station or None if no tile
        tileRotation - the rotation of the tile 
            (0 is north, 1 is east, 2 is south, 3 is west.
            If the tile is a power station, it should be 0.  
            If there is no tile, it should be None.
    """  
    tileName=None
    tileRotation=None
    if playerData.board[row][column]!=None:
        tileName= playerData.board[row][column].Type
        tileRotation=playerData.board[row][column].Rotation 
    return (tileName, tileRotation)

def route_complete(playerData, carId):
    """The engine calls this function 
        during part 1 to validate your route checking
    
    Parameters:
        playerData - your player data as always
        carId - the id of the car where the route starts (1-32)
        
    You return:
        isComplete - true or false depending on whether or not this car
             connects to another car or power station"""
    
    if carId>=1 and carId<=8:
        current=[0,carId-1]
        entrance=0
    elif carId>8 and carId<=16:
        current=[carId-9,7]
        entrance=1
    elif carId>16 and carId<=24:
        current=[7,24-carId]
        entrance=2
    else:
        current=[32-carId,0]
        entrance=3
    doesIt,score=isComplete(playerData,current,entrance,0)
    return doesIt

def isComplete(playerData,current,entrance,score):
    if current[0]<0 or current[0]>7 or current[1]<0 or current[1]>7:
        return True,score
    else:
        looksy=playerData.board[current[0]][current[1]]
        if looksy==None:
            return False,score
        if looksy.Type=='ps':
            return True,score*2
        else:
            score=score+1
            for (en,ex) in looksy.Tracks:
                if en==entrance:
                    if ex==0:
                        return isComplete(playerData,[current[0]-1,current[1]],2,score)
                    if ex==1:
                        return isComplete(playerData,[current[0],current[1]+1],3,score)
                    if ex==2:
                        return isComplete(playerData,[current[0]+1,current[1]],0,score)
                    if ex==3:
                        return isComplete(playerData,[current[0],current[1]-1],1,score)

def route_score(playerData,carId):
    """The engine calls this function 
        during route 1 to validate your route scoring
    
    Parameters:
        playerData - your player data as always
        carId - the id of the car where the route starts (1-32)
        
    You return:
        score - score is the length of the current route from the carId.
                if it reaches the power station,
                the score is equal to twice the length.
    """
    
    if carId>=1 and carId<=8:
        current=[0,carId-1]
        entrance=0
    elif carId>8 and carId<=16:
        current=[carId-9,7]
        entrance=1
    elif carId>16 and carId<=24:
        current=[7,24-carId]
        entrance=2
    else:
        current=[32-carId,0]
        entrance=3
    doesIt,score=isComplete(playerData,current,entrance,0)
    return score

def game_over(playerData, historyFileName = None):
    """The engine calls this function after the game is over
        (regardless of whether or not you have been kicked out)

    You can use it for testing purposes or anything else you might need to do...
    
    Parameters:
        playerData - your player data as always
        historyFileName - name of the current history file, 
            or None if not being used 
    """
    
    # Test things here, changing the function calls...
    print "History File: %s" % historyFileName
    print "If it says False below, you are doing something wrong"
    
    if historyFileName == "example_complete_start.data":
        print tile_info_at_coordinates(playerData, 5, 2) == ('e', 0)
        print tile_info_at_coordinates(playerData, 7, 7) == ('f', 0)
        print tile_info_at_coordinates(playerData, 4, 4) == ('ps', 0)
        
        print route_complete(playerData,25) == True
        print route_complete(playerData,12) == True
        print route_complete(playerData,3) == True
        
        print route_score(playerData,12) == 12
        print route_score(playerData,13) == 5
        print route_score(playerData,3) == 18
        
    elif historyFileName == "example_incomplete1.data":
        print tile_info_at_coordinates(playerData, 6, 0) == ('b', 1)
        print tile_info_at_coordinates(playerData, 6, 4) == (None, None)
        print tile_info_at_coordinates(playerData, 0, 6) == ('j', 1)
        
        print route_complete(playerData,25) == False
        print route_complete(playerData,12) == False
        print route_complete(playerData,3) == False
        
        print route_score(playerData,26) == 1
        print route_score(playerData,12) == 0
        print route_score(playerData,3) == 0
        
    elif historyFileName == "testage.data":
        print tile_info_at_coordinates(playerData, 0, 3) == ('c', 0)
        print tile_info_at_coordinates(playerData, 3, 5) == (None, None)
        print tile_info_at_coordinates(playerData, 3, 3) == ('ps', 0)
        
        print route_complete(playerData,25) == False
        print route_complete(playerData,12) == False
        print route_complete(playerData,3) == False
        
        print route_score(playerData,25) == 0
        print route_score(playerData,12) == 0
        print route_score(playerData,4) == 3
    