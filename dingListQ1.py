# David Ding
# ICS3U1
# May 31st 2017
# Auto-complete software with a constant refresh

# IMPORTS
import pygame

# ========================================= VARIABLE DECLARATION AND INITIALIZATION
pygame.init()

# ------------------- Constants
# MAXX is the maximum x-size of the window
# MAXY is the maximum y-size of the window  Note: Strange resolution because it is 9:16 aspect ratio for 600 pixels
# SIZE is the size of the window as a duple
MAXX = 600
MAXY = 1067
SIZE = (MAXX, MAXY)

# -------------------Variable Declaration
# screen is the pygame screen
# keyboard is the picture of the Android keyboard that was imported
# running is the boolean variable for the game loop
# myClock is the clock variable to set frame rate
# file is the file that is to be opened
# data is the raw data array before checking for repeated words
# words is the processed data array that holds the unique words in the text
# frequency is what stores the frequency of the words, related lists with words
# sentence holds the entire string
# next_word is what stores whether or not the user wants to insert a new word
# curr_word is the current word that is currently being typed
screen = pygame.display.set_mode(SIZE)
keyboard = pygame.image.load("keyboard.png")
running = True
myClock = pygame.time.Clock()
file = open("dict.txt", "r")
data = []
words = []
frequency = []
sentence = ""
next_word = False
curr_word = ""

# Variables for if the character is held down, used to avoid repeating inputs... fairly self-explanatory
pressed_a = False
pressed_b = False
pressed_c = False
pressed_d = False
pressed_e = False
pressed_f = False
pressed_g = False
pressed_h = False
pressed_i = False
pressed_j = False
pressed_k = False
pressed_l = False
pressed_m = False
pressed_n = False
pressed_o = False
pressed_p = False
pressed_q = False
pressed_r = False
pressed_s = False
pressed_t = False
pressed_u = False
pressed_v = False
pressed_w = False
pressed_x = False
pressed_y = False
pressed_z = False
pressed_backspace = False
pressed_space = False
pressed_period = False

# ------------------- Fonts
# mainFont is the main font that is used in this program
mainFont = pygame.font.SysFont("arial", 24)

# ------------------- Rectangles for the Keyboard Interface
# In order from left to right on the main screen
word1 = pygame.Rect(10, 400, 190, 50)
word2 = pygame.Rect(200, 400, 190, 50)
word3 = pygame.Rect(400, 400, 190, 50)

# ------------------ Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# ================================================== DEFINITIONS

# blit_body is the variable used to blit the text in paragraph form - borrowed from previous program (Unit_3_Assignment)
def blit_body(surface, pos, text, font):
    # ----- Local Variables
    # wheight is the word height
    # lines is an array for lines in the text
    # space_width is the space required for the given font to render a space character
    # x and y are the x and y coordinates of the current "cursor" to print out words
    # wrectangle is the width of the rectangle that the font.render renders
    # wwidth is the width of the word
    # MAX_WIDTH is the maximum width that the words can go to
    wheight = 0
    lines = [word.split(' ') for word in text.splitlines()]
    space_width = font.size(' ')[0]
    x, y = pos
    wrectangle, wwidth = None, None
    MAX_WIDTH = 550

    # ----- Main Logic of Definition
    # This loops through each line of text
    for word in lines:
        # This loops through each word in the lines
        for i in word:
            wrectangle = font.render(str(i), 0, WHITE)
            wwidth, wheight = wrectangle.get_size()
            if x + wwidth >= MAX_WIDTH:
                x = pos[0]
                y += wheight
            surface.blit(wrectangle, (x, y))
            x += wwidth + space_width
    x = pos[0]
    y += wheight

# ========================================= MAIN PROGRAM
# ------------------ Opening the file and reading lines
# This loop opens all the strings into a "raw data" array without processing anything
while True:
    line = file.readline()
    if line != "":
        data.append(line.strip().lower())
    else:
        break

