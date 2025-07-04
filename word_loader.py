import unicodedata

def remove_tonos(text):
    """Removes Greek tonos and returns uppercase version."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).upper()

def load_words_with_categories(filename="words.txt"):
    """Loads (cleaned_word, raw_category) pairs from file."""
    word_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    raw_word = parts[0].strip()
                    raw_category = parts[1].strip()
                    clean_word = remove_tonos(raw_word).upper()
                    category = raw_category.capitalize()
                    word_list.append((clean_word, category))
    except FileNotFoundError:
        print("Το αρχείο words.txt δεν βρέθηκε.")
    return word_list

def get_words_by_category(category, word_list):
    """Returns a list of words from a specific category."""
    return [word for word, cat in word_list if cat.lower() == category.lower()]

def get_all_categories(word_list):
    """Returns a sorted list of unique categories."""
    return sorted(set(cat for _, cat in word_list))
