import csv
from typing import Optional

def load_data_from_csv(path):
    emoji_dict ={}
    with open(path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            emoji_dict[row['emoji']] = row['text']
    return emoji_dict

emoji_dict = load_data_from_csv('emojis.csv')

def get_emoji_description(emoji) -> Optional[str]:
    try:
        return emoji_dict[emoji]
    except KeyError:
        raise KeyError(f"Input '{emoji}' not found in the emoji dataset.")