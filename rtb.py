import scrapy
import json
import pymongo


def urls_brands():
    base_url = 'https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter='
    alphabet = 'ABCDEFGHIJKLMNO'
    urls = list()
    for c in alphabet:
        urls.append(base_url + c)
    return urls

def inserirmongo():
    collection_name = 'brands'
    mongo_uri='mongodb+srv://gzguidetti:password@cluster0.5ralvcb.mongodb.net/?retryWrites=true&w=majority'
    mongo_db=('crawler')
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    with open('marcas.json') as f:
        data = json.load(f)
    db[collection_name].insert_many(data)

def write_results(brands):
    sorted_brands = sorted(brands, key=lambda d: d['name'])
    jsonstring = json.dumps(sorted_brands)
    output_file = open('marcas.json', 'w')
    output_file.write(jsonstring)
    output_file.close()

class BrandsSpider(scrapy.Spider):
    name = 'brands'
    start_urls = urls_brands()
    # esta sera a lista de marcas depois do agente ter feito o trabalho.
    brands = list()

    def parse(self, response):
        for e in response.css('.rankingName'):
            brand_to_write = e.css('::text').get()
            self.brands.append({'name': brand_to_write})
            yield {'name': brand_to_write}

    def close(self, reason):
        write_results(self.brands)
        inserirmongo()
