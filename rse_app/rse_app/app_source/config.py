# -*- coding: utf-8 -*-
import sys

# sys.path.insert(0, '/home/ubuntu/ppi_core/backend/src/utilities/')
# from persistence.hdfs_config import *

DEBUG = True

DATABASES = {"estimated": 'ESTIMATED', "reduced": 'REDUCED', "weighted": 'WEIGHTED'}

DATABASES_CATALOGO = [{"text": "Estimated", "id": "estimated"}, {"text": "Reduced", "id": "reduced"},
                      {"text": "Weighted", "id": "weighted"}]

COUNTRIES = [{"text": "Australia", "id": "AUS"}, {"text": "Brazil", "id": "BRA"}, {"text": "New Zealand", "id": "NZL"}]

CURRENCIES = {'response': [{"id": "SDR", "text": "SDR"}, {"id": "EUR", "text": "EUR"},
                           {"id": "NC", "text": "NATIONAL CURRENCY"}], 'error': ""}
DEFAULT_CURRENCY = "EUR"

YEARS = [{"id": "2017", "text": "2017"}, {"id": "2016", "text": "2016"}, {"id": "2015", "text": "2015"},
         {"id": "2014", "text": "2014"}, {"id": "2013", "text": "2013"}, {"id": "2012", "text": "2012"},
         {"id": "2011", "text": "2011"}]

LEVEL_OF_GOVERMENTS = [{"id": "Not defined", "text": "Not defined"}, {"id": "Central", "text": "Central"},
                       {"id": "Sub-central", "text": "Sub-central"}, {"id": "Other entities", "text": "Other entities"}]

CONTRACT_TYPES = [{"id": "Goods", "text": "Goods"}, {"id": "Services", "text": "Services"},
                  {"id": "Works", "text": "Works"}]

PROCUREMENT_METHODS = [{'id': "Not defined", 'text': "Not defined"}, {"id": "Limited", "text": "Limited"},
                       {"id": "Open", "text": "Open"}, {"id": "Others", "text": "Others"}, {"id": "Selective",
                                                                                            "text": "Selective"}]




STATIC_ZIP = "/static/zips"
STATIC_EXCEL = "/static/excels"


MAX_SIZE = 1 * 10 ** 9

ORDERED_GROUPS = ["year", "level_of_government", "sublvlgov", "contract_type", "procurement_method",
                  "overthreshold", "division", "supplier_country", "supplier_geographic_area",
                  "contract_domestic", "country_ultimate_parent", "area_ultimate_parent", "contract_mode"]


HEADERS_DEBUG = ['Lvl Gov', 'Cont Type', 'Procur Met', 'N contracts', 'Aggregated Value', 'Typical Deviation']

RESULTS_DEBUG = [['Central', 'Goods', 'Limited', 8202, '4375459832.59', '26820383.9126'],
                 ['Other entities', 'Goods', 'Limited', 350459, '64354411451.80', '8322676.2553'],
                 ['Central', 'Goods', 'Open', 28647, '3520612094.80', '1827926.2912'],
                 ['Other entities', 'Goods', 'Open', 47550, '9069201906.09', '6623115.7340'],
                 ['Central', 'Services', 'Limited', 8673, '3667912072.49', '5673343.1801'],
                 ['Other entities', 'Services', 'Limited', 300220, '62520166489.89', '7355735.3760'],
                 ['Central', 'Services', 'Open', 20491, '5935740461.81', '6053469.4495'],
                 ['Other entities', 'Services', 'Open', 40340, '9816717616.94', '1829155.8938'],
                 ['Central', 'Works', 'Limited', 773, '140749886.27', '1416776.8284'],
                 ['Other entities', 'Works', 'Limited', 6127, '2146903819.14', '5570134.3622'],
                 ['Central', 'Works', 'Open', 3233, '441158693.24', '703070.1056'],
                 ['Other entities', 'Works', 'Open', 4404, '698208969.52', '668997.0488']]
