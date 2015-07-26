class Tile:
    """  Represents a domino tile which can be placed by a player. """
    def __init__(self, lft, rgt):
        self.__lft = lft
        self.__rgt = rgt
        
    def get_lft(self):
        return self.__lft
        
    def get_rgt(self):
        return self.__rgt

    def match_lft(self, tile):
        if self.__lft == tile.__lft:
            return -1
        elif self.__lft == tile.__rgt:
            return +1
        else:
            return 0

    def match_rgt(self, tile):
        if self.__rgt == tile.__lft:
            return -1
        elif self.__rgt == tile.__rgt:
            return +1
        else:
            return 0

class Player:
    """ Represents a (you guess it) a player. """
    def __init__(self, name):
        self.__name = name
        self.__tiles = []
        
    def set_tiles(self, tiles):
        self.__tiles = tiles

    def get_tiles(self):
        return self.__tiles
        
    def play(self, game):
        """ Place a piece or draw a tile from the game's heap """
        
        # Check if I can play a tile
        for tile in self.__tiles:
            if self.__can_play(self, tile, game):
                self._play_impl(game)
                return
        
        # I cannot play it, so I draw a new tile
        new_tile = game.draw()
        if new_tile:
            tiles.append(new_tile)
        
    def __play_impl(self, game):
        pass
        
    def __can_play(self, tile, game):
        """ Check if the player can play """
        return (game.get_cur_lft().match_lft(tile) 
            or (game.get_cur_rgt().match_rgt(tile))

class Game:
    
    def __init__(self, tiles):
        self.__tiles = tiles
        self.__left_tile_in_game = None
        self.__right_tile_in_game = None
    
    def draw(self):
        return self.tiles_in_heap.pop()
        
    def place_lft(self, tile, orientation):
        if orientation == -1:
            self.__left_tile_game = tile.rgt
        else: #we assume orientation is +1
            self.__left_tile_game = tile.lft
            
    def place_rgt(self, tile, orientation):
        if orientation == +1:
            self.__right_tile_game = tile.lft
        else: #we assume orientation is -1
            self.__right_tile_game = tile.rgt
            

class HumanPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name)
        
class AIPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name)
        
    def __play_impl(game):
        for tile in self.tiles:
            match = game.get_cur_lft().match_lft(tile)
            if match:
                game.place_lft(tile, match)
                self.__tiles.remove(tile)
                return

            match = game.get_cur_rgt().match_rgt(tile)
            if match:
                game.place_rgt(tile, match)
                self.__tiles.remove(tile)
                return
            
        