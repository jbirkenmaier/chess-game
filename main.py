import function_library as fl
import matplotlib.pyplot as plt

starting_position = fl.setup()
current_position = starting_position

while True:
    fl.create_board('purple','white','purple','black',40,20, current_position)
    piece = input('Enter piece')
    start = fl.user_to_machine_translation(input('Enter start'))
    target = fl.user_to_machine_translation(input('Enter target'))
    for element in current_position:
        if element.name == piece and element.position==start:
            element.position=target
    
            