# Parsing the raw data into lines and frequency of word
for word in data:
    # Only put the word into the processed array if it is the first occurrence of the word
    # Otherwise, update the frequency of the frequency array
    if word not in words:
        words.append(word)
        frequency.append(1)
    else:
        frequency[words.index(word)] += 1

# ------------------ Game Loop
while running:
    # Wipes the screen every frame and draws the "background"
    screen.fill(BLACK)
    screen.blit(keyboard, pygame.Rect(0, 0, 600, 1067))

    # Checks if the user wants to quit
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False

    # keys stores all the keys that the user presses
    keys = pygame.key.get_pressed()
    # Checking user input
    if keys[pygame.K_q]:
        pressed_q = True
    elif keys[pygame.K_w]:
        pressed_w = True
    elif keys[pygame.K_e]:
        pressed_e = True
    elif keys[pygame.K_r]:
        pressed_r = True
    elif keys[pygame.K_t]:
        pressed_t = True
    elif keys[pygame.K_y]:
        pressed_y = True
    elif keys[pygame.K_u]:
        pressed_u = True
    elif keys[pygame.K_i]:
        pressed_i = True
    elif keys[pygame.K_o]:
        pressed_o = True
    elif keys[pygame.K_p]:
        pressed_p = True
    elif keys[pygame.K_a]:
        pressed_a = True
    elif keys[pygame.K_s]:
        pressed_s = True
    elif keys[pygame.K_d]:
        pressed_d = True
    elif keys[pygame.K_f]:
        pressed_f = True
    elif keys[pygame.K_g]:
        pressed_g = True
    elif keys[pygame.K_h]:
        pressed_h = True
    elif keys[pygame.K_j]:
        pressed_j = True
    elif keys[pygame.K_k]:
        pressed_k = True
    elif keys[pygame.K_l]:
        pressed_l = True
    elif keys[pygame.K_z]:
        pressed_z = True
    elif keys[pygame.K_x]:
        pressed_x = True
    elif keys[pygame.K_c]:
        pressed_c = True
    elif keys[pygame.K_v]:
        pressed_v = True
    elif keys[pygame.K_b]:
        pressed_b = True
    elif keys[pygame.K_n]:
        pressed_n = True
    elif keys[pygame.K_m]:
        pressed_m = True
    elif keys[pygame.K_PERIOD]:
        pressed_period = True
    elif keys[pygame.K_BACKSPACE]:
        pressed_backspace = True
    elif keys[pygame.K_SPACE]:
        pressed_space = True
    keys = pygame.key.get_pressed()

    # Processes User Input - only add the letters to the current word if the button has been let go already
    if pressed_q and not keys[pygame.K_q]:
        curr_word += "q"
        pressed_q = False
    elif pressed_w and not keys[pygame.K_w]:
        curr_word += "w"
        pressed_w = False
    elif pressed_e and not keys[pygame.K_e]:
        curr_word += "e"
        pressed_e = False
    elif pressed_r and not keys[pygame.K_r]:
        curr_word += "r"
        pressed_r = False
    elif pressed_t and not keys[pygame.K_t]:
        curr_word += "t"
        pressed_t = False
    elif pressed_y and not keys[pygame.K_y]:
        curr_word += "y"
        pressed_y = False
    elif pressed_u and not keys[pygame.K_u]:
        curr_word += "u"
        pressed_u = False
    elif pressed_i and not keys[pygame.K_i]:
        curr_word += "i"
        pressed_i = False
    elif pressed_o and not keys[pygame.K_o]:
        curr_word += "o"
        pressed_o = False
    elif pressed_p and not keys[pygame.K_p]:
        curr_word += "p"
        pressed_p = False
    elif pressed_a and not keys[pygame.K_a]:
        curr_word += "a"
        pressed_a = False
    elif pressed_s and not keys[pygame.K_s]:
        curr_word += "s"
        pressed_s = False
    elif pressed_d and not keys[pygame.K_d]:
        curr_word += "d"
        pressed_d = False
    elif pressed_f and not keys[pygame.K_f]:
        curr_word += "f"
        pressed_f = False
    elif pressed_g and not keys[pygame.K_g]:
        curr_word += "g"
        pressed_g = False
    elif pressed_h and not keys[pygame.K_h]:
        curr_word += "h"
        pressed_h = False
    elif pressed_j and not keys[pygame.K_j]:
        curr_word += "j"
        pressed_j = False
    elif pressed_k and not keys[pygame.K_k]:
        curr_word += "k"
        pressed_k = False
    elif pressed_l and not keys[pygame.K_l]:
        curr_word += "l"
        pressed_l = False
    elif pressed_z and not keys[pygame.K_z]:
        curr_word += "z"
        pressed_z = False
    elif pressed_x and not keys[pygame.K_x]:
        curr_word += "x"
        pressed_x = False
    elif pressed_c and not keys[pygame.K_c]:
        curr_word += "c"
        pressed_c = False
    elif pressed_v and not keys[pygame.K_v]:
        curr_word += "v"
        pressed_v = False
    elif pressed_b and not keys[pygame.K_b]:
        curr_word += "b"
        pressed_b = False
    elif pressed_n and not keys[pygame.K_n]:
        curr_word += "n"
        pressed_n = False
    elif pressed_m and not keys[pygame.K_m]:
        curr_word += "m"
        pressed_m = False
    elif pressed_backspace and not keys[pygame.K_BACKSPACE]:
        if curr_word != "":
            curr_word = curr_word[0:len(curr_word)-1]
        else:
            sentence = sentence[0:len(curr_word)-1]
        pressed_backspace = False
    elif pressed_space and not keys[pygame.K_SPACE]:
        next_word = True
        pressed_space = False
    elif pressed_period and not keys[pygame.K_PERIOD]:
        curr_word += "."
        pressed_period = False

    # request is an array that stores the potential words from the list
    request = []

    # Cycles through all the words in the array "words"
    for ele in words:
        if curr_word == ele[0:len(curr_word)]:
            request.append([frequency[words.index(ele)], ele])
        request.sort(reverse=True)

    # If the user has pressed the space bar
    if next_word:
        # if there are no suggestions, add the next word
        if len(request) == 0:
            sentence += curr_word + " "
            curr_word = ""
        # If there are suggestions, add the first suggested word
        else:
            sentence += request[0][1] + " "
            curr_word = ""
        print(sentence)
        next_word = False

    # Finding words in the suggested words bar
    # If there are more than 3 options, take the first three
    if len(request) >= 3:
        # Display the next words in the autocomplete bar
        option1 = mainFont.render(request[1][1], 1, (255, 255, 255))
        option2 = mainFont.render(request[0][1], 1, (255, 255, 255))
        option3 = mainFont.render(request[2][1], 1, (255, 255, 255))
        screen.blit(option1, word1)
        screen.blit(option2, word2)
        screen.blit(option3, word3)
    # If there are less than 3
    else:
        # If it is empty, then simply display nothing
        if len(request) == 0:
            option1 = mainFont.render("", 1, (255, 255, 255))
            screen.blit(option1, word1)
        # If one word, then display the word in the middle
        elif len(request) == 1:
            option1 = mainFont.render(request[0][1], 1, (255, 255, 255))
            screen.blit(option1, word2)
        # If there are two words, display the first in the middle, second to the side
        elif len(request) == 2:
            option1 = mainFont.render(request[1][1], 1, (255, 255, 255))
            option2 = mainFont.render(request[0][1], 1, (255, 255, 255))
            screen.blit(option1, word1)
            screen.blit(option2, word2)

    # Final output
    out = mainFont.render(curr_word, 1, (255, 255, 255))
    screen.blit(out, pygame.Rect(50, 100, 100, 100))
    blit_body(screen, (50, 150), sentence, mainFont)

    # Update frames and flip
    myClock.tick(60)
    pygame.display.flip()

# Close file
file.close()
