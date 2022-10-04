from django.conf import settings
import requests
import json

steamApiKey = settings.STEAM_API_KEY

steamIDs = settings.ALL_STEAM_IDS

class Steam():

    def updateSteamData(self):
        print(steamIDs)
        steamRequest = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + steamApiKey + "&steamids=" + steamIDs)
        self.steamData = json.loads(steamRequest.content)

    def getSteamAvatar(self, steamid):
        for x in range(0,5):
            steamidFromJson = self.steamData['response']['players'][x]['steamid']

            if steamidFromJson == steamid:
                return self.steamData['response']['players'][x]['avatarfull']

    def getSteamName(self, steamid):
        for x in range(0,5):
            steamidFromJson = self.steamData['response']['players'][x]['steamid']

            if steamidFromJson == steamid:
                return self.steamData['response']['players'][x]['personaname']
