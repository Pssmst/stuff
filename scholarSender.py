import json

details = [
   'scholarshipName: ',        # String   0
   'scholarshipOpen: ',        # String   1
   'scholarshipDeadline: ',    # String   2
   'isEssayRequired: ',        # Bool     3
   'isNeedBased: ',            # Bool     4
   'isMeritBased: ',           # Bool     5
   'applicationUrl: ',         # String   6
   'programUrl: ',             # String   7
   'degreeSeeking: ',          # List     8
   'enrollmentStatus: ',       # List     9
   'citizenshipStatuses: ',    # List     10
   'demographics: ',           # List     11
   'currentGradeLevel: ',      # List     12
   'miscellaneous: ',          # List     13
   'activity: ',               # List     14 
   'affiliation: ',            # List     15
   'armedServices: ',          # 2D Array 16
   'situation: ',              # List     17
   'profession: ',             # 2D Array 18
   'financialInformation: ',   # List     19
   'applicationRestriction: ', # String   20
   'academics: ',              # List     21
   'condition: ',              # List     22
   'fieldsOfStudy: ',          # List     23
   'locations: ',              # DICT     24
   'interests: ',              # List     25
   'studyAbroad: ',            # List / Sometimes found as `[]` instead of `None`
   'age: ',                    # String   27
   ''                          # Additional Data
]

unwanted_characters = ["'",'"','[',']']

with open("rawOutput.txt", 'r', encoding="utf-8") as file:
   with open("output.txt", 'w', encoding="utf-8") as f:
      data = file.readlines()
      
      MasterList = []
      scholarship = []
      i = 0
      
      for line in data:
         line = line.strip()
         #print(line, end='')
         
         if (line == ''):
            MasterList.append(scholarship)
            scholarship = []
            i = -1
         
         # Remove programmy looking stuff around the lists
         if (i in [8,9,10,11,12,13,14,15, 17,19, 21,22,23, 25,26]):
            for char in unwanted_characters:
               line = line.replace(char,'')
         
         # REMOVE BEGINNING TAG
         if (line[:len(details[i])] == details[i]): # If line starts with correct detail name
            data_length = len(details[i]) - len(line) # Calculate length of string that goes AFTER detail name
            
            if (line != ''):
               line = line[data_length:].rstrip('\n')
               
               if (line in ['None','fieldsOfStudy: '] and i not in [1,2]): # Replace "None" with empty space
                  line = ' '
               
               if (i in [3,4,5]): # Is Essay Required or Need-Based or Merit-Based
                  if (line == 'False'): line = 'Yes'
                  else: line = 'No'
               
               
               elif (i == 16 and line != ' '): # ARMED SERVICES
                  data = eval(line) # Convert the string back into a 2D-array
                  line = ""
                  
                  for service in data:
                     if (service[0] == '-'): service[0] = '(No specific branch)'
                     if (service[2] == '-'): service[2] = ''
                     
                     line += f"<strong>{service[0]}</strong><br>"
                     line += f"<strong>- Status:</strong> {service[1]}<br>"
                     line += f"<strong>- Relations:</strong> {service[2]}<br>" if service[2] else ""
                     line += "<br>"
               
               
               elif (i == 18 and line != ' '): # PROFESSION
                  data = eval(line) # Convert the string back into a 2D-array
                  line = ""
                  for service in data:
                     line += f"{service[0]}<br>- <strong>{service[1][:7]}</strong>{service[1][7:]}<br><br>"
               
               
               elif (i == 24): # LOCATIONS
                  data = eval(line) # Convert the string back into a dict
                  line = ""
                  
                  for country, states in data.items():
                     line += f"<strong>{country} ---------------</strong><br>"
                     if not states:
                        line += "(Everywhere)"
                     else:
                        for state, (cities, counties) in states.items():
                           line += f"<strong>State:</strong> {state}<br>"
                           line += f"<strong>- Cities:</strong> {', '.join(cities)}<br>" if cities else ""
                           line += f"<strong>- Counties:</strong> {', '.join(counties)}<br>" if counties else ""
                     line += "<br>"
               
               scholarship.append(line)
         i += 1
      
      empty_list = False

      # CLEANUP EMPTY LISTS
      for s in range(len(MasterList)):
         try:
            if (empty_list):
               del MasterList[s]
               empty_list = False
            
            if (MasterList[s] == []):
               empty_list = True
            
            f.write(f'{str(MasterList[s])}\n') # Comment out eventually
         except:
            continue

################################################################################################################

# Move data to json
with open('App/output.js', 'w') as f:
   f.write(f'var MasterList = {json.dumps(MasterList)};')

print("> Scholarships sorted")