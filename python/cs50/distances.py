distances = {
    "Voyager 1": "163 AU", 
    "Voyager 2": "136",
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44 
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    
    m = convert(au)   #(distances[spacecraft])
    print(f"{m} m away")

def convert(au):
    return au * 149597870700


main()



# def main():
    # for name in distances.keys():
        # print(f"{name} is {distances[name]} AU from Earth")


# def main():
    # for distance in distances.values():
        # print(f"{distance} AU is {convert(distance)} m")
