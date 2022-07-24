text = input("Enter text: ")

english_to_cyrillic_mapping = [
    ["A", "\u0410"],
    ["B", "\u0412"],
    ["C", "\u0421"],
    ["E", "\u0415"],
    ["H", "\u041D"],
    ["K", "\u041A"],
    ["M", "\u041C"],
    ["O", "\u041E"],
    ["P", "\u0420"],
    ["T", "\u0422"],
    ["Y", "\u0423"],
    ["X", "\u0425"],
    ["a", "\u0430"],
    ["e", "\u0435"],
    ["o", "\u043E"],
    ["p", "\u0440"],
    ["c", "\u0441"],
    ["y", "\u0443"],
    ["x", "\u0445"],
]

for char in english_to_cyrillic_mapping:
    text = text.replace(char[0], char[1])

print(text)
