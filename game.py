from room import Room

class Game:
    MENU = """1.) Nazwa pokoju
2.) Opis sytuacji
3.) Opis pokoju
4.) Lista dostepnych narzedzi
5.) Opis uzycia narzędzi
6.) Uzyj narzedzia
7.) Wyswietl poziom gry
8.) Wyjscie z gry
Wybierz opcje: """

    def __init__(self):
        self.level = 1
        self.rooms = []
        self.add_room(1)
        self.options = {
            "1": self.title,
            "2": self.described_sytuation,
            "3": self.described_room,
            "4": self.tools,
            "5": self.title,
        }
        self.add_room(self.level)

    def add_room(self, number_room):
        self.rooms.append(Room(number_room))
        self.rooms[0].load_room()


    def title(self):
        print("Nazwa pokoju: ", self.rooms[0].get_title())

    def described_sytuation(self):
        print(self.rooms[0].get_described_sytuation())

    def described_room(self):
        print(self.rooms[0].get_described_room())

    def tools(self):
        print(*list(self.rooms[0].get_items()))

    def start(self):
        while (selection := input(self.MENU)) != "8":
            try:
                self.options[selection]()
            except KeyError:
                print("Niepoprawna opcja, powtorz.")




if __name__ == "__main__":
    game = Game()
    game.start()