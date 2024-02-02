import requests
import json
(lng_origine, lat_origine) = (2.34017, 48.84635)
(lng_destination, lat_destination) = (2.35036, 48.8413)
try:
    r = requests.get(f"https://wxs.ign.fr/essentiels/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-osrm&start={lng_origine},{lat_origine}&end={lng_destination},{lat_destination}").json()
    print(r)
    print(f"Distance : {r['distance']} mètres, Durée :{r['duration']} minutes")
except Exception:
    print(f'erreur requete !')