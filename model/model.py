from database import dayly_sales_Dao, retailer_Dao, product_Dao
from database.DAO import DAO

class Model:
    def __init__(self):
        self._years = []
        self._product_brands = []
    #    self._retailer_names = []
        self._diz_retailers = DAO.get_retailers()

    def initialize(self):
        self.add_years()
        self.add_product_brands()



    def add_years(self):
        for anno in DAO.get_years():
            self._years.append(anno['year(`Date`)'])

    def add_product_brands(self):
        for marchio in DAO.get_brands():
            self._product_brands.append(marchio['Product_brand'])

    def get_top_vendite(self, anno, brand, retailer_code):
        DAO.get_top_vendite(anno, brand, retailer_code)
