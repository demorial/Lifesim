class Country:
    # doen met die wat j wil net gedink as j
    # difficulty will change gebaseer op country
    def __init__(self, country, saftyRank):
        self.country = country
        self.saftyRank = saftyRank

    def getCountry(self):
        return self.country

    def getSaftyRank(self):
        return self.saftyRank
