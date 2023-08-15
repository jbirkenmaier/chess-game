import matplotlib.pyplot as plt

'''
white:
♔
♕
♖
♗
♘
♙
black
♚
♛
♜
♝
♞
♟︎
'''

piece_shorts = ['rw','nw','bw','qw','kw','bw','nw','rw','pw','pw','pw','pw','pw','pw','pw','pw','rb','nb','bb','qb','kb','bb','nb','rb','pb','pb','pb','pb','pb','pb','pb','pb']

piece_starting_positions =['a1','b1','c1','d1','e1','f1','g1','h1','a2','b2','c2','d2','e2','f2','g2','h2','a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7']

chars = ['a','b','c','d','e','f','g','h']
nums = ['1','2','3','4','5','6','7','8']

def setup():
    initialize_pieces = [piece(piece_shorts[i][0],piece_starting_positions[i],piece_shorts[i][1]) for i in range(len(piece_starting_positions))]
    return initialize_pieces

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
        self.character

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
            
            if self.color == 'w':
                self.character = '♘'
            if self.color == 'b':
                self.character = '♞'
                
        if name == 'p': #pawn
            if self.color == 'w':
                self.character = '♙'
                list_of_powers=[[coordinate_x,coordinate_y+1],
                                [coordinate_x+1,coordinate_y+1],
                                [coordinate_x-1,coordinate_y+1]
                                ]
                if self.position[1] == '1':
                    list_of_powers.append([coordinate_x,coordinate_y+2])

            if self.color == 'b':
                self.character = '♟'
                list_of_powers=[[coordinate_x,coordinate_y-1],
                                [coordinate_x+1,coordinate_y-1],
                                [coordinate_x-1,coordinate_y-1]
                                ]
                if self.position[1] == '6':
                    list_of_powers.append([coordinate_x,coordinate_y-2])
                    
        if name == 'r':
            list_of_powers=[]
            to_right=[[coordinate_x+i, coordinate_y] for i in range(1,8-coordinate_x)] #to the right
            to_left =[[coordinate_x-i, coordinate_y] for i in range(1,coordinate_x+1)]#to the left
            up = [[coordinate_x, coordinate_y+i] for i in range(1,8-coordinate_y)]#up
            down =[[coordinate_x, coordinate_y-i] for i in range(1,coordinate_y+1)]#down
            for element in to_right:
                list_of_powers.append(element)
            for element in to_left:
                list_of_powers.append(element)
            for element in up:
                list_of_powers.append(element)
            for element in down:
                list_of_powers.append(element)

            if self.color == 'w':
                self.character = '♖'
            if self.color == 'b':
                self.character = '♜'

        if name == 'b':
            list_of_powers=[]
            upper_right=[[coordinate_x+i, coordinate_y+i] for i in range(1,8-coordinate_x)]
            upper_left=[[coordinate_x-i, coordinate_y+i] for i in range(1,8-coordinate_x)]
            lower_right=[[coordinate_x+i, coordinate_y-i] for i in range(1,8-coordinate_x)]
            lower_left=[[coordinate_x-i, coordinate_y-i] for i in range(1,8-coordinate_x)]
            for element in upper_right:
                list_of_powers.append(element)
            for element in upper_left:
                list_of_powers.append(element)
            for element in lower_right:
                list_of_powers.append(element)
            for element in lower_left:
                list_of_powers.append(element)

            if self.color == 'w':
                self.character = '♗'
            if self.color == 'b':
                self.character = '♝'
                
        if name == 'q':
            list_of_powers=[]
            to_right=[[coordinate_x+i, coordinate_y] for i in range(1,8-coordinate_x)] #to the right
            to_left =[[coordinate_x-i, coordinate_y] for i in range(1,coordinate_x+1)]#to the left
            up = [[coordinate_x, coordinate_y+i] for i in range(1,8-coordinate_y)]#up
            down =[[coordinate_x, coordinate_y-i] for i in range(1,coordinate_y+1)]#down
            upper_right=[[coordinate_x+i, coordinate_y+i] for i in range(1,8-coordinate_x)]
            upper_left=[[coordinate_x-i, coordinate_y+i] for i in range(1,8-coordinate_x)]
            lower_right=[[coordinate_x+i, coordinate_y-i] for i in range(1,8-coordinate_x)]
            lower_left=[[coordinate_x-i, coordinate_y-i] for i in range(1,8-coordinate_x)]
            for element in to_right:
                list_of_powers.append(element)
            for element in to_left:
                list_of_powers.append(element)
            for element in up:
                list_of_powers.append(element)
            for element in down:
                list_of_powers.append(element)
            for element in upper_right:
                list_of_powers.append(element)
            for element in upper_left:
                list_of_powers.append(element)
            for element in lower_right:
                list_of_powers.append(element)
            for element in lower_left:
                list_of_powers.append(element)

            if self.color == 'w':
                self.character = '♕'
            if self.color == 'b':
                self.character = '♛'
                
        if name == 'k':
            list_of_powers=[[coordinate_x,coordinate_y+1], 
                            [coordinate_x+1,coordinate_y+1],
                            [coordinate_x-1,coordinate_y+1],
                            [coordinate_x+1,coordinate_y],
                            [coordinate_x-1,coordinate_y],
                            [coordinate_x-1,coordinate_y-1],
                            [coordinate_x,coordinate_y-1],
                            [coordinate_x+1,coordinate_y-1]
                            ]
            if self.color == 'w':
                self.character = '♔'
            if self.color == 'b':
                self.character = '♚'
                
        return list_of_powers


            

    def translate_position(self, position): #translate from user input
        for count, letter in enumerate(self.characters):
            if letter == position[0]:
                return '%s%s'%(count,str(int(position[1])-1))

    def retranslate_position(self, position): #translate from machine output
        return '%s%s'%(self.characters[int(position[0])],self.numbers[int(position[1])])

    def check_if_allowed(self, list_target_positions):
        legal_target_positions = [element for element in list_target_positions if (int(element[0])>=0 and int(element[1]) >=0) and (int(element[0])<=7 and int(element[1]) <=7)]
        legal_target_positions = ['%i%i'%(element[0],element[1]) for element in legal_target_positions]
        self.num_of_possible_moves = len(legal_target_positions)
        return legal_target_positions


