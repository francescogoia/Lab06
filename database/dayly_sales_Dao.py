from database.DB_connect import DBConnect


class Daily_sales_Dao:
    def __init__(self):
        pass

    @staticmethod
    def get_years(self):
        self.connessione = DBConnect.get_connection()
        self._cursore = self.connessione.cursor(dictionary=True)
        query_brand = """select distinct year(`Date`)
                        from go_daily_sales gds """
        self._cursore.execute(query_brand)
        self._rows = self._cursore.fetchall()
        self._lista_years = []
        for row in self._rows:
            self._lista_years.append(row)

        self._cursore.close()
        self.connessione.close()

if __name__ == "__main__":
    ds = Daily_sales_Dao()
    ds.get_years()
    for i in ds._lista_years:
        print(i)