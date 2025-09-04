import ast
import sys

class SaveLoadSystem:
    file_name = 'high_scores.txt'

    def save_value(input_value, filename):
        with open(filename, 'w') as f:
            f.write(input_value)

    def load_value(filename):
        with open(filename, 'r') as f:
            read = f.read()
        return read

    try: 
        values = ast.literal_eval(load_value(file_name))
        print('Past scores: ', values)
    except: 
        print('Creating a new file...')
        values = {}

def running_save_load_system(values={}, file_name='high_score.txt',save_value=SaveLoadSystem.save_value):
    while True:
        user_input = input('Which score would you like to save? Freeplay or Time Limit? Or type "none" to exit. ')
        if user_input == 'freeplay':
            values["freeplay"] = input("Enter your Freeplay score here: ")
            save_value(str(values), file_name)
            user_input = input('Would you like to save another score? (yes/no) ')
            if user_input == 'yes':
                user_input = input('Enter your Time Limit score here: ')
                save_value(str(values), file_name)
            elif user_input == 'no':
                print(values)
                print("Your scores have been saved! Play again to beat your high scores!")
                sys.exit()
            else:
                print('Unknown command...')
        elif user_input == 'time limit':
            values["time limit"] = input("Enter your Time Limit score here: ")
            save_value(str(values), file_name)
            user_input = input('Would you like to save another score? (yes/no) ')
            if user_input == 'yes':
                input("Enter your Freeplay score here: ")
                save_value(str(values), file_name)
            elif user_input == 'no':
                print(values)
                print("Your scores have been saved! Play again to beat your high scores!")
                sys.exit()
            else:
                print('Unknown command...')
        elif user_input == 'none':
            print(values)
            print("Your scores have been saved! Play again to beat your high scores!")
            sys.exit()

        else:
            print('Unknown command...')

        
