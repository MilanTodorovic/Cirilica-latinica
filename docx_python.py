from docx import Document


def transliteracija(text):
    global letters_dct, digraphs_dct
    global capital_letters_dct, capital_digraphs_dct
    _text = ""

    for i in text:
        if i.isalpha():
            if i.isupper():
                _text += capital_letters_dct.get(i,
                            capital_digraphs_dct.get(i, i))
            else:
                _text += letters_dct.get(i,
                            digraphs_dct.get(i, i))
        else:
            _text += i
            
    return _text


lst = []
letters = "абвгдђежзијклмнопрстћуфхцчш"
capital_letters = letters.upper()
digraphs = "њљџ"
capital_digraphs = digraphs.upper()
latin_letters = "abvgdđežzijklmnoprstćufhcčš"
capital_latin_letters = latin_letters.upper()
latin_digraphs = ["nj","lj","dž"]
capital_latin_digraphs = [x.upper() for x in latin_digraphs]

letters_dct = {x:y for x,y in zip(letters, latin_letters)}
digraphs_dct = {x:y for x,y in zip(digraphs, latin_digraphs)}
capital_letters_dct = {x:y for x,y in zip(capital_letters,
                                          capital_latin_letters)}
capital_digraphs_dct = {x:y for x,y in zip(capital_digraphs,
                                       capital_latin_digraphs)}


with open("Eskimski-cobissnet.docx", "rb") as f:
    doc = Document(f)
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.text = transliteracija(run.text)
    doc.save("experiment.docx")
