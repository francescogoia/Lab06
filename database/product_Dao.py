from database.DB_connect import DBConnect


class Product_Dao:
    def __init__(self):
        pass

    @staticmethod
    def get_brands(self):
        self.connessione = DBConnect.get_connection()
        self._cursore = self.connessione.cursor(dictionary=True)
        query_brand = """select distinct Product_brand 
                        from go_products gp"""
        self._cursore.execute(query_brand)
        self._rows = self._cursore.fetchall()
        self._lista_brands = []
        for row in self._rows:
            self._lista_brands.append(row)

        self._cursore.close()
        self.connessione.close()

if __name__ == "__main__":
    pDao = Product_Dao()
    pDao.get_brands()
    for i in pDao._lista_brands:
        print(i)