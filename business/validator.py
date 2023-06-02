
allowed_chars = set("qwertyuioplkjhgfdsazxcvbnm,.?,\' ")


def validate(text):
    return сорян_за_такую_валидацию(text)


def сорян_за_такую_валидацию(text):
    # удаляем всякие непонятные кракозябры :)
    cleaned_text = ''.join(char for char in text if char.lower() in allowed_chars)
    return cleaned_text
