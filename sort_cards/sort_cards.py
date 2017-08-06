"""Sort crads"""


def sort_cards(card_list=None):
    if card_list == '':
        return ''
    if card_list is None:
        return None
    buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    key_for_brckets = {'A': 0, ' 2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
    rev_key_for_brckets = {0: 'A', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: 'T', 10: 'J', 11: 'Q', 12: 'K'}
    for x in card_list:
        buckets[key_for_brckets[x]] = buckets[key_for_brckets[x]] + 1
    output = []
    for y in range(len(buckets)):
        for z in range(buckets[y]):
            output.append(rev_key_for_brckets[y])
    return output
