import function_library as fl

knight = fl.piece('n','f7')
pawn = fl.piece('p','d8')

print(pawn.position)
print(pawn.position_user)

def possible_moves(piece):
    return [piece.retranslate_position(piece.capability[i]) for i in range(piece.num_of_possible_moves)]

move_options = possible_moves(knight)

print(move_options)
print(len(move_options))
