import function_library as fl


#starting_position = fl.setup()

#print(starting_position[0].name)
#print(starting_position[0].color)


#knight = fl.piece('n','f7','w')
pawn = fl.piece('r','d6','b')

print(pawn.position)
print(pawn.position_user)

move_options = fl.possible_moves(pawn)

print(move_options)
print(len(move_options))
