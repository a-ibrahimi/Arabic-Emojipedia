from typing import Optional
import pkg_resources
import pandas as pd
import logging

def load_data():
    """Return a dictionary with the different emojis and their corresponding descriptions

    Contains the following fields:
        emoji          str
        text           str

    """
    stream = pkg_resources.resource_stream(__name__, 'data/emojis.csv')
    return pd.read_csv(stream, encoding='utf-8')

emoji_df = load_data()

def get_emoji_description(emoji) -> Optional[str]:
    """Retrieve the text description associated with a given emoji.

    Args:
    - emoji (str): The emoji for which the description is requested.

    Returns:
    - Optional[str]: The text description corresponding to the provided emoji.
                     Returns None if the description is not found.

    This function searches for the text description of a specified emoji within
    the emoji_df DataFrame. If the emoji is found, it returns the associated text.
    If no matching text is found for the given emoji, it logs an error using the
    logging module and returns None.
    """
    text_for_emoji = emoji_df.loc[emoji_df['emoji'] == emoji, 'text'].values

    if len(text_for_emoji) > 0:
        return text_for_emoji[0]
    else:
        logging.error(f"No text found for emoji {emoji}")