import csv
import sqlite3
queryDict = {1: "id",
             2: "media_type",
             3: "name",
             4: "short_name",
             5: "long_description",
             6: "short_description",
             7: "created_at",
             8: "updated_at",
             9: "review_url",
             10: "review_score",
             11: "slug",
             12: "genres",
             13: "created_by",
             14: "published_by",
             15: "franchises",
             16: "Regions"}

connection = sqlite3.connect('reviews.db')
c = connection.cursor()
c.execute("SELECT * FROM reviews")
result = c.fetchall()
endProgram = False

# sanitizing: dealing with unwanted characters/strings
def sanitize_database():
    with open('codefoobackend_cfgames.csv', "r", encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            if row[0] == "id":
                continue
            rowContainer = []
            for currentRow in row:
                currentRow = currentRow.replace("\"", "\'").replace("<p>", "".strip())
                rowContainer.append(currentRow)
            executeCommand = ("UPDATE reviews SET media_type = \"" + rowContainer[1] +
                              "\", name = \"" + rowContainer[2] +
                              "\", short_name = \"" + rowContainer[3] +
                              "\", long_description = \"" + rowContainer[4] +
                              "\", short_description = \"" + rowContainer[5] +
                              "\", created_at = \"" + rowContainer[6] +
                              "\", updated_at = \"" + rowContainer[7] +
                              "\", review_url = \"" + rowContainer[8] +
                              "\", review_score = \"" + rowContainer[9] +
                              "\", slug = \"" + rowContainer[10] +
                              "\", genres = \"" + rowContainer[11] +
                              "\", created_by = \"" + rowContainer[12] +
                              "\", published_by = \"" + rowContainer[13] +
                              "\", franchises = \"" + rowContainer[14] +
                              "\", Regions = \"" + rowContainer[15] + "\"" + " WHERE id = " + "\"" + rowContainer[
                                  0] + "\"" + ";")
            # print(executeCommand)
            c.execute(executeCommand)

sanitize_database()

class QueryEngine():
    # orders the list by descending or ascending value
    def __order_by__(self, executeString):
        print("Do you want to sort the query (y/n)?")
        currentInput = input()
        if currentInput == "y":
            # take user input and then select a category
            print("Please select a category to sort by (1-17):\n" +
                  "1. id\n" +
                  "2. media type\n" +
                  "3. name\n" +
                  "4. short name\n" +
                  "5. long description\n" +
                  "6. short description\n" +
                  "7. created at\n" +
                  "8. updated at\n" +
                  "9. review url\n" +
                  "10. review score\n" +
                  "11. slug\n" +
                  "12. genre\n" +
                  "13. created by\n" +
                  "14. published by\n" +
                  "15. franchises\n" +
                  "16. regions\n" +
                  "17. cancel\n")
            currentInput = input()
            while not currentInput.isnumeric():
                print("Error, input is not a number (1-17). Please Enter a digit in the range (1-17):")
                currentInput = input()
            currentInput = int(currentInput)
            if currentInput == 17:
                return executeString
            if currentInput == 1 or currentInput == 10:
                executeString += "ORDER BY CAST(" + queryDict.get(currentInput) + " AS INTEGER)"
            else:
                executeString += "ORDER BY " + queryDict.get(currentInput)
            print("Sort by ascending or descending (a/d):")
            sortInput = input()
            if sortInput == "a":
                executeString += " ASC "
            elif sortInput == "d":
                executeString += " DESC "
            else:
                print("invalid input: " + sortInput + " defaulting to ascending order")
                executeString += " ASC "
        return executeString

    # limits the range of the search query
    def __limit_range__(self, executeString):
        print("Do you want to limit the range? (y/n)")
        userAnswer = input()
        if userAnswer == "y":
            print("what should the limit be?")
            rangeInput = input()
            if rangeInput.isnumeric():
                executeString += " LIMIT " + rangeInput
            else:
                print("Invalid limit input, default to all")
        else:
            print("Default to all")
        return executeString

    # gets a set of queries
    def get_all_queries(self):
        queryList = []
        print("Please select what the search query should display (1-17):\n" +
              "1. id\n" +
              "2. media type\n" +
              "3. name\n" +
              "4. short name\n" +
              "5. long description\n" +
              "6. short description\n" +
              "7. created at\n" +
              "8. updated at\n" +
              "9. review url\n" +
              "10. review score\n" +
              "11. slug\n" +
              "12. genre\n" +
              "13. created by\n" +
              "14. published by\n" +
              "15. franchises\n" +
              "16. regions\n" +
              "17. done\n")

        queryDisplay = input()
        while not queryDisplay.isnumeric():
            print("Please enter a number from 1-17")
            queryDisplay = input()
        queryDisplay = int(queryDisplay)

        while queryDisplay != 17:
            if 1 <= queryDisplay <= 16:
                print("Search query added: " + queryDict.get(queryDisplay))
                if not queryDict.get(queryDisplay) in queryList:
                    queryList.append(queryDict.get(queryDisplay))
                print(queryList)
            else:
                print(str(queryDisplay) + " is out of bounds (1-17)")
            queryDisplay = input()
            while not queryDisplay.isnumeric():
                print("Please enter a number from 1-17")
                queryDisplay = input()
            queryDisplay = int(queryDisplay)

        queryLength = len(queryList)
        if queryLength == 0:
            return
        executeString = "SELECT "
        for query in queryList:
            executeString += query + ", "
        executeString = executeString[:-2]
        executeString += " FROM reviews"
        c.execute(executeString)
        print(queryList)
        for row in c.fetchall():
            x = 0
            queryRow = ""
            while x < queryLength:
                queryRow += row[x]
                if x + 1 < queryLength:
                    queryRow += ", "
                x += 1
            print(queryRow)
        print()

    # gets a specific query
    def get_specific_query(self):
        print("Please select a query to search in (1-17):\n" +
              "1. id\n" +
              "2. media type\n" +
              "3. name\n" +
              "4. short name\n" +
              "5. long description\n" +
              "6. short description\n" +
              "7. created at\n" +
              "8. updated at\n" +
              "9. review url\n" +
              "10. review score\n" +
              "11. slug\n" +
              "12. genre\n" +
              "13. created by\n" +
              "14. published by\n" +
              "15. franchises\n" +
              "16. regions\n" +
              "17. cancel\n")
        userInput = input()
        if not userInput.isnumeric():
            print("Error, invalid input: " + userInput)
            return

        userInput = int(userInput)
        if 1 <= userInput <= 16:
            print("Please enter a term to search for: ")
            term = input()
            executeString = "SELECT * FROM reviews WHERE " + queryDict.get(userInput) + " = " + "\"" + term + "\""
            if userInput == 12 or userInput == 13 or userInput == 14 or userInput == 15 or userInput == 16:
                executeString = "SELECT * FROM reviews WHERE " + queryDict.get(userInput) + " = " + "\"{" + term + "}\""

            executeString = QueryEngine.__order_by__(self, executeString)
            executeString = QueryEngine.__limit_range__(self, executeString)

            c.execute(executeString)
            for row in c.fetchall():
                counter = 1
                for column in row:
                    print(queryDict.get(counter) + ": " + column)
                    counter += 1
                print()
        else:
            if userInput == 17:
                print("Returning to the main program")
            else:
                print("Invalid input")
        print()

    # displays the full database
    def display_database(self):
        for row in result:
            print(row)
