from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room(room_number)

    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms:{', '.join(free_rooms)}\n"
                f"Taken rooms:{', '.join(taken_rooms)}")
