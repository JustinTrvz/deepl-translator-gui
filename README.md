# DeepL Translator GUI
- Translate any words from a language to the desired target language in a simple GUI.
- Default language is 'DE' (German), but feel free to change the target language.


## Requirements
- Python
- DeepL API Key

### Python
- **Windows:** See this tutorial: [How to install Python on Windows](https://realpython.com/installing-python/#how-to-install-python-on-windows)
- **Linux:**  Execute `sudo apt-get install python3-tk` on command-line.

### DeepL API Key
1. Visit [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api/).
2. Sign up for free API usage or login.
3. Start free trial.
4. Visit your [DeepL Account Summary](https://www.deepl.com/account/summary) and copy the `Authentication Key for DeepL API`.
   - The key looks like: `kjdf39-345jernt-nt4ntr-nxckj7:abc` (_Just an example! Do not use it!_)
5. Create a file `deepl_api.txt` in this directory and insert your copied DeepL API key.

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

# Change target language
1. Open `translator.py` with your favorite editor.
2. In the section `# DeepL Translator config` you need to change the variable
   1. `TARGET_LANGUAGE` to any [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
      1. _Example: `TARGET_LANGUAGE = 'PL'`_
   2. `TARGET_LANGUAGE_TEXT` to the coherent [ISO language name](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
      1. _Example: `TARGET_LANGUAGE_TEXT = 'Polish'`_