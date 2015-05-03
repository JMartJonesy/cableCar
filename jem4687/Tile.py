class Tile():
    __slots__ = ('Tracks','Rotation','Type')
    def __init__(self,nRotation,nType,nTracks):
        self.Rotation=nRotation
        self.Type=nType
        self.Tracks=nTracks