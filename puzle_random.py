import random

pieces = [
    ["-B2", "+W1", "+B1", "-W2"],
    ["-B1", "+B2", "+B1", "+W1"],
    ["-B1", "-W2", "+B2", "+W1"],
    ["+B2", "+W2", "-B1", "+W1"],
    ["+B1", "-W1", "-B2", "-W2"],
    ["+B2", "+W1", "-B1", "+W2"],
    ["+B1", "-W1", "+W2", "+B2"],
    ["-W2", "+W2", "-B2", "-B1"],
    ["+B2", "-W2", "+W1", "-W1"]
    ]

successful_combinations = 0
combination_count = 0


def rotate(piece):
    last_item_from_list = piece.pop()
    piece.insert(0, last_item_from_list)
    return piece


def compatibility_check(layout, piece, n):
    surrounded_pieces = check_surroundings(n)
    if len(surrounded_pieces) == 1 and n != 3 and n != 6:
        previous_piece = layout[surrounded_pieces[0]]
        left_bird = previous_piece[2]
        main_bird_left = piece[0]
        if left_bird[0] != main_bird_left[0] and left_bird[1] == main_bird_left[1] and left_bird[2] == main_bird_left[2]:
            return True
        else:
            return False
    elif len(surrounded_pieces) == 1:
        top_piece = layout[surrounded_pieces[0]]
        top_bird = top_piece[3]
        main_bird_top = piece[1]
        if top_bird[0] != main_bird_top[0] and top_bird[1] == main_bird_top[1] and top_bird[2] == main_bird_top[2]:
            return True
        else:
            return False
    else:
        previous_piece = layout[surrounded_pieces[1]]
        top_piece = layout[surrounded_pieces[0]]
        left_bird = previous_piece[2]
        top_bird = top_piece[3]
        main_bird_left = piece[0]
        main_bird_top = piece[1]
        if left_bird[0] != main_bird_left[0] and left_bird[1] == main_bird_left[1] and left_bird[2] == main_bird_left[2] and top_bird[0] != main_bird_top[0] and top_bird[1] == main_bird_top[1] and top_bird[2] == main_bird_top[2]:
            return True
        else:
            return False


def check_surroundings(n):
    surrounded_pices = []
    if n%3 == 0 and n != 0:
        surrounded_pices.append(n - 3)
    elif n == 1 or n == 2:
        surrounded_pices.append(n - 1)
    elif n != 0:
        surrounded_pices.append(n - 3)
        surrounded_pices.append(n - 1)
    return surrounded_pices

for _ in range (10000):
    for piece in pieces:
        continue_to_next_piece = True
        for i in range(4):                                 # enables the first piece to rotate 4 times
            piece = rotate(piece)
            layout = [[], [], [], [], [], [], [], [], []]  # empties previous layout
            new_pieces = pieces.copy()                     # duplicates existing pieces
            random.shuffle(new_pieces)
            if piece != pieces[0]:
                removed_piece = new_pieces.pop(new_pieces.index(piece))
                new_pieces.insert(0, removed_piece)                         # shuffles around the pieces so the layout[0] piece would be first
            n = 0
                                                                    # resets the list item index
            layout[0] = piece                                               # changes the piece in layout[0]
            for _ in range(i):
            # print(i)
                layout[0] = rotate(layout[0])                                  # rotates the piece depending on var: i
            # print(layout[0])
            for space in layout:
                if not continue_to_next_piece:
                    break
                unsucessful_attempts = 0   
                if len(space) == 0:                                         # works on every space except the first one (already has been set)
                    layout[n] = new_pieces[n]                               # fills empty spaces in layout with pieces (works if pieces are rearranged)
                    for _ in range(4):
                        new_pieces[n] = rotate(new_pieces[n])                           # rotates the piece for max. 4 times
                        if compatibility_check(layout, layout[n], n) or n == 0: # checks if the piece matches it's surroundings
                            # layout[n] = new_pieces[n]
                            if layout[8] != []:
                                print(len(layout))
                                successful_combinations += 1
                                print(f"Nr. {successful_combinations} | {layout}")
                                if layout == pieces:
                                    print("!!!!!UP!!!!!!")
                            break
                        else:
                            unsucessful_attempts += 1
                            if unsucessful_attempts >= 4:
                                continue_to_next_piece = False
                                break
                n += 1
                combination_count += 1

print(combination_count)