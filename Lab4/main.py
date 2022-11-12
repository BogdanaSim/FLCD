from fa import FiniteAutomaton


def print_menu():
    print("Menu")
    print("1 - Get the set of states")
    print("2 - Get the alphabet")
    print("3 - Get the transitions")
    print("4 - Get the initial state")
    print("5 - Get the set of final states")
    print("6 - Check if is dfa")
    print("7 - Check if sequence is accepted")
    print("8 - Exit")


if __name__ == '__main__':
    fa = FiniteAutomaton("FA.in")
    done = False
    while not done:
        print_menu()
        option = input("Choose an option:")

        if option == "1":
            print('Q = {' + ', '.join([str(x) for x in fa.Q]) + '}')
        elif option == "2":
            print('E = {' + ', '.join([str(x) for x in fa.E]) + '}')
        elif option == "3":
            T = ""
            for (origin, path) in fa.T.keys():
                T += "(" + str(origin) + "," + str(path) + ")" + "->" + str(fa.T[(origin, path)]) + "\n"

            print('T = {\n' + T + '}')
        elif option == "4":
            # print(fa.q0)
            print("q0 = {"+str(fa.q0)+"}")
        elif option == "5":
            print('F = {' + ', '.join([str(x) for x in fa.F]) + '}')
        elif option == "6":
            print(fa.is_dfa())
        elif option == "7":

            if fa.is_dfa():
                sequence = input("Enter sequence: ")
                print(fa.is_accepted_by_fa(sequence))
            else:
                print("It is not an dfa!")
        elif option == "8":
            done = True
        else:
            print("This option does not exist!")





