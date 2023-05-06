# DeepL Translator GUI
- Translate any words from a language to the desired target language in a simple GUI.
- Default language is 'DE' (German), but feel free to change the target language.


## Requirements
- DeepL API Key
- Python

## Usage
![](images/translator-usage.png)
- The DeepL Translator GUI is meant to be used while reading documents of a foreign language.
- Paste or type the words in the top text field and afterwards click on `Translate`. 
- You can right-click on the windows top bar and set it to `Always on top`.
- The shortcut `Ctrl+A` select all the text from both text fields.
- Only the textfield `Any language:` is modifyable.

## Setup
1. It is recommended to use a [Python Venv](https://docs.python.org/3/library/venv.html).
   1. Change to this directory, if not already done.
      - `cd <YOUR_WORK_DIR>/fixed-translator`
   2. Create a Python venv in this directory.
      - `python -m venv .`
2. Install pip packages.
   1. `pip install -r requirements.txt`
3. Execute the script.
   1. `python3 ./translator.py`
