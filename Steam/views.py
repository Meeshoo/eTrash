from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.template.response import TemplateResponse
from CSGORanks.models import CSGORanks
from Steam.models import Steam
from django.views.decorators.csrf import csrf_exempt

CSGORankClient = CSGORanks()
SteamClient = Steam()
SteamClient.updateSteamData()
    
McMitchName = SteamClient.getSteamName(settings.MITCH_STEAM_ID)
McMitchImage = SteamClient.getSteamAvatar(settings.MITCH_STEAM_ID)

CallumcaName = SteamClient.getSteamName(settings.CALLUM_STEAM_ID)
CallumcaImage = SteamClient.getSteamAvatar(settings.CALLUM_STEAM_ID)

JakeAMName = SteamClient.getSteamName(settings.JAKE_STEAM_ID)
JakeAMImage = SteamClient.getSteamAvatar(settings.JAKE_STEAM_ID)

DefaultsoundName = SteamClient.getSteamName(settings.DONGY_STEAM_ID)
DefaultsoundImage = SteamClient.getSteamAvatar(settings.DONGY_STEAM_ID)

TheScannerDarklyName = SteamClient.getSteamName(settings.SCANNER_STEAM_ID)
TheScannerDarklyImage = SteamClient.getSteamAvatar(settings.SCANNER_STEAM_ID)


@csrf_exempt
def index(request):

    if request.method == 'GET':

        ranks = CSGORankClient.getCurrentCSGORanks()

        for entry in ranks:
            if entry.name == "McMitch":
                McMitchRank = entry.rank
            elif entry.name == "Callumca":
                CallumcaRank = entry.rank
            elif entry.name == "JakeAM":
                JakeAMRank = entry.rank
            elif entry.name == "Defaultsound":
                DefaultsoundRank = entry.rank
            elif entry.name == "The Scanner Darkly":
                TheScannerDarklyRank = entry.rank

        return TemplateResponse(request, 'index.html', {
        "McMitchImage":McMitchImage, "McMitchName":McMitchName, "McMitchRank":McMitchRank,
        "DefaultsoundImage":DefaultsoundImage, "DefaultsoundName":DefaultsoundName, "DefaultsoundRank":DefaultsoundRank,
        "CallumcaImage":CallumcaImage, "CallumcaName":CallumcaName, "CallumcaRank":CallumcaRank,
        "TheScannerDarklyImage":TheScannerDarklyImage, "TheScannerDarklyName":TheScannerDarklyName, "TheScannerDarklyRank":TheScannerDarklyRank,
        "JakeAMImage":JakeAMImage, "JakeAMName":JakeAMName, "JakeAMRank":JakeAMRank,
        })

    elif request.method == 'POST':
        print("POST received, nothing to do")
        return
