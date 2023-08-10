import function_library as fl
import matplotlib.pyplot as plt

starting_position = fl.setup()
current_position = starting_position

print(current_position[0].name)
print(current_position[0].color)


knight = fl.piece('n','f7','w')
pawn = fl.piece('k','d6','b')

print(pawn.position)
print(pawn.position_user)

move_options = fl.possible_moves(pawn)

print(move_options)
print(len(move_options))

while True:
    fl.create_board('purple','white','purple','black',40,20, current_position)
    input('Enter_move')



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
