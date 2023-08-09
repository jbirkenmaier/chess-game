import function_library as fl


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


print('⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛')
input()

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
