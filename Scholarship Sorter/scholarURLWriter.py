from urllib.parse import quote # Just for STUPID HIDDEN CHARACTERS

scholarship_list = []
string = ""

# 374: Lots of locations (African American Achievement Scholarship)
# 4674: Profession example
# 429: Weird profession example

startpos = 0 # 4

def removeHiddenCharacters(original_string, reference_string):
   # Create a set of characters in the reference string for efficient lookup
   reference_set = set(reference_string)
   
   # Use list comprehension to keep only the matching characters
   filtered_string = ''.join(char for char in original_string if char in reference_set)
   
   return filtered_string


with open("scholarships.txt", 'r', encoding="utf-8") as file:
   scholarships = file.readlines()
   for line in scholarships:
      line = line.lower()

      for char in line:
         if (char == " "):
            char = "-"
         if (char in [' ', '_', ',', '<', '.', '>', '/', '?', "'", '"', '[', ']', '{', '}', '\\', '|', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '`', '~']):
            char = ""
         string += char

      # Reveals hidden characters -- i.e. garbage like "%E2%80%8B"
      encoded_string = removeHiddenCharacters(quote(string), string)
      
      # Sometimes there's a random "0" at the end of the link and I don't know why
      if (encoded_string and encoded_string[-1] == "0"): # I don't know why I need the first argument but it just works
         encoded_string = encoded_string[:-1]
      
      url = f"https://bigfuture.collegeboard.org/scholarships/{encoded_string}\n"
      
      if (len(encoded_string) >= 2):
         if (encoded_string != "back-to-top"):
            scholarship_list.append(url)

      string = ""

with open("filteredScholarships.txt", 'w', encoding="utf-8") as file:
   for line in scholarship_list:
      if (scholarship_list.index(line) >= startpos):
         file.write(line)
   print("\nDone! Scholarship URLs updated.\n")