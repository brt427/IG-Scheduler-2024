import readData
import igList
import random
import version
import copy
import writeData

"""
Created by Blake Thomas - 2024
Email brt427@gmail.com with questions
"""

masterList = readData.camperList
juniorCampers = masterList[:79]
seniorCampers = masterList[79:]
scheduleList = []

masterIGList = [igList.jrP1,igList.jrP2,igList.srP1,igList.srP2]



def scheduleIG(igList, camperList, period):
    score = 0
    var = "ig" + str(period)
    
    if period == 1:
        prefs = "ig1Prefs"
        #altPrefs = "ig2Prefs"
    else:
        prefs = "ig2Prefs"
        #altPrefs = "ig1Prefs"
        
    for camper in camperList: 
        i = 0
        currDict = igList
        try:
            while i < 4:
                if getattr(camper, "ig1") is not None and getattr(camper, "ig2") is not None:

                    score-=i
                    break
                
                if len(currDict[getattr(camper, prefs)[i]].camperRoster) < currDict[getattr(camper, prefs)[i]].capacity:  
                    
                    if currDict[getattr(camper, prefs)[i]].twoHour:
                        setattr(camper, "ig1", currDict[getattr(camper, prefs)[i]].name)
                        setattr(camper, "ig2", currDict[getattr(camper, prefs)[i]].name)
                        currDict[getattr(camper, prefs)[i]].camperRoster.append(camper)
                        #print(str(camper))
                    else:
                        setattr(camper, var, currDict[getattr(camper, prefs)[i]].name)
                        currDict[getattr(camper, prefs)[i]].camperRoster.append(camper)
                        #print(str(camper))
                        break
                else:
                    i += 1
        except KeyError as e:
                print(f"KeyError: {e} - Preference or IG not found.")
                print(camper.id)
                #i += 1
                #i += 1
        score += i
        #camper.score = score
    return score



def resetCampers():
    for camper in masterList:
        camper.reset()
        camper.reset()

    for igList in masterIGList:
        for ig in igList.values():
            ig.reset()

            
        

def scheduleAll():


    jrShuffle = shuffleList(juniorCampers)
    srShuffle = shuffleList(seniorCampers)


    totalScore = 0
    #jrP1
    totalScore+=scheduleIG(igList.jrP1,jrShuffle,1)
    #print(totalScore)

    #jrP2
    totalScore+=scheduleIG(igList.jrP2,jrShuffle[::-1],2)
    #print(totalScore)
    

    #srP1
    
    totalScore+=scheduleIG(igList.srP1,srShuffle,1)
    #print(totalScore)

    #srP2
    totalScore+=scheduleIG(igList.srP2,srShuffle[::-1],2)
    #print(totalScore)


   


    print()
    #print("Score is: " + str(totalScore))
    #check if there is space

    scheduleVersion = copy.deepcopy(version.version(masterList, masterIGList, totalScore))
    resetCampers()

    return scheduleVersion

def shuffleList(list):
    shuffled_list = sorted(list, key=lambda x: random.random())
    return shuffled_list




def main():
    iter = 10000
    for i in range(iter):
        #print(f"Run {i+1}:"
        if i%10 == 0:
            print("creating optimal solution...")
            print(f"{(i/iter)*100}%")
        #print("%")

        scheduleList.append(scheduleAll())

    sorted_versions = sorted(scheduleList, key=lambda v: v.score)

    optimalSchedule = sorted_versions[0]
    print(optimalSchedule.score)

    writeData.writeData(optimalSchedule)

    for camper in optimalSchedule.camperList:
        pass
        #print("Buddy #: %s IG1: %s IG2: %s" % (camper.id, camper.ig1, camper.ig2))

    


    '''
    # Print the sorted list to verify
    for version in sorted_versions:
        print(f"Score: {version.score}, Campers: {version.camperList}, IG Rosters: {version.igRosters}")
    '''
    

main()



#scheduleAll()

"""
print()
for key, activity in igList.jrP1.items():
    print(f"Key: {activity.key}, Name: {activity.name}, Capacity: {activity.capacity}, Camper Roster: {len(activity.camperRoster)}")
print()
for camper in masterList:
    print("Buddy #: %s IG1: %s IG2: %s" % (camper.id, camper.ig1, camper.ig2))

"""