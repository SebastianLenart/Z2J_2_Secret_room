from room import Room

class Game:
    def __init__(self):
        self.rooms = []
        self.add_room()

    def add_room(self):
        self.rooms.append(Room())
        self.rooms[0].load_room(1)
        self.rooms[0].get_items_and_answer()




if __name__ == "__main__":
    game = Game()