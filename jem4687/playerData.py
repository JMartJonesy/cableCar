"""
Cable Car: Student Computer Player

A sample class you may use to hold your state data
Author: Adam Oest (amo9149@rit.edu)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
Author: YOUR NAME HERE (your email address)
"""
from Tile import *
class PlayerData(object):
    """A sample class for your player data"""
    
    # Add other slots as needed
    __slots__ = ('logger', 'playerId', 'currentTile', 'numPlayers','board','Score','Dictionary')
    
    def __init__(self, logger, playerId, currentTile, numPlayers):
        """
        __init__: PlayerData * Engine.Logger * int * NoneType * int -> None
        Constructs and returns an instance of PlayerData.
            self - new instance
            logger - the engine logger
            playerId - my player ID (0-5)
            currentTile - my current hand tile (initially None)
            numPlayers - number of players in game (1-6)
        """
        
        self.logger = logger
        self.playerId = playerId
        self.currentTile = currentTile
        self.numPlayers = numPlayers
        self.board=[[None for i in range(8)] for j in range(8)]
        self.board[3][3]=Tile(0,'ps',[])
        self.board[3][4]=Tile(0,'ps',[])
        self.board[4][3]=Tile(0,'ps',[])
        self.board[4][4]=Tile(0,'ps',[])
        self.Dictionary={'a':[[0,0],[1,3],[2,2],[3,1]]}
        self.Dictionary['b']=[[0,1],[1,3],[2,0],[3,2]]
        self.Dictionary['c']=[[0,1],[1,2],[2,0],[3,3]]
        self.Dictionary['d']=[[0,0],[1,3],[2,1],[3,2]]
        self.Dictionary['e']=[[0,0],[1,1],[2,3],[3,2]]
        self.Dictionary['f']=[[0,2],[1,3],[2,0],[3,1]]
        self.Dictionary['g']=[[0,0],[1,1],[2,2],[3,3]]
        self.Dictionary['h']=[[0,3],[1,0],[2,1],[3,2]]
        self.Dictionary['i']=[[0,1],[1,2],[2,3],[3,0]]
        self.Dictionary['j']=[[0,3],[1,2],[2,1],[3,0]]
        self.Score=0
        
        # initialize any other slots you require here
        
    def __str__(self):
        """
        __str__: PlayerData -> string
        Returns a string representation of the PlayerData object.
            self - the PlayerData object
        """
        result = "PlayerData= " \
                    + "playerId: " + str(self.playerId) \
                    + ", currentTile: " + str(self.currentTile) \
                    + ", numPlayers:" + str(self.numPlayers)
                
        # add any more string concatenation for your other slots here
                
        return result