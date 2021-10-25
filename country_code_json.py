from geopy.geocoders import Nominatim
from geo_location import get_location
import spacy
from collections import Counter
from geotext import GeoText


geolocator = Nominatim(user_agent="geoapiExercises")
nlp_wk = spacy.load('xx_ent_wiki_sm')


def get_loc(x):
    doc = nlp_wk(x)
    loc = []
    for ent in doc.ents:
        #print(ent, ent.label_)
        if ent.label_ == 'LOC':
            loc.append(str(ent))
    return loc


def get_country_code(doc):
    try:
        location = geolocator.geocode(doc)
        x = get_location(location.raw['lat'], location.raw['lon'])
        # print(doc, location.raw['class'], x['country_code'])
        return x['country_code']
    except Exception as e:
        # print("from 'get_country_code' exception => ", e, flush=True)
        return None


# if __name__ == '__main__':
    # print(get_country_code('The Swatch Group (Hong Kong) Limited10/F Kerry Centre683 King’s RoadQuarry BayCN-Hong Kong'))
    # loc = get_loc('The Swatch Group (Hong Kong) Limited10/F Kerry Centre683 King’s RoadQuarry BayCN-Hong Kong')
    # loc = '098632 Singapore The Dhaka Swatch Group S.E.A. (S) Pte Ltd1 Harbor Front AvenueKeppel Bay Tower #14-03/07Singapore 098632'.split()
    # print(loc)
    # cc = []
    # city = []
    # for l in loc:
    #     t = get_country_code(l)
    #     p = GeoText(l)
    #     for tmp in p.cities:
    #         city.append(tmp)
    #     if t is not None:
    #         cc.append(t)
    # yy = Counter(cc)
    # xx = yy.most_common(1)[0][0] if yy else None
    # print(xx)
    # print(city)
