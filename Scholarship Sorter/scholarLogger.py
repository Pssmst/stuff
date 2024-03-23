from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import pandas as pd
import json
import re

# URL WRITING ###################################################################################################################
import subprocess
subprocess.run(['python', 'scholarURLWriter.py'], check=True)

# MAIN ##########################################################################################################################

easyDetails = [
   "scholarshipName",      # Name of scholarship
   #"scholarshipStatus",   # Available to apply? (Will quickly become outdated)
   "scholarshipOpen",      # Open date
   "scholarshipDeadline",  # Closing date
   #"applicationFee",      # Cost to apply (...what? Scholarships are free!)
   "isEssayRequired",      # Is an essay required?
   "isNeedBased",          # Is it need-based?
   "isMeritBased",         # Is it merit-based?
   "applicationUrl",       # URL to apply
   "programUrl"            # URL to program
   #"aboutPara"            # Summary of everything you already know
   #"eligibilityCriteriaDescriptions"
]

complexDetails_lists = [
   "degreeSeeking",
   "enrollmentStatus",
   "citizenshipStatuses",
   "demographics"
]
complexDetails_dicts = [
   "currentGradeLevel",       # ['currentGrade']
   "miscellaneous",           # ['miscellaneousCriteria','miscellaneousOther']
   "activity",                # ['activity','activityOther']
   "affiliation",             # ['affiliationEntityOther','indirectRelation','affiliationEntity','directRelation']
   "armedServices",           # ['armedServiceBranch','armedServiceStatus','armedServiceRelation']
   "situation",               # ['situation','situationOther']
   "profession",              # ['profession','isCurrentProfession','professionOther','mustBeCurrentProfession','socCode']
   "financialInformation",    # ['financialEligibilityCriteria','financialEligibilityAmount']
   "applicationRestriction",  # ['applicationRestriction']
   "academics",               # ['academicEligibility','academicEligibilityValue']
   "condition",               # ['condition']
   "fieldsOfStudy",           # ['fieldName','cipCode']
   "locations",               # ['country','county','state']
   "interests",               # ['interestOther','interestCriteria']
   "studyAbroad",             # ['country']
   "age",                     # ['maximumAgeRequirement','minimumAgeRequirement']
]
complexDetails_redundantDicts = [
   "currentGradeLevel",       # ['currentGrade']
   "miscellaneous",           # ['miscellaneousCriteria','miscellaneousOther']
   "activity",                # ['activity','activityOther']
   "situation",               # ['situation','situationOther']
   "condition",               # ['condition']
   "fieldsOfStudy",           # ['fieldName','cipCode']
   "interests",               # ['interestOther','interestCriteria']
   "studyAbroad",             # ['country']
]

# RARE: "collegeAttendaneCriteria", "graduationStatuses"
# Needed: "collegeReadinessProgramParticipation", "currentSchool"

