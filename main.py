import function_library as fl

knight = fl.piece('n','d4')

print(knight.position)
print(knight.position_user)
print([knight.retranslate_position(knight.capability[i]) for i in range(knight.num_of_possible_moves)])
print(knight.num_of_possible_moves)
