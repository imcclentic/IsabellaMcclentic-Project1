
def get_data():
    my_file = open('nationsPop.txt', 'r')
    lines = my_file.readlines()
    country_data = []
    for country_line in lines:
        country_line = country_line.strip()
        nation_pop_list = country_line.split(',')
        pop_dictionary = {'Name': nation_pop_list[0],
                          'Population': int(nation_pop_list[1]),
                          'Change': float(nation_pop_list[2])}
        country_data.append(pop_dictionary)
    return country_data

def print_menu():
    print("========Please select from the following========")
    print("[1] Find the largest country")
    print("[2] Find the smallest country")
    print("[3] Add a new country")
    print("[4] Quit")
    print("================================================")

def main():
    country_list = get_data()
    while True:
        print_menu()
        user_choice = input("Please enter the number of your selection:")

main()

#Parameters go in the ()
#Arguments are sent to a function when you call them
#passing several parameters to functions
    #by default the first argument gets copied into the first parameter, not in the order they appear in def main -
    #those are called positional arguments
    #Arcade is a funation that had multiple parameters
    #default values -- parameter = default value (does not have to be included in argument)
#keyword arguments - you can send an srgument in any order as long as the parameter is assigned a name
# ^ parameter_name=value

#mutable vs immutable arguments
    #immutable - cannot be changed when being called by a function
