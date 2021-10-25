from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="geoapiExercises")


def get_location(lat, long):
    try:
        return geolocator.reverse(str(lat)+","+str(long)).raw['address']
    except Exception as e:
        print(e, flush=True)
        return {'error': 'No location found or invalid coordinates.'}


# if __name__ == '__main__':
#     lat = '-19.808054'
#     lat = '3.262626'
#     long = '-48.066019'
#     long = '-9.463663'
#
#     x = get_location(lat, long)
#
#     print(x)
