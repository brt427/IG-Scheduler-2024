import csv

def writeData(optimalSchedule):


    with open('optimal_schedule.csv', 'w', newline='') as csvfile:
        fieldnames = ['Camper ID', 'IG1', 'IG2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the optimal schedule details
        for camper in optimalSchedule.camperList:
            writer.writerow({
                'Camper ID': camper.id,
                'IG1': camper.ig1,
                'IG2': camper.ig2
            })

    print(f'Optimal schedule saved to optimal_schedule.csv with score: {optimalSchedule.score}')