def user_to_machine_translation(position): #translate from user input
    for count, letter in enumerate(chars):
        if letter == position[0]:
            return '%s%s'%(count,str(int(position[1])-1))

def machine_to_user_translation(position): #translate from machine output
    return '%s%s'%(chars[int(position[0])],nums[int(position[1])])           
            
def possible_moves(piece):
    return [piece.retranslate_position(piece.capability[i]) for i in range(piece.num_of_possible_moves)]

def create_board(first_color,second_color,third_color,piece_color, piece_size, square_size, current_position):
    plt.ion()
    fig,ax = plt.subplots()

    for element in current_position:
        ax.text(float(element.position[0])*square_size, float(element.position[1])*square_size,element.character, fontsize=piece_size, color=piece_color)

    for j in range(0,8):
        if j%2 ==0:
            for i in range(0,8,2):
                rectangle = plt.Rectangle((square_size*i,j*square_size), square_size, square_size, fc=first_color)
                plt.gca().add_patch(rectangle)
                rectangle = plt.Rectangle((square_size*i+square_size,j*square_size), square_size, square_size, fc=second_color,ec=third_color)
                plt.gca().add_patch(rectangle)
        else:
            for i in range(0,8,2):
                rectangle = plt.Rectangle((square_size*i+square_size,j*square_size), square_size, square_size, fc=first_color)
                plt.gca().add_patch(rectangle)
                rectangle = plt.Rectangle((square_size*i,j*square_size), square_size, square_size, fc=second_color,ec=third_color)
                plt.gca().add_patch(rectangle)
            
    plt.axis('scaled')
    move_color = 'w'
    
    while True:
        print(move_color, ' to move')
        check_moves = True
        illegal = False
        fig.canvas.draw()
        fig.canvas.flush_events()
        piece = input('Enter piece')
        start = user_to_machine_translation(input('Enter start'))
        target = user_to_machine_translation(input('Enter target'))

        for element in current_position:
            if check_moves == True:
                for obj in current_position:
                    if obj.position == target and obj.color == move_color: #taking pieces of the same color is illegal
                            print('Illegal move: %s takes the %s %s on %s, enter a different move' %(move_color, obj.color, obj.character, machine_to_user_translation(obj.position)))
                            illegal = True

                    if obj.name == piece and  obj.name == 'p' and obj.position == start and target == obj.capability[0] and target in [element.position for element in current_position]:
                        print('Illegal move')
                        illegal = True
                    if obj.name == piece and  obj.name == 'b' and obj.position == start and target in obj.capability and [element.position
                                                                                                                          for element in current_position
                                                                                                                          if element.position in obj.capability and int(element.position[0])**2+int(element.position[1])**2 < int(target[0])**2+int(target[1])**2]!=[]:
                        print('Illegal move')
                        illegal = True

                        
                    if obj.position == target and obj.color != move_color and illegal == False:
                        for text_object in plt.gca().texts:
                            if  text_object.get_text() == obj.character and text_object.get_position()[0] == float(target[0])*square_size and text_object.get_position()[1] == float(target[1])*square_size:
                                text_object.set_text('')
                                new_position=(9*square_size,9*square_size)
                                text_object.set_position(new_position)


                        
                check_moves = False
                    

            if illegal == True:
                break

            #print(element.name, piece, element.position, start)
            if element.name == piece and element.position==start:
                if target in element.capability:
                    element.position=target
                    piece_character = element.character
                    print(piece_character)
                    element.position_user=element.retranslate_position(element.position)
                    element.capability = element.check_if_allowed(element.powers(element.name, element.position))
                    if move_color == 'w':
                        move_color = 'b'
                    else:
                        move_color = 'w'
                else:
                    print('illegal move')
                    print('possible moves with this piece: ',machine_to_user_translation(element.capability))
                    illegal = True
                    break

        if illegal == False:
            for text_object in plt.gca().texts:
                if  text_object.get_text() == piece_character and text_object.get_position()[0] == float(start[0])*square_size and text_object.get_position()[1] == float(start[1])*square_size:
                    new_position=(float(target[0])*square_size,float(target[1])*square_size)
                    text_object.set_position(new_position)

    

    