def scholarSorter(url):
   page = requests.get(url) # Gets all the HTML in the URL
   soup = BeautifulSoup(page.text, "html.parser")
   script_tag = soup.find("script", id="__NEXT_DATA__")

   if (script_tag):
      json_data = script_tag.string
      data = json.loads(json_data)
      
      info_list = []
      
      # TEST IF URL WORKS
      try:
         print(data["props"]["pageProps"]["data"]["scholarshipName"])
      except:
         print(f"Not worky: {url}") ,info_list.append(f"Not worky: {url}")
         return "Broken URL"
      
      # DETAILS #################################################################################################################
      '''
      # FIND SOMETHING IN SPECIFIC (comment out the other detail finders)
      thingToFind = 'collegeAttendanceCriteria'
      print(f'{thingToFind}: {data["props"]["pageProps"]["data"]["eligibilityCriteria"][thingToFind]}')
      if (data["props"]["pageProps"]["data"]["eligibilityCriteria"][thingToFind] != None):
         input(), input('yo'), input('you found the thing'), input('you sure you dont care?')
      '''
      
      # Details that are easy to find (in the data directly)
      for key in easyDetails:
         try: # You know, some people are just lazy and forget to add some things
            value = data["props"]["pageProps"]["data"][key]
            info_list.append(f"{key}: {value}") #,print(f"{key}: {value}")
         except:
            info_list.append(f"{key}: None") #,print(f"{key}: None")
      
      # Complex details marked as LISTS (in eligibilityCriteria)
      for element in complexDetails_lists:
         value = data["props"]["pageProps"]["data"]["eligibilityCriteria"][element]
         info_list.append(f"{element}: {value}") #,print(f"{element}:", value)
      
      # Complex details marked as DICTIONARIES (in eligibilityCriteria)
      for key in complexDetails_dicts:
         topic = data["props"]["pageProps"]["data"]["eligibilityCriteria"][key]
         
         if (topic != None): # Only do details that are ACTUALLY there
            
            # REDUNDANTS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if (key in complexDetails_redundantDicts):
               dundant_list = []
               
               for subtopic in topic: # Iterate through each dictionary in the topic
                  for Key, value in subtopic.items(): # Iterate through each element in the dictionary
                     if (value in [None, 'Other']): continue
                     else: dundant_list.append(value)

               info_list.append(f"{key}: {dundant_list}") #,print(f"{key}: {dundant_list}")
            
            
            # PROFESSION ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif (key == 'profession'):
               profession_list = []
               
               for subtopic in topic: # Iterate through each dictionary in the topic
                  
                  profession_specifics = []
                  for Key, value in subtopic.items(): # Iterate through each element in the dictionary
                     if (value not in ['Other', None]):
                        profession_specifics.append(value)
                  
                  try:
                     if (profession_specifics[1]):
                        profession_specifics[1] = "Must be current profession"
                     else:
                        profession_specifics[1] = "Doesn't need to be current profession"
                  except:
                     profession_specifics.append('N/A')
                  profession_list.append(profession_specifics)
               
               info_list.append(f"{key}: {profession_list}") #,print(f"{key}: {profession_list}")
            
            
            # AFFILIATION +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif (key == 'affiliation'):
               
               affiliation_list = []
               for subtopic in topic: # Iterate through each dictionary in the topic
                  
                  affiliation_specifics = []
                  for Key, value in subtopic.items(): # Iterate through each element in the dictionary
                     if (Key != 'indirectRelation'):
                        affiliation_specifics.append(value)
                  
                  for i in affiliation_specifics[:]:
                     if (i in [None, 'Other']):
                        del affiliation_specifics[affiliation_specifics.index(i)]

                  affiliation_list.append(f'{affiliation_specifics[1]} {affiliation_specifics[0]}')

               affiliation_list = list(set(affiliation_list)) # Removes duplicates
               info_list.append(f"{key}: {affiliation_list}") #,print(f"{key}: {affiliation_list}")
            
            
            # ARMED SERVICES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif (key == 'armedServices'):
               
               service_list = []
               for subtopic in topic: # Iterate through each dictionary in the topic
                  
                  service_specifics = []
                  for Key, value in subtopic.items(): # Iterate through each element in the dictionary
                     if (value == None): value = '-'
                     service_specifics.append(value)
                  
                  service_list.append(service_specifics)

               formatted_data = defaultdict(lambda: defaultdict(set)) # Thanks ChatGPT

               # Iterate through the service_list and organize the data
               for branch, status, relation in service_list:
                  formatted_data[branch][status].add(relation)

               # Lists to hold the branches, statuses, and relations
               new_service_list = []

               # Extract data from formatted_data
               for branch, status_relations in formatted_data.items():
                  services = ", ".join(sorted(status_relations.keys()))
                  relations = ", ".join(sorted(set.union(*status_relations.values())))
                  new_service_list.append([branch, services, relations])

               info_list.append(f"{key}: {new_service_list}") #,print(f"{key}: {new_service_list}")


            # LOCATIONS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif (key == 'locations'):
               locations = topic
               
               new_locations = {}

               # Group locations by country
               for location in locations:
                  country = location['country']
                  state = location.get("state")
                  city = location.get("city")
                  county = location.get("county")

                  if country not in new_locations:
                     new_locations[country] = {}

                  if state: # If the state is specified (not None)
                     if state not in new_locations[country]:
                        new_locations[country][state] = ([], [])

                     if city:     new_locations[country][state][0].append(city) # First part of tuple
                     elif county: new_locations[country][state][1].append(county) # Second part of tuple

               info_list.append(f"{key}: {new_locations}") #,print(f"{key}: {new_locations}")


            # ACADEMICS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif (key == 'academics'):
               
               academics_list = []
               for subtopic in topic: # Iterate through each dictionary in the topic
                  academicEligibility, academicEligibilityValue = subtopic.values()
                  string = f'{academicEligibility} of {academicEligibilityValue}'
                  academics_list.append(string)
               
               info_list.append(f"{key}: {academics_list}") #,print(f"{key}: {academics_list}")
            
            
            # FINANCIAL INFORMATION +++++++++++++++++++++++++++++++++++ I HAVE NO IDEA IF THIS WORKS OR NOT +++++++++++++++++++++
            elif (key == 'financialInformation'):
               
               financialInformation_list = []
               for subtopic in topic: # Iterate through each dictionary in the topic
                  financialEligibilityCriteria, financialEligibilityAmount = subtopic.values()
                  string = f'{financialEligibilityCriteria}: {financialEligibilityAmount}'
                  financialInformation_list.append(string)
               
               info_list.append(f"{key}: {financialInformation_list}") #,print(f"{key}: {financialInformation_list}")
            
            
            # AGE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            elif (key == 'age'):
               
               maximumAgeRequirement, minimumAgeRequirement = topic.values()
               if (maximumAgeRequirement == minimumAgeRequirement): ages = maximumAgeRequirement
               elif (maximumAgeRequirement == None and minimumAgeRequirement == None): ages = 'None'
               elif (maximumAgeRequirement != None and minimumAgeRequirement == None): ages = f'{maximumAgeRequirement} or below'
               elif (maximumAgeRequirement == None and minimumAgeRequirement != None): ages = f'{minimumAgeRequirement} or above'
               elif (maximumAgeRequirement != None and minimumAgeRequirement != None): ages = f'{minimumAgeRequirement}-{maximumAgeRequirement}'
               else: ages = '???'

               info_list.append(f"{key}: {ages}") #,print(f"{key}: {ages}")
            
            # EVERYTHING ELSE (Pretty sure it's just ApplicationRestriction now) ++++++++++++++++++++++++++++++++++++++++++++++++
            else:
               for subtopic in topic: # Iterate through each dictionary in the topic
                  for Key, value in subtopic.items(): # Iterate through each element in the dictionary
                     if (value == None): value = "None"
                     info_list.append(f"{key}: {value}") #,print(f"{key}: {value}")

         # (If topic is None)
         else: info_list.append(f"{key}: None") #,print(f"{key}: None")
      
   else:
      info_list = [f"\nSCRIPT TAG NOT FOUND ({url})"]
      print(f"\nSCRIPT TAG NOT FOUND ({url})")
   
   return info_list


