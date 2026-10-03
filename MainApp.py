import re
from Utils import parse_coord,findPlacements
from DiscoZooSolver import DiscoZooSolver
from DiscoZooState import DiscoZooState
from Animals import *
print("Choose an animal from the available regions, or add your own, custom tiles!!")

def pickFromRegion():
    print("Available Regions:",", ".join(r.capitalize() for r in REGIONS.keys()))
    print("(Type \"menu\" anytime to go back to the main selection menu)")
    
    while True:
        print("Available Regions:",", ".join(r.capitalize() for r in REGIONS.keys()))
        usrChoice = input("Pick a region: ").upper().strip()
        if (usrChoice in REGIONS):
            AnimalEnum = REGIONS[usrChoice]

            print(f"Animals in {usrChoice.capitalize()}:")
            for i,a in enumerate(AnimalEnum,1):
                print(f"{i}. {a}")

            animal_list = list(AnimalEnum)
            while True:
                usrAnimal = input("Pick your animal (name or number), or enter \"0\" or \"menu\" to go back to region selection: ").upper().strip()
                if usrAnimal == "0" or usrAnimal == "MENU":
                    break
                if usrAnimal.isdigit():
                    idx = int(usrAnimal) - 1
                    if 0<=idx<len(animal_list):
                        return animal_list[idx].value
                    else:
                        print("Number out of range! Pick a valid animal.")
                else:
                    try:
                        finalAnimal = AnimalEnum[usrAnimal]
                        return finalAnimal.value
                    except KeyError:
                        print("Animal does not exist! Pick a valid animal.")
        elif usrChoice == "MENU":
            return None
        else:
            print("The region does not exist! Pick a valid region.")
        

    
        
    


def customTileInput():
    print("Enter the tiles of your choice in the format (x,y)")
    print("Remember that a row or column goes up to 5.")
    print("You can enter up to 5 tiles, and at least 2 tiles. Press enter anytime to stop adding tiles.")

    pattern = []
   
    while len(pattern)<5:
        prompt = f"Enter tile {len(pattern) + 1}"
        if len(pattern)>=2:
            prompt+=", or press enter to exit"
        tileIn = input(prompt+": ").strip()
        if not tileIn:
            if (len(pattern)<2):
                print("You have to enter at least two tiles!!")
                continue
            break

        tile = parse_coord(tileIn,5)

        if not tile:
            print("Invalid Tile Format!! Use (row, col) between 1 and 5.")
            continue

        zero_indexed_tile = (tile[0]-1, tile[1]-1)

        if (zero_indexed_tile in pattern):           
            print("You have already given this tile!")
            continue

        pattern.append(zero_indexed_tile)
            
            
            
        
            

    return pattern
        

def getSolution(pattern):
    replacements = findPlacements(pattern)

    initialState = DiscoZooState(None, replacements, None)

    solution = DiscoZooSolver.aStarSolver(initialState)

    if solution is not None:
        print("Optimal Clicks Found!!!\n")
        DiscoZooSolver.backtrackUI(solution)
    else:
        print("No solution found...")

while (True):
    print("1. Custom Tile Input")
    print("2. Choose an Animal from a Region")
    choice = input("Pick: ")
    
    if (choice=="1"):
        customTileInput()
    elif (choice=="2"):
        pattern = pickFromRegion()
        
        getSolution(pattern)
        
        

















