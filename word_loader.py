import unicodedata

# Functions
def load_words_with_categories(filename="greekWordlistCategorized.txt"):
    """
    Loads raw words and categories from file, no processing.
    Returns: List of (word, category) as-is from the file.
    """
    word_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    word = parts[0].strip()
                    category = parts[1].strip()
                    word_list.append((word, category))
    except FileNotFoundError:
        print("Το αρχείο greekWordlistCategorized.txt δεν βρέθηκε.")
    return word_list

def load_words_only(filename="greekWordlistCategorized.txt"):
    """
    Loads just the raw words (without categories) from the file.
    Returns: List of strings.
    """
    words = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 1:
                    word = parts[0].strip()
                    if word:
                        words.append(word)
    except FileNotFoundError:
        print("Το αρχείο greekWordlistCategorized.txt δεν βρέθηκε.")
    return words

def capitalize_first_letter(text):
    """
    Capitalizes only the first letter, rest stays lowercase.
    Example: 'μήλο' → 'Μήλο'
    """
    return text[:1].upper() + text[1:].lower() if text else ""

def remove_tonos(text):
    """
    Removes Greek tonos/accents from the string.
    Example: 'μήλο' → 'μηλο'
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def capitalize_all(text):
    """
    Converts entire string to uppercase.
    Example: 'μήλο' → 'ΜΉΛΟ'
    """
    return text.upper()

def get_words_by_category(category, word_list):
    """Returns a list of words from a specific category."""
    return [word for word, cat in word_list if cat.lower() == category.lower()]

def get_all_categories(word_list):
    """Returns a sorted list of unique categories."""
    return sorted(set(cat for _, cat in word_list))

### Main ###
# Load the wordlist file    
words = load_words_only()

for word in words:
    # Remove tonos
    no_tonos = remove_tonos(word)

    #Capitalize first letter only
    first_cap = capitalize_first_letter(no_tonos)

    #Capitalize whole word
    all_caps = capitalize_all(no_tonos)

    #print(f"Original: {word}")
    #print(f"  No tonos: {no_tonos}")
    #print(f"  First letter capitalized: {first_cap}")
    print(all_caps)
