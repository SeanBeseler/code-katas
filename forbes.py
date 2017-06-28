import json
import sys

def get_billionaire(file_name='data.json'):
    """get the info for the oldest and youngest billionaire under 80"""
    print('here')
    with open(file_name) as data_file:
        data = json.load(data_file)
    oldest = None
    youngest = None
    for billionaire in data:
        if not oldest and not youngest and billionaire['net_worth (USD)'] > 999999999:
            youngest = billionaire
            oldest = billionaire
        elif billionaire['age'] < 80 and billionaire['net_worth (USD)'] > 999999:
                if billionaire['age'] > oldest['age']:
                    oldest = billionaire
                elif billionaire['age'] > 0:
                    if billionaire['age'] < youngest['age']:
                        youngest = billionaire
    output = [oldest['name'], oldest['net_worth (USD)'], oldest['source'], youngest['name'], youngest['net_worth (USD)'], youngest['source']]
    return(output)


if __name__ == '__main__':
    print(get_billionaire(sys.argv[1]))
