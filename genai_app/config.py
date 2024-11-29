# app/config.py

CONFIG = {
    "matching_method": "jaro_winkler",  # Matching algorithm
    "threshold": 0.9,                  # Confidence threshold
    "top_k": 5                         # Top-k matches to consider for efficiency
}

CHOICES_URL = "https://externaldatastoreaccnt.blob.core.windows.net/takehometestdata/field_options.json"

# Caching configuration
CACHE_TIMEOUT = 3600  # Cache timeout in seconds (default: 1 hour)

# Initialize global variables
CACHED_CHOICES = None
CACHE_TIMESTAMP = 0

SCENARIOS = {
    0: {'State': 'tate_7', 'Pack_Size': 'PackSize_3', 'Category_Name': 'Categor_name_5'},
    1: {'Sub_Category_Name': 'Sub_Category_Name_45', 'Area': 'Area_29', 'SaleChanel': 'SalesChane1'},
    2: {'asdaSub_Category_Name': 'Sub_Category_Name49', 'Store': 'Stre_304'},
    3: {'Suplier': 'Supplier_1026', 'Promotion': 'Promotion_2'},
    4: {'Caihn': 'Chain_2', 'Region': 'Region_14'}
}
