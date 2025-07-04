# Greek categorized wordlist
This wordlist is ideal for games. It has Greek words, written in lowercase and with tonos. Also there is a category next to each word

![image](https://github.com/user-attachments/assets/f20b4f2f-527e-4471-8bd0-4eac06866b2a)


# Usage
The wordlist is ideal to use for games where you need greek words depending on different categories.

# Categories
There are 15 diffent categories (for example months, colors, buildings, fruits etc)

# How to use the wordlist
word_loader.py  
In this file is all the heavy job done.  
There are functions:  
remove_tonos(text) to remove the tonos from the words  
load_words_with_categories(filename="greekWordlistCategorized.txt") the main function to load the wordlist  
get_words_by_category(category, word_list)  
get_all_categories(word_list)  

In the main file type folowing:

`from word_loader import load_words_with_categories, get_words_by_category, get_all_categories`  
`word_list = load_words_with_categories()`

To Get all categories  

`categories = get_all_categories(word_list)`  

To Get words only from specific categories  

`selected_categories = ["Ζώο", "Φρούτο"]`  
`filtered_words = [entry for entry in word_list if entry[1] in selected_categories]`  

Or use the helper:  

`words_in_animal = get_words_by_category("Ζώο", word_list)`
