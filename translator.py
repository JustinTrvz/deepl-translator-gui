import tkinter as tk
import requests
import base64

# DeepL API-Konfiguration
api_key_file = open("deepl_api.txt", "r")
api_key = api_key_file.readline()
DEEPL_API_KEY = str(base64.b64decode(api_key), "utf-8")
DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'


def select_all_text(event):
    if (event.state & 0x4) != 0 and event.keysym.lower() == 'a':
        event.widget.tag_add('sel', '1.0', 'end')

# GUI erstellen
def create_gui():
    window = tk.Tk()
    window.title('DeepL Übersetzer')

    input_label = tk.Label(window, text='Any language:')
    input_label.pack()

    input_text = tk.Text(window, height=3, width=30)
    input_text.pack()
    input_text.bind_all('<Control-a>', select_all_text)
    input_text.bind_all('<Control-A>', select_all_text)

    translate_button = tk.Button(window, text='Translate', command=lambda: translate_text(input_text, output_text))
    translate_button.pack()

    output_label = tk.Label(window, text='German:')
    output_label.pack()

    output_text = tk.Text(window, height=3, width=30)
    output_text.pack()


    window.mainloop()


# Textübersetzung mit der DeepL API
def translate_text(input_text, output_text):
    text = input_text.get('1.0', 'end-1c')  # Eingabetext abrufen

    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}'
    }

    params = {
        'text': text,
        'target_lang': 'DE'
    }

    response = requests.post(DEEPL_API_URL, headers=headers, data=params)

    output_text.config(state='normal')

    if response.status_code == 200:
        output_text.delete('1.0', tk.END)
        translation = response.json()['translations'][0]['text']
        output_text.insert('end', translation)  # Übersetzung in Ausgabefeld einfügen
    else:
        output_text.insert('end', 'Fehler bei der Übersetzung')#

    output_text.config(state='disabled')


# GUI starten
if __name__ == '__main__':
    create_gui()
