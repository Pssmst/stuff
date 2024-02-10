import os

MasterList = []

def GrandSort(path):
   level_list = []
   current_level_list = []
   firstLineFound = False

   with open(path, "r", encoding='utf-8') as file:
      for line in file:
         current_list = []
         selection = ""

         for char in line: # Find first line
            if (char[0] in ['0','1','2','3','4','5','6','7','8','9']):
               current_list = []
               firstLineFound = True

         if (firstLineFound): # Do all the things...
            for char in line:
               if (char != "\t"): # Check if the next element is coming up
                  selection += char
               else:
                  current_list.append(selection)
                  selection = ""
               
               if (char == "\n"):
                  current_list.append(selection) # Append last element after loop
                  current_level_list.extend(current_list)
                  #print(current_list)
                  #print("CURRENT LEVEL LIST:", current_level_list, "\n")
               
                  # Check if the last element is indeed the level ID
                  if all(char.isdigit() or char == '\n' for char in current_level_list[-1]) and len(current_level_list[-1]) >= 8:
                  
                     # CLEAN UP LIST
                     current_level_list = [item for item in current_level_list if bool(item)] # Remove empty strings
                     current_level_list = [item.replace("\n", "") for item in current_level_list] # Remove newlines in elements
                     current_level_list = [item.replace("☠️", "") for item in current_level_list] # Remove newlines in elements
                     current_level_list = [item.replace("🟨", "🟡") for item in current_level_list] # Replaces old w/ new
                     current_level_list = [item.replace("⬛", "🔴") for item in current_level_list] # Replaces old w/ new
                     
                     for char in current_level_list: # Remove any weird garbage elements
                        if (char in ["☠️","👑"]):
                           del current_level_list[current_level_list.index(char)]
                     
                     #print(f"FINAL LIST: {current_level_list}\n")
                     level_list.append(current_level_list)
                     current_level_list = []
                     
                     # CLEAN UP LEVEL_LIST
                     for level in level_list:
                        #print(len(level))
                        for item in level:
                           if (item == "Level ID"): # Remove legends
                              rogue_index = level.index(item)+1
                              del level[:rogue_index]
                           
                           if (item in ["__","_"]): # Remove extra elements
                              del level[level.index(item)]
      return level_list

# Create MasterList
for year in range(2016, 2024 + 1):
   path = os.path.abspath(f"years/{year}.txt")
   MasterList.extend(GrandSort(path))

# CLEAN UP MASTERLIST #######################################################################################################

warning_list = []

def lookIn(place, emoji):
   if (char == emoji):
      rogue_index = MasterList[i][place[1]].index(char)
      warning_list.append([i, MasterList[i][place[1]][-rogue_index:], f"From: {place[0]}", MasterList[i][place[1]+1]])
      MasterList[i][place[1]] = MasterList[i][place[1]][:rogue_index]

for i in range(len(MasterList)):
   for j in range(2): # Do it twice (required for some reason)

      # Look for names of LEVELS cut into 2 elements
      if (MasterList[i][3][:3] != "By:"):
         MasterList[i][2] += MasterList[i][3] # Move it over
         del MasterList[i][3]
      
      # Look for names of SONGS cut into 2 elements
      if "⭐️" not in MasterList[i][5]:
         MasterList[i][4] += MasterList[i][5] # Move it all over
         MasterList[i][5] = MasterList[i][6]
         MasterList[i][6] = MasterList[i][7]
         del MasterList[i][7]
   
   # Separate a million warnings attached to both REWARDS and LEVEL ID
   for place in [["levelIDs", 5], ["rewards", 6]]:
      for emoji in ['🚨', '💀', '🔮', '✨', '🌋', '🔥', '⌛', '👹']:
         for char in MasterList[i][place[1]]:
            lookIn(place, emoji)
   
   # Fill in some missing IDs
   if (MasterList[i][6] == ""):
      MasterList[i][6] = MasterList[i][7]
      MasterList[i][7] = ""
   try:
      if (MasterList[i][7] == ""):
         MasterList[i][7] = MasterList[i][8]
         MasterList[i][8] = ""
   except: continue
   
# FIX THE UNREAD WARNINGS
for i in range(len(MasterList)):
   if ("Spike Gauntlet Level" in MasterList[i][6]):
      warning_list.append([i, "🏜️ Spike Gauntlet Level", "From: levelIDs", MasterList[i][7]])
      MasterList[i][6] = MasterList[i][7]
   
   if ("Gear Trilogy" in MasterList[i][6]):
      warning_list.append([i, "⚙️ Gear Trilogy", "From: levelIDs", MasterList[i][7]])
      MasterList[i][6] = MasterList[i][7]
   
   if ("HARD COIN" in MasterList[i][6]):
      warning_list.append([i, "⚠️HARD COINS", "From: levelIDs", MasterList[i][7]])
      MasterList[i][6] = MasterList[i][7]

   if ("HARD COIN" in MasterList[i][5]):
      warning_list.append([i, "⚠️HARD COIN(S)", "From: rewards", MasterList[i][6]])
      MasterList[i][5] = MasterList[i][5][:-12]

for i in range(len(MasterList)):
   try:
      MasterList[i][7] = ""
   except:
      continue

# print warning list
for i in range(len(warning_list)):
   print(warning_list[i])

star_list = []
for i in range(len(MasterList)):
   star_list.append(MasterList[i][5][0])
star_list = star_list[::-1]

# FLIP THE LIST
MasterList = MasterList[::-1]

# OUTPUT ##################################################################################################################
print(f'Longest List in MasterList:\nLength: {len(max(MasterList, key=len))}\nIndex: {MasterList.index(max(MasterList, key=len))}')

def output(path, item):
   with open(path, "w", encoding='utf-8') as f:
      for i in range(len(MasterList)): # Find width of array (using width of longest list)
         try:
            #f.write(f'{MasterList[i][0]} - {MasterList[i][item]}\n') # Use to help troubleshooting
            f.write(f'{MasterList[i][item]}\n')
         except:
            #f.write(f"{MasterList[i][0]} - \n") # Use to help troubleshooting
            f.write("")

# OUTPUT RAW LIST
with open(os.path.abspath("outputs/_rawOutput.txt"), "w", encoding='utf-8') as f:
   for i in range(len(MasterList)):
      f.write(f'{MasterList[i]}\n')

# OUTPUT ORGANIZED INFORMATION
output_paths = ["0_nums","1_dates","2_levels","3_creators","4_songs","5_rewards","6_levelIDs","7_extra", "8_extra2"]
for string in output_paths:
   path = os.path.abspath(f"outputs/{string}.txt")
   output(path, output_paths.index(string))

# Do the stars too
with open(os.path.abspath("outputs/9_stars.txt"), "w", encoding='utf-8') as f:
   for i in range(len(star_list)):
      f.write(star_list[i] + "\n")

print(">> Sorting Complete")