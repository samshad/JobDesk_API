from geopy.geocoders import Nominatim
from geo_location import get_location


geolocator = Nominatim(user_agent="geoapiExercises")


def is_location(x):
    location = geolocator.geocode(x)
    return location


if __name__ == "__main__":
    x = is_location('4452 Itingen BL')
    if x is not None:
        y = get_location(x.raw['lat'], x.raw['lon'])
        print("valid location")
        print(x.raw)
        print(y)
        # {'Finance': 1, 'Globally': 1, 'Warsaw â€': 1, 'Warsaw': 2, 'Very': 1, 'Alcon Polska': 1, 'Collaboration': 1, 'Multisport': 1, 'Brand': 1, 'Marynarska Street': 1, 'Proven': 1, 'Strong': 1}
