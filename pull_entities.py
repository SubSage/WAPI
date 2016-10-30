import json
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='d6d5a86057cd102193772643841b7bf4f5231bda')

#takes a url and returns a json document with the entities mentioned
def pull_entities ( page ):
    return json.loads(json.dumps(alchemy_language.entities(
    url = page,
    sentiment=1),
    indent=2));

#takes a json document (e.g. from pull_entities) and returns a dictionary of mentioned
#"People" and their associated relevances to the main topic
def get_people ( pagedata ):
    data = pagedata["entities"]
    people = [{item["text"]:item["relevance"]} for item in data if item["type"] == "People"]
    return people;

#same but with organizations
def get_organizations ( pagedata ):
    data = pagedata["entities"]
    orgs = [{item["text"]:item["relevance"]} for item in data if item["type"] == "Organization"]
    return orgs;

#same but with countries
def get_countries ( pagedata ):
    data = pagedata["entities"]
    countries = [{item["text"]:item["relevance"]} for item in data if item["type"] == "Country"]
    return countries;

#same but with locations
def get_cities( pagedata ):
    data = pagedata["entities"]
    cities = [{item["text"]:item["relevance"]} for item in data if item["type"] == "City"]
    return cities;

#same but with geographic features (e.g. mountains)
def get_geofeatures( pagedata ):
    data = pagedata["entities"]
    feats = [{item["text"]:item["relevance"]} for item in data if item["type"] == "GeographicFeature"]
    return feats;
