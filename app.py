from fastapi import FastAPI
from post_data import JobData
from post_data import ProfileData
from post_data import JobTitle
from geo_location import get_location
# from get_tags import get_tags
from geotext import GeoText
from langdetect import detect
import country_code_json as get_cc
from collections import Counter
from predict_sector_title import get_sector


app = FastAPI()


@app.get('/')
def index():
    return {
        'message': 'API up and running',
        'endpoints': ['jobsector', 'job', 'profile']
    }


@app.post('/jobsector')
def get_job_details(data: JobTitle):
    data = data.dict()
    jobtitle = data['jobtitle']

    print("in jobsector => \n", jobtitle, flush=True)

    jobsectors = get_sector(jobtitle)

    print("in jobsector => \n", jobsectors, flush=True)

    ret = {
        'jobsectors': jobsectors
    }

    return ret


@app.post('/job')
def get_job_details(data: JobData):
    data = data.dict()

    print("in Job => \n", data, flush=True)

    # extracting payload
    doc = data['data']
    uid = data['uid']
    lc = data['lc']

    if len(doc) < 1:
        return {
            "error": "empty document."
        }

    lang = detect(doc)
    # tags = get_tags(doc)
    tags = []

    country_code = []
    cities = []

    if 'restriction_ISO2' in data['jsonJobLocation']:
        country_code = []
        cities = []
        if data['jsonJobLocation']['restriction_ISO2'].lower() in country_code:
            country_code = data['jsonJobLocation']['restriction_ISO2'].lower()
        else:
            country_code = []
            cities = []

    # country_code = Counter(country_code)
    # country_code = country_code.most_common(1)[0][0] if country_code else None

    if data['geoLat'] is not None and data['geoLong'] is not None:
        address = get_location(data['geoLat'], data['geoLong'])
        ret = {
            'uid': uid,
            'tags': tags,
            'lang': lang,
            'country_code': country_code,
            'cities': cities,
            'GeoAddress': address
        }

    else:
        ret = {
            'uid': uid,
            'tags': tags,
            'lang': lang,
            'country_code': country_code,
            'cities': cities
        }

    print("out Job => \n", ret, flush=True)

    return ret


@app.post('/profile')
def get_profile_details(data: ProfileData):
    data = data.dict()

    print("in Profile => \n", data, flush=True)

    # extracting payload
    doc = data['data']
    uid = data['uid']

    lang = detect(doc)
    # tags = get_tags(doc)
    tags = []
    # LOC = get_loc(doc)

    ret = {
        'uid': uid,
        'tags': tags,
        'lang': lang
    }

    print("out Profile => \n", ret, flush=True)
    return ret


"""if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)"""

# uvicorn app:app --reload

