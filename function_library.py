
piece_shorts = ['rw','nw','bw','qw','kw','bw','nw','rw','pw','pw','pw','pw','pw','pw','pw','pw','rb','nb','bb','qb','kb','bb','nb','rb','pb','pb','pb','pb','pb','pb','pb','pb']

piece_starting_positions =['a1','b1','c1','d1','e1','f1','g1','h1','a2','b2','c2','d2','e2','f2','g2','h2','a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7']



def setup():
    pieces = [piece(element
class piece():

    def __init__(self, name, position, color):
        self.color = color
        self.characters = ['a','b','c','d','e','f','g','h']
        self.numbers = ['1','2','3','4','5','6','7','8']
        self.name=name
        self.position=self.translate_position(position)
        self.position_user=self.retranslate_position(self.position)
        self.capability = self.check_if_allowed(self.powers(self.name, self.position))
        self.num_of_possible_moves

    def powers(self, name, position):
        coordinate_x = int(position[0])
        coordinate_y = int(position[1])
        if name == 'n': #knight
            list_of_powers=[[coordinate_x+2,coordinate_y+1],
                            [coordinate_x+2,coordinate_y-1],
                            [coordinate_x-2,coordinate_y+1],
                            [coordinate_x-2,coordinate_y-1],
                            [coordinate_x-1,coordinate_y+2],
                            [coordinate_x+1,coordinate_y+2],
                            [coordinate_x-1,coordinate_y-2],
                            [coordinate_x+1,coordinate_y-2]
                            ]
        if name == 'p': #pawn
            list_of_powers=[[coordinate_x,coordinate_y+1],
                            [coordinate_x+1,coordinate_y+1],
                            [coordinate_x-1,coordinate_y+1]
                            ]
            #list_of_powers=[element for element in list_of_powers if 

        if name == 'r':
            pass
        if name == 'b':
            pass
        if name == 'q':
            pass
        if name == 'k':
            pass                            
        
        return list_of_powers


            

    def translate_position(self, position):
        for count, letter in enumerate(self.characters):
            if letter == position[0]:
                return '%s%s'%(count,str(int(position[1])-1))

    def retranslate_position(self, position):
        return '%s%s'%(self.characters[int(position[0])],self.numbers[int(position[1])])

    def check_if_allowed(self, list_target_positions):
        legal_target_positions = [element for element in list_target_positions if (int(element[0])>=0 and int(element[1]) >=0) and (int(element[0])<=7 and int(element[1]) <=7)]
        legal_target_positions = ['%i%i'%(element[0],element[1]) for element in legal_target_positions]
        self.num_of_possible_moves = len(legal_target_positions)
        return legal_target_positions
            
            
def possible_moves(piece):
    return [piece.retranslate_position(piece.capability[i]) for i in range(piece.num_of_possible_moves)]
