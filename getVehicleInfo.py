
def getFuelLevel(json):
    return json["fuellevelpercent"]["value"]


def getLocation(json):
    location = []
    location.append(json["longitude"]["value"])
    location.append(json["latitude"]["value"])
    location.append(json["heading"]["value"])
    return location


def getTirePressures(json):
    tirePressures = []
    tirePressures.append(json["tirepressurerearleft"]["value"])
    tirePressures.append(json["tirepressurerearright"]["value"])
    tirePressures.append(json["tirepressurefrontright"]["value"])
    tirePressures.append(json["tirepressurefrontleft"]["value"])
    return tirePressures
