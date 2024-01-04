from openai import OpenAI
client = OpenAI()
import re


def openai_translate(origin_language, target_language, text):
    """openai_translate
    Args:
        origin_language (str): origin_language
        target_language (str): target_language
        text (str): text
    """
    prompt = [
        {
        "role": "system",
        "content": f"You will be provided with a sentence in {origin_language}, and your task is to translate it into {target_language}."
        },
        {
        "role": "user",
        "content": text
        }
    ]
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=prompt,
    temperature=0.7,
    max_tokens=128,
    top_p=1
    )
    print("原文: " + text)
    print("翻译结果: " + response.choices[0].message.content)
    return response.choices[0].message.content

def translate_srt_line(origin_language, target_language, text, n):
    print("\rtranslate line in: ", n + 1, end=" ")
    print(text)
    if text == "" or text == '\n':
        return text
    text = text.rstrip('\n')
    if re.match(r"^[0-9]+$", text):
        return add_newline_if_missing(text)

    if re.match(r"\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}", text):
        return add_newline_if_missing(text)
    return add_newline_if_missing(openai_translate(origin_language, target_language, text))

def add_newline_if_missing(s):
    if not s.endswith('\n'):
        s += '\n'
    return s

def translate_file(origin_language, target_language, origin_file, target_file):
    with open(origin_file, 'r', encoding='utf-8') as f1, open(target_file, 'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        print("translate file total lines: ", len(lines))
        for n, line in enumerate(lines):
            result = translate_srt_line(origin_language, target_language, line, n)
            f2.writelines(result)
        print("\ntranslate write file done")

if __name__ == "__main__":
    # openai_translate("English", "Chinese", "Hello, World!")
    translate_file("en", "zh", "G:/0_data/01_录播/0_vedal987/2024-01-01/test.srt", "G:/0_data/01_录播/0_vedal987/2024-01-01/test_zh.srt")