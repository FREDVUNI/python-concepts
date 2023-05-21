import math

def dist(ref1, ref2):
    x1, y1 = coordinates(ref1)
    x2, y2 = coordinates(ref2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance * 0.5

def coordinates(reference):
    x = ord(reference[0]) - ord('A') + 1 
    y = int(reference[1:])
    return x, y

def validate_reference(reference):
    if len(reference) < 2 or not reference[0].isupper() or not reference[1:].isdigit():
        return False
    return True

def trips(references):
    total_distance = 0.0
    for i in range(len(references) - 1):
        ref1 = references[i]
        ref2 = references[i + 1]
        if not validate_reference(ref1) or not validate_reference(ref2):
            return "Bad reference: {}".format(ref1 if not validate_reference(ref1) else ref2)
        dist_value = dist(ref1, ref2)
        total_distance += dist_value
    return "Total distance = {} km".format(total_distance)

trip_references = input("Enter trip map references: ").split()

result = trips(trip_references)
print(result)
