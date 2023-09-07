def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    list = []
    for name in names:
        list.append(f'Hello, my name is {name}.')
    return list

def assign_rooms(names):
    room_numbers = range(1, 9)
    list = []
    for room in room_numbers:
        list.append(f"Hello, {names[room -1]}! You'll be assigned to room {room}!")
    return list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for room in assign_rooms(names):
        print(room)
