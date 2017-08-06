def watch_pyramid_from_the_side(characters=None):
    if characters == '':
        return('')
    if not characters:
        return(None)
    output = ''
    if not characters:
        return
    point = len(characters) - 1
    count = -1
    while True:
        if point == -1:
            break
        char = characters[point]
        count = count + 2
        view = ''
        for x in range(point):
            view += ' '
        for x in range(count):
            view = view + char
        for x in range(point):
            view += ' '
        output += view + '\n'
        point -= 1
    output = output[:-1]
    return(output)


def watch_pyramid_from_above(characters=None):
    if characters == '':
        return('')
    if not characters:
        return(None)
    point = len(characters)
    output = ''
    count = -1
    total_lane = point * 2 - 1
    hold = []
    off_set = -1
    view = ''
    flag = 0
    for x in characters:
        count += 2
    for x in range(total_lane):
        at = 0
        view = ''
        po = x
        if po >= point:
            po = x - 1
            po = point - po
        if flag == 0:
            for y in range(count):
                view += characters[at]
                if y + po + 1 >= count and at != 0:
                    at -= 1
                elif at < po and at < point - 1 and flag == 0:
                    at += 1
                if characters[at] is characters[-1]:
                    flag = 1
            if flag == 0:
                hold.append(view)
        elif flag == 1:
            view = hold[off_set]
            off_set -= 1
        output += view + '\n'
    output = output[:-1]
    return(output)


def count_visible_characters_of_the_pyramid(characters=None):
    if not characters:
        return(-1)
    total = 0
    count = -1
    for x in characters:
        count += 2
        temp_count = count
        if temp_count > 1:
            temp_count = ((temp_count - 2) * 4) + 4
        total += temp_count
    return(total)


def count_all_characters_of_the_pyramid(characters):
    if not characters:
        return(-1)
    total = 0
    count = -1
    for x in characters:
        count += 2
        total += count**2
    return(total)

