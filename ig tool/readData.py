#Read CSV file and interpret data
import pandas as pd

# Load the CSV file
file_path = '/Users/blakethomas/Desktop/ig tool/S2W1 Sorting - S2W1 Raw Juniors.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the CSV to understand its structure
data.head(5)

#print(data.head)

class Camper:

    def __init__(self, id, jr, prefs):
        self.id = id
        self.jr= jr
        
        #Prefs for IG1 and IG2
        self.ig1Prefs = prefs[0:4] 
        self.ig2Prefs = prefs[4:8]


        self.ig1 = None 
        self.ig2 = None
        self.score = 0
    def __str__(self):
        
        return("Buddy #: %s; JR?: %s; IG1: %s, IG2: %s" %(self.id,self.jr,self.ig1,self.ig2))
    def reset(self):
        self.ig1 = None
        self.ig2 = None
       #return("Buddy #: %s; JR?: %s; IG1 Preferences: %s, IG2 Preferences: %s, IG1: %s, IG2: %s" %(self.id,self.jr, self.ig1Prefs, self.ig2Prefs,self.ig1,self.ig2))
        

#list of campers
camperList = []

#Cutoff for JR Buddy #'s
jrRange = 80

camperList = []
for index, row in data.iterrows():
    id = row['Buddy #']
    responses = row[1:].tolist()
    camperList.append(Camper(id, jrRange > id, responses))

#print(str(camperList[0]))
for camper in camperList:
    print(str(camper))