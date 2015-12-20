"""
Clients for various grocery startups APIs e.g. PepperTap, BigBasket, ZopNow,
NaturBasket.
"""

import requests

PEPPERTAP_CATEGORIES = {
	
	"Breakfast": "1",
	"Fruits & Vegetables": "2",
	"Drinks & Beverages": "3",
	"Health & Beauty": "4",
	"Cooking Essentials": "5",
	"Home Supplies & Utilities": "6",
	"Baby Needs": "7",
	"Dairy": "64",
	"Instant Foods": "66",
	"Snack Foods": "67",
}

ZONE_ID = "81"


class PepperTapClient(object):
	def __init__(self):
		self.categories = PEPPERTAP_CATEGORIES

	def get_catalogue(self, category, zone=ZONE_ID):
		r = requests.get("http://api.peppertap.com/catalogue/product_list/?classification_id=" + 
							str(category) + "&zone_id=" + str(zone))
		data = r.json()
		dirty_product_list = data['pl']
		cleaned_product_list = []

		for product in dirty_product_list:
			cleaned_product = self._cleanup(product)
			cleaned_product_list.append(cleaned_product)
		return cleaned_product_list
		    

	def _cleanup(self, product):
		result = []
		# process and clean
		items = product['ps']
		title = product['tle']
		typ = product['typ']

		for item in items:
			cleaned_item = {}
			cleaned_item['quantity'] = item['da']
			cleaned_item['price'] = item['sp']
			cleaned_item['mrp'] = item['mrp']
			cleaned_item['name'] = title
			cleaned_item['typ'] = typ
			result.append(cleaned_item)

		return result




