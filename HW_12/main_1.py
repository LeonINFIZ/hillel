import codecs


def delete_html_tags_and_clean(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """
    Removes all HTML tags from the provided HTML file, cleans the resulting text
    by stripping extra whitespace and empty lines, and writes the cleaned text
    to a specified output file.

    :param html_file: The path to the input file containing HTML content.
    :type html_file: str
    :param result_file: The path to the output file where the cleaned text will be
        written. Defaults to 'cleaned.txt'.
    :type result_file: str, optional
    :returns: None
    """
    html = ""

    # Читання HTML-файлу повністю
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    new_text = ""

    # Видалення HTML-тегів
    while '<' in html and '>' in html:
        # Визначення індексів початку та кінця першого тегу
        start_tag = html.index('<')
        end_tag = html.index('>')

        # Витягування тексту перед тегом
        new_text += html[:start_tag]

        # Видалення тегу зі строки
        html = html[end_tag + 1:]

    # Додавання залишку тексту, якщо він є
    new_text += html

    # Очищення тексту від зайвих пробілів та порожніх рядків
    cleaned_text = "\n".join(
        line.strip() for line in new_text.splitlines() if line.strip()
    )

    # Збереження результату у файл
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)


delete_html_tags_and_clean('draft.html', result_file='cleaned.txt')