# Sometimes there's a random extra hyphen in the URLs, rendering some of the processed URLs as invalid
# This function tries all possible values of the extra hyphens to fix that. Brute forcing always works, kids
def notWorky(url):
   tries = 0
   try:
      while tries < 20: # Stops it from looping forever and eventually gives up
         info_list = scholarSorter(url)
         if info_list != "Broken URL":
            return info_list
         
         hyphen_indices = [i for i, char in enumerate(url) if char == "-"]
         url_variations = []
         
         # Generate variations with an extra hyphen
         for i in hyphen_indices:
            variation = url[:i] + "-" + url[i:]
            url_variations.append(variation)
         
         # Generate variations with a missing hyphen
         for i in range(len(url) + 1):
            variation = url[:i] + url[i+1:]
            url_variations.append(variation)
         
         # Try each variation
         for variation in url_variations:
            info_list = scholarSorter(variation)
            if info_list != "Broken URL":
               return info_list
         tries += 1
   except:
      return ["Sorry! Something went wrong!"]


scholar_number = 1

# WRITE INFO INTO TEXT
with open("filteredScholarships.txt", 'r', encoding="utf-8") as file:
   with open("rawOutput.txt", 'w', encoding="utf-8") as f:
      for url in file.readlines():
         
         info_list = scholarSorter(url)
         if (info_list == "Broken URL"):
            info_list = notWorky(url)
         
         # Output
         for element in info_list:
            f.write(f'{element}\n')
         
         # Additional Data
         url = url.rstrip('\n')
         
         if (len(info_list) != 28): # Check if info_list is complete or not
            f.write(f'Num: {scholar_number} | URL: {url} | Len: {len(info_list)} -- NOT ACCEPTABLE LENGTH!\n')
         else:
            f.write(f'{scholar_number} | URL: {url} | Len: {len(info_list)}\n')

         scholar_number += 1
         
         f.write('\n'), print()
         #input()