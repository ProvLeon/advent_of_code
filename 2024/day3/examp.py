import re

def get_result(s):
    """Calculate the sum of products from 'mul(...)' patterns in the string."""
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    result = 0
    for m in re.findall(pattern, s):
        # print(m)
        l, r = m[4:-1].split(',')
        # print(l, r)
        result += int(l) * int(r)
    return result


# Part 2
def remove_dont_to_do(text):
    """Remove all substrings from 'don't()' to 'do()' in the given text."""
    pattern = r"don't\(\).*?do\(\)"
    cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)
    return cleaned_text

with open("day3_input.txt", "r", encoding = "utf-8") as file:
    text = file.read()
print(text)
print(get_result(text))

cleaned_text = remove_dont_to_do(text)
print(cleaned_text)
print(get_result(cleaned_text))
