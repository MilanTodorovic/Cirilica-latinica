from docx import Document
import sys, os, time

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

t1 = time.time()
print("Program starting...", time.strftime("%H:%M:%S", time.gmtime()))

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

cwd = os.getcwd()
files = os.listdir(cwd)
nr_files = len(list(filter(lambda x: ".docx" in x, files)))
number = 0

for file in files:
    if ".docx" in file:
        number+=1
        sys.stdout.write("Processing file: {0} of {1}\n".format(number, nr_files))
        sys.stdout.flush()
        with open(file, "rb") as f:
            doc = Document(f)
            for paragraph in doc.paragraphs:
                for run in paragraph.runs:
                    run.text = transliteracija(run.text)
            doc.save("latin_{}".format(file))
            
t2 = time.time()
print("Done.", time.strftime("%H:%M:%S", time.gmtime()))
print("Time elapsed: {0:.6f} seconds".format(t2-t1))
