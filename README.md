# Arabic Emojipedia

Welcome to the Arabic Emojis Dataset Repository!🌟

The aim of this repository is to serve as a linguistic resource for NLP researchers focusing on Arabic language and dialects. The included CSV file and associated package provides an easy way to substitute emojis with their corresponding Arabic descriptions, thereby enhancing interpretability and ensuring consistent representation in Arabic language and dialect datasets, including Moroccan and Tunisian Darija.

The dataset was created by processing the emoji dataset available at [https://github.com/datasets/emojis](https://github.com/datasets/emojis). We wholeheartedly encourage contributions to expand and enrich this resource further.

## Package Integration
### New Addition: Package for Emoji Descriptions

A Python package associated with this dataset! You can programmatically access emoji descriptions using a dedicated function provided by this package.

### Installation
You can install our package via pip:
```py
pip install arabic-emojipedia
```

### Usage Example
```py
from arabic-emojipedia.emoji_description import get_emoji_description

emoji = "😊"
description = get_emoji_description(emoji)
print(f"Description for {emoji}: {description}")
```

## CSV File Structure

The CSV file follows a structured format as shown below:

| Emoji | Name                |
|-------|---------------------|
| 🎃    | جاك فانوس          |
| 🎄    | شجرة عيد الميلاد  |
| 🎆    | العاب ناريه        |
| 🎇    | الماسة             |
| 🧨    | مفرقعة نارية       |
| ✨    | بريق               |
| 🎈    | بالون              |
| 🎉    | بوبر الحزب         |

The file contains a total of 4,733 emojis.

🚀 Feel free to explore and leverage this dataset to enhance your NLP research in Arabic. We look forward to your contributions to make this resource even more comprehensive and valuable.

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.
