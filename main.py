import re
x = input("Ievadi tekstu: ")
text = re.sub(r'\{[^}]*\}', '', x)
print(text)