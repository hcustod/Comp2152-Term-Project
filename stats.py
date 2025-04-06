class Stats:
    # Initialize game stats
    def __init__(self, username):
        self.username = username
    
        self.weapon = ""
        self.loot = []
        self.stars = 0
        self.winner = ""

     # Update each stat 
  #  def update_stats(self, weapon = None, loot = None, stars = None, winner = None):
  #      self.weapon = weapon
  #      self.loot = loot
  #      self.stars = stars
  #      self.winner = winner

    def return_stats(self):
        return self

###
#    def display_stats(self):
#        print("\n///////////////////////////////////////////\n")
#        print(f"{self.winner}")
#        print(f"{self.username}")
#    
#        print(f"weapon: {self.weapon}")
#        print(f"loot: {self.loot}")
#        print(f"stars: {self.stars}")
#        print("\n///////////////////////////////////////////\n")

#        print(self.__str__)

###
