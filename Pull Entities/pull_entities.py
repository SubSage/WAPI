import json
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key="e0cd161378deaeff0567c6a3e0c9c3a3953f20b9")

class Watson:
    #takes a url and returns a json document with the entities mentioned
    def pull_entities ( self, page ):
        return json.loads(json.dumps(alchemy_language.entities(
        url = page, sentiment = 1)));

    def pull_entities_from_text ( self, words ):
        return json.loads(json.dumps(alchemy_language.entities(
        text = words, sentiment = 1)));

    #takes a json document (e.g. from pull_entities) and returns a dictionary of mentioned
    #"People" and their associated relevances to the main topic
    def get_people ( self, pagedata ):
        data = pagedata["entities"]
        people = [[item["text"],item["relevance"], item["sentiment"]["type"]] for item in data if item["type"] == "Person"]
        return people;

    #same but with organizations
    def get_organizations ( self, pagedata ):
        data = pagedata["entities"]
        orgs = [{item["text"]:item["relevance"]} for item in data if item["type"] == "Organization"]
        return orgs;

    #same but with countries
    def get_countries ( self, pagedata ):
        data = pagedata["entities"]
        countries = [{item["text"]:item["relevance"]} for item in data if item["type"] == "Country"]
        return countries;

    #same but with locations
    def get_cities( self, pagedata ):
        data = pagedata["entities"]
        cities = [{item["text"]:item["relevance"]} for item in data if item["type"] == "City"]
        return cities;

    #same but with geographic features (e.g. mountains)
    def get_geofeatures( self, pagedata ):
        data = pagedata["entities"]
        feats = [{item["text"]:item["relevance"]} for item in data if item["type"] == "GeographicFeature"]
        return feats;

