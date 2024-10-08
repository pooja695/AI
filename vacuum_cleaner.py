************************************************** 
                      Code

def vacuum_cleaner():
    print("Im Vacuum cleaner")
    rooms = {
        'A': input("Is room A dirty or clean? (dirty/clean): ").strip().lower(),
        'B': input("Is room B dirty or clean? (dirty/clean): ").strip().lower(),
        'C': input("Is room C dirty or clean? (dirty/clean): ").strip().lower()
    }

    current_location = input("\nWhere is the vacuum cleaner now? (A/B/C): ").strip().upper()

    if current_location not in rooms:
        print("Invalid location! Please choose A, B, or C.")
        return

    while True:

        if rooms[current_location] == 'dirty':
            print(f"The room {current_location} is dirty. Vacuuming now...")
            rooms[current_location] = 'clean'  
        else:
            print(f"The room {current_location} is already clean. No need to vacuum here.")

        print("\nCurrent room status:")
        for room, status in rooms.items():
            print(f"Room {room} is {status}.")

        if all(status == 'clean' for status in rooms.values()):
            print("\nGreat! All rooms are clean now. Job done!")
            break

        next_room = input("\nWhich room should the vacuum cleaner move to next? (A/B/C) or type 'exit' to stop: ").strip().upper()

        if next_room == 'EXIT':
            print("Okay, stopping the vacuum cleaner. Goodbye!")
            break

        if next_room not in rooms:
            print("Invalid room choice! Please enter A, B, or C.")
        else:
            current_location = next_room  

vacuum_cleaner()


************************************
          Output
Im Vacuum cleaner
Is room A dirty or clean? (dirty/clean): dirty
Is room B dirty or clean? (dirty/clean): dirty
Is room C dirty or clean? (dirty/clean): dirty

Where is the vacuum cleaner now? (A/B/C): B
The room B is dirty. Vacuuming now...

Current room status:
Room A is dirty.
Room B is clean.
Room C is dirty.

Which room should the vacuum cleaner move to next? (A/B/C) or type 'exit' to stop: A
The room A is dirty. Vacuuming now...

Current room status:
Room A is clean.
Room B is clean.
Room C is dirty.

Which room should the vacuum cleaner move to next? (A/B/C) or type 'exit' to stop: B
The room B is already clean. No need to vacuum here.

Current room status:

Current room status:
Room A is clean.
Room B is clean.

Current room status:
Room A is clean.
Room B is clean.

Current room status:
Room A is clean.
Room B is clean.

Current room status:
Room A is clean.
Room B is clean.
Room C is dirty.

Current room status:
Room A is clean.
Room B is clean.

Current room status:

Current room status:

Current room status:

Current room status:

Current room status:
Room A is clean.

Current room status:

Current room status:
Room A is clean.
Room B is clean.

Current room status:
Room A is clean.

Current room status:
Room A is clean.

Current room status:
Room A is clean.

Current room status:
Room A is clean.

Current room status:
Room A is clean.
Room B is clean.

Current room status:
Room A is clean.
Room B is clean.
Room C is dirty.

Current room status:
Room A is clean.
Room B is clean.
Room C is dirty.
Current room status:
Room A is clean.
Room B is clean.
Room C is dirty.

Room B is clean.
Room C is dirty.

Which room should the vacuum cleaner move to next? (A/B/C) or type 'exit' to stop: c
The room C is dirty. Vacuuming now...

Current room status:
Room C is dirty.

Which room should the vacuum cleaner move to next? (A/B/C) or type 'exit' to stop: c
The room C is dirty. Vacuuming now...

Current room status:
Which room should the vacuum cleaner move to next? (A/B/C) or type 'exit' to stop: c
The room C is dirty. Vacuuming now...

Current room status:
Room A is clean.
Room A is clean.
Room B is clean.
Room B is clean.
Room C is clean.

Great! All rooms are clean now. Job done!
