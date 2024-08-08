def main():
  book_path = 'books/frankenstein.txt'
  book_text = get_book_text(book_path)
  num_words = count_words(book_text)
  char_stats = get_char_stats(book_text.lower())
  stats_list = dict_to_array(char_stats)

  stats_list.sort(reverse=True, key=sort_on("times"))
  
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  print("\n")
  for item in stats_list:
    if item["char"].isalpha():
      print(f"The '{item['char']}' character was found {item["times"]} times")
  print("\n")
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  words = text.split()
  return len(words)

def get_char_stats(text):
  characters = {}
  for char in text:
    if char in characters:
      characters[char] += 1
    else:
      characters[char] = 1
  return characters

def dict_to_array(obj):
  list = []
  for key in obj:
    item = { 'char': key, 'times': obj[key] }
    list.append(item)
  return list

def sort_on(key):
  return lambda dict: dict[key]

def sort_on_new(dict):
  print('test', dict, dict["times"])
  return dict["times"]

main()
