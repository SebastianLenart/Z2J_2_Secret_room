import pprint


class Room:
    def __init__(self, number_of_room):
        self.number_of_room = number_of_room
        self.title = None
        self.described_sytuation = None
        self.described_room = None
        self.items_help_and_answer = dict()
        self.good_answer = None

    def load_room(self):
        with open("rooms.txt", "r", encoding="utf8") as f:
            all_rooms = f.read()
            one_room_start = all_rooms.find(f"#Room_{self.number_of_room}")
            one_room_end = all_rooms.find(f"#END_ROOM_{self.number_of_room}") + len(f"#END_ROOM_{self.number_of_room}")
            one_room = all_rooms[one_room_start:one_room_end].split("#")
            self.title = one_room[2].strip()
            self.described_sytuation = one_room[3].strip()
            self.described_room = one_room[4].strip()
            self.good_answer = one_room[5].strip()
            # od 5 do len(one_room) = 10 wiec do 9 bo liczenie od 0
            for number in (range(6, len(one_room) - 1)):  # kazdy pokoj moze miec rozna liczbe przedmiotow
                item, help, answer = one_room[number].strip().split(";")
                self.items_help_and_answer[item] = [help, answer]

    def get_title(self):
        return self.title

    def get_described_sytuation(self):
        return self.described_sytuation

    def get_described_room(self):
        return self.described_room

    def get_items(self):
        return self.items_help_and_answer.keys()

    def get_items_and_help(self):
        return [{key: value[0]} for key, value in self.items_help_and_answer.items()]

    def get_items_and_answer(self):
        return [{key: value[1]} for key, value in self.items_help_and_answer.items()]

    def get_answer(self):
        return self.good_answer
