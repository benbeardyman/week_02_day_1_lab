class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, search_player):
            if search_player in self.players:
                return True
            else :
                return False
            
    def play_game(self, result):
            if result == True:
                self.points += 3
            if result == False:
                self.points += 0
