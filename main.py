import re

conversion_table: dict = {
    "⓪": "0",
    "①": "1",
    "②": "2",
    "③": "3",
    "④": "4",
    "⑤": "5",
    "⑥": "6",
    "⑦": "7",
    "⑧": "8",
    "⑨": "9",
    "➕": "+",
    "➖": "-",
    "❌": "*",
    "➗": "/",
    "㌫": "%",
    "　": " ",
    "《": "(",
    "》": ")",
    "“": '"',
}

def replacement(match):
    return conversion_table[match.group(0)]

def transpile(source: str, conversion_table: dict) -> str:
    result: str = ""
    for char in source:
        if char in conversion_table.keys():
            result += conversion_table[char]
        else:
            result += char
    return result

def convert(source: str) -> str:
    return transpile(source, {value: key for key, value in conversion_table.items()})

def check_error(source: str):
    if len(re.findall("[1-9]", source)) != 0:
        raise SyntaxError("It's not allowed use normal number character. Instead, you can use only circle number character as number expression.")
    if len(re.findall(r"\+|\-|\*|\/|\%", source)) != 0:
        raise SyntaxError("It's not allowed use normal operator character. Instead, you can use only decorated operator character as operator expression.")
    if len(re.findall(r"[a-z]|[A-Z]", source)) != 0:
        raise SyntaxError("It's not allowed use normal alphabets character. Instead, you can use cute pictograph")

print("⑨ hard to input esolang calculator")
while True:
    code = input("> ")
    check_error(code)
    print(convert(str(eval(transpile(code, conversion_table)))))
