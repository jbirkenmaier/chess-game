class piece():

    def __init__(self, name, position):
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
            print('CALL')
            list_of_powers=[[coordinate_x,coordinate_y+1],
                            [coordinate_x+1,coordinate_y+1],
                            [coordinate_x-1,coordinate_y+1]
                            ]

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
            
            
