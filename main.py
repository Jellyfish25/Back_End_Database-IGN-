from QueryEngine import QueryEngine

# ********* MAIN PROGRAM **************
myQueryEngine = QueryEngine()
endProgram = False

while not endProgram:
    print("Please enter any of the following commands (1-10):\n" +
          "1. view all queries \n" +
          "2. search for a specific query\n" +
          "q. quit the program\n")
    userInput = input()
    if userInput == "1":
        myQueryEngine.get_all_queries()
    elif userInput == "2":
        myQueryEngine.get_specific_query()
    elif userInput == "q":
        endProgram = True
    else:
        print("Error: " + userInput + " is not a currently supported command!")

        
