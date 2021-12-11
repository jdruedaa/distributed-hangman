

def draw_base_circle(allowed_errors):
    print("  |                 /-----\ ")
    print("  |                / _   _ \ ")
    if allowed_errors==0:
        print("  |                \   x   / ")
    else:
        print("  |                \   O   / ")
    print("  |                  -----")

def draw_hands():

    print("  |                    |")
    print("  |                /===|===\ ")
    print("  |               /    |    \ ")
    for i in range(0, 2):
        print("  |                    |")
def draw_stick():
    for i in range(0, 5):
        print("  |                    |")
def draw_legs():
    print("  |              /===========\ ")
    print("  |             /             \ ")

def draw_hangman(allowed_errors):
    print("   _", end="")
    for i in range(0, 10):
        print(" _", end="")
    print("")
    print("  |                    |")
    # draw the base only
    if allowed_errors==4:
        for i in range(0, 3):
            print("  |")
    #draw circle
    elif allowed_errors==3:
        draw_base_circle(allowed_errors)
    #draw stick
    elif allowed_errors == 2:
        draw_base_circle(allowed_errors)
        draw_stick()
    #draw hands
    elif allowed_errors == 1:
        draw_base_circle(allowed_errors)
        draw_hands()
    else:
        draw_base_circle(allowed_errors)
        draw_hands()
        draw_legs()

    for i in range(0,2):
        print("  |")



def print_solved(word,correct_guesses):
    wordTillNow=""
    for letter in word:
        if letter.lower() in correct_guesses:
            wordTillNow+=letter+" "

        else:
            wordTillNow += "_ "
    return wordTillNow
def process_word(l,word,correct_guesses,allowed_errors):
    for i in range(0,len(l)):
        returned_value=process_letter(l[i], word, correct_guesses, allowed_errors)
    if returned_value<allowed_errors:
        allowed_errors -= 1
    return (allowed_errors)




def process_letter(l,word,correct_guesses,allowed_errors):
    for letter in word:
        if letter.lower()==l:
            correct_guesses.append(l)
            return allowed_errors
    allowed_errors-=1
    return allowed_errors

def solved(word,correct_guesses):

    for letter in word:
        if letter.lower() not in correct_guesses:
            return False
    return True

#_________________________________________________________________testing______________________________
# def main():
#     word="Andrew"
#     correct_guesses=[]
#     allowed_errors: int = 4  # "circle,body,hands,legs"
#     while solved(word,correct_guesses)==False:
#         print('guess a letter:')
#         x = input()
#         allowed_errors=process_word(x,word,correct_guesses,allowed_errors)
#         if allowed_errors==0:
#             draw_hangman(allowed_errors)
#             print("GAME OVER")
#             return 0
#         draw_hangman(allowed_errors)
#         print(correct_guesses)
#         print(allowed_errors)
#         print(print_solved(word,correct_guesses))
#
#
# main()