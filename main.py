word = str(input("Type in the word to guess here\n")).upper().strip()
blanks = []
counter = len(word)
times = 5
game = True
found = False

# Make the blanks
for letter in range(len(word)):
    blanks.append("_")

# Create empty lines to prevent the people guessing from seeing the inputted word
for i in range(15):
    print("\n")

# Display how many blanks there are in the word
print(*blanks)


def not_found(times):
    if not found:
        times_left = times - 1
        print("\n" + str(times_left) + " times left")
        return times_left
    else:
        return times


def game_end():
    if counter == 0:
        print("\nYou win! The word was " + word)
        return False
    elif times == 0:
        print("\nYou lose! The word was " + word)
        return False
    else:
        return True


while game:
    guess = str(input("\nType in your letter guess here\n")).upper().strip()
    for letter in range(len(word)):
        if guess == word[letter]:
            blanks.insert(letter, word[letter])
            blanks.pop(letter+1)
            counter -= 1
            found = True

    # The asterisk before "blanks" makes it so the list is printed out as a string with blanks between each element
    print(*blanks)
    times = not_found(times)
    game = game_end()
    found = False
