

#Form "key" : [IG Name, Capacity, Enrollment #]
class IG:
    def __init__(self, key, name, capacity=10, twoHour = False):
        self.key = key
        self.name = name
        self.capacity = capacity
        self.camperRoster = []
        self.twoHour = twoHour
    def reset(self):
        self.camperRoster = []
    

# Create IG objects for jrP1
jrP1 = {
    'A': IG('A', 'Kayaking', 13),
    'B': IG('B', 'Navy Seals', 16),
    'C': IG('C', 'Wave Riders', 12),
    'D': IG('D', 'Arts & Crafts', 20),
    'E': IG('E', 'Good Vibes', 10),
    'F': IG('F', 'Court Sports', 16),
    'G': IG('G', 'OP', 10, True),  # Assuming combining Junior and Senior OP
    'H': IG('H', 'Farm', 20, True)
}

# Create IG objects for jrP2
jrP2 = {
    'A': IG('A', 'Swimming', 14),
    'B': IG('B', 'Paddleboarding', 10),
    'C': IG('C', 'Special OPs', 24),
    'D': IG('D', 'Nature', 11),
    'E': IG('E', 'Field Sports', 18),
    'F': IG('F', 'Pickleball', 14)
}

srP1 = {
    'A': IG('A', 'Swimming', 14),
    'B': IG('B', 'Paddleboarding', 10),
    'C': IG('C', 'Burgess Special Ops', 24),
    'D': IG('D', 'Nature', 11),
    'E': IG('E', 'Field Sports', 18),
    'F': IG('F', 'Pickleball', 14),
    'G': IG('G', 'Volleyball', 12),
    'H': IG('H', 'OP', 10, True),  # Assuming combining Junior and Senior OP
    'I': IG('I', 'Sailing', 9, True)
}

srP2 = {
    'A': IG('A', 'Kayaking', 13),
    'B': IG('B', 'Navy Seals', 16),
    'C': IG('C', 'Wave Riders', 12),
    'D': IG('D', 'Arts & Crafts', 20),
    'E': IG('E', 'Good Vibes', 10),
    'F': IG('F', 'Court Sports', 16),
    'G': IG('G', 'Volleyball', 12)
}



# Displaying the activities to verify
for key, activity in jrP1.items():
    print(f"Key: {activity.key}, Name: {activity.name}, Capacity: {activity.capacity}, Camper Roster: {activity.camperRoster}")

for key, activity in jrP2.items():
    print(f"Key: {activity.key}, Name: {activity.name}, Capacity: {activity.capacity}, Camper Roster: {activity.camperRoster}")
