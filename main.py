import function_library as fl

knight = fl.piece('n','a8')

print(knight.position)
print(knight.position_user)
print(knight.retranslate_position(knight.capability))
