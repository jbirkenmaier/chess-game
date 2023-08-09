import function_library as fl

knight = fl.piece('n','f7')
pawn = fl.piece('p','d6')

print(pawn.position)
print(pawn.position_user)

move_options = fl.possible_moves(pawn)

print(move_options)
print(len(move_options))
