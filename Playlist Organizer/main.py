import os

playlist_path = os.path.abspath("playlist.txt")
output_path = os.path.abspath("output.txt")

song_list = []
current_list = []
append_condition = False

with open(playlist_path, "r", encoding='utf-8') as file:
   for line in file:
      for char in line: # Check for song length line
         if (char == ":"):
            append_condition = True
      
      if (append_condition == True): # Just keep appending lines
         current_list.append(line)
      
      for char in line:
         if (char == "•" and len(line) > 3): # Check for final line
            append_condition = False
            song_list.append(current_list)
            current_list = []

############ SONG EXAMPLE ##############################################
#  4:05                       # Song length (start list here)          #
#  NOW PLAYING                                                         #
#  Choose Your Seeds          # Song name                              #
#  Ruscel Torres              # Uploader                               #
#  •                                                                   #
#  22K views • 4 months ago   # Views and upload date (end list here)  #
########################################################################

with open(output_path, "w", encoding='utf-8') as f:
   f.write("### NUMBERS (COLUMN 1) ##############################\n\n")
   for i in range(len(song_list)):
      f.write(str(i+1) + "\n")
   
   f.write("\n\n### SONGS (COLUMN 2) ##############################\n\n")
   for i in range(len(song_list)):
      f.write(song_list[i][2])
      
   f.write("\n\n### LENGTH (COLUMN 3) ##############################\n\n")
   for i in range(len(song_list)):
      f.write(song_list[i][0])
   
   f.write("\n\n### UPLOADERS (COLUMN 4) ##############################\n\n")
   for i in range(len(song_list)):
      f.write(song_list[i][3])
   
