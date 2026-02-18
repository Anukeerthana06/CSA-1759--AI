# Vacuum Cleaner Problem

room = {'A': 'Dirty', 'B': 'Dirty'}
pos = 'A'

while room['A'] == 'Dirty' or room['B'] == 'Dirty':
    if room[pos] == 'Dirty':
        print(pos, ": Cleaning")
        room[pos] = 'Clean'
    else:
        pos = 'B' if pos == 'A' else 'A'
        print("Moving to", pos)

print("All rooms are clean")
