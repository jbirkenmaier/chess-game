class piece():

    def __init__(self, name, position):
        self.characters = ['a','b','c','d','e','f','g','h']
        self.numbers = ['1','2','3','4','5','6','7','8']
        self.name=name
        self.position=self.translate_position(position)
        self.position_user=self.retranslate_position(self.position)
        self.capability = self.powers(self.name, self.position)

    def powers(self, name, position):
        coordinate_x = int(position[0])
        coordinate_y = int(position[1])
        list_of_powers =[]
        if name == 'n': #knight
            list_of_powers.append([coordinate_x+2,coordinate_y+1],
                                  [coordinate_x+2,coordinate_y-1],
                                  [coordinate_x-2,coordinate_y+1],
                                  [coordinate_x-2,coordinate_y-1],
                                  [coordinate_x-1,coordinate_y+2],
                                  [coordinate_x+1,coordinate_y+2],
                                  [coordinate_x-1,coordinate_y-2],
                                  [coordinate_x+1,coordinate_y-2]
                                  )

            

    def translate_position(self, position):
        for count, letter in enumerate(self.characters):
            if letter == position[0]:
                return '%s%s'%(count,str(int(position[1])-1))

    def retranslate_position(self, position):
        return '%s%s'%(self.characters[int(position[0])],self.numbers[int(position[1])])

    def check_if_allowed(self, 
                
            
