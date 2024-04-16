from database.DB_connect import DBConnect


class Retailer_Dao:
    def __init__(self):
        pass

    @staticmethod
    def get_names(self):
        self.connessione = DBConnect.get_connection()
        self._cursore = self.connessione.cursor(dictionary=True)
        query_brand = """select distinct Retailer_name 
                            from go_retailers gr """
        self._cursore.execute(query_brand)
        self._rows = self._cursore.fetchall()
        self._lista_names = []
        for row in self._rows:
            self._lista_names.append(row)

        self._cursore.close()
        self.connessione.close()

if __name__ == "__main__":
    rDao = Retailer_Dao()
    rDao.get_names()
    for i in rDao._lista_names:
        print(i)