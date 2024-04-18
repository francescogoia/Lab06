from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_years():
        connessione = DBConnect.get_connection()
        _cursore = connessione.cursor(dictionary=True)
        query_brand = """select distinct year(`Date`)
                            from go_daily_sales gds """
        _cursore.execute(query_brand)
        _rows = _cursore.fetchall()
        _lista_years = []
        for row in _rows:
            _lista_years.append(row)
        _cursore.close()
        connessione.close()
        return _lista_years

    @staticmethod
    def get_brands():
        connessione = DBConnect.get_connection()
        _cursore = connessione.cursor(dictionary=True)
        query_brand = """select distinct Product_brand 
                            from go_products gp"""
        _cursore.execute(query_brand)
        _rows = _cursore.fetchall()
        _lista_brands = []
        for row in _rows:
            _lista_brands.append(row)
        _cursore.close()
        connessione.close()
        return _lista_brands

    @staticmethod
    def get_retailers():
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)
        query_brand = """select * 
                                from go_retailers gr 
                                order by gr.Retailer_name"""
        cursore.execute(query_brand)
        rows = cursore.fetchall()
        diz_retailer = {}
        for row in rows:
            rt = Retailer(row['Retailer_code'], row['Retailer_name'], row['Type'], row['Country'])
            diz_retailer[rt.retailer_code] = rt
        cursore.close()
        connessione.close()
        return diz_retailer

    @staticmethod
    def get_top_vendite(anno, brand, retailer_code):
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)
        query = """select gds.`Date`,(gds.Unit_sale_price * gds.Quantity) as Ricavo, Retailer_code, gds.Product_number 
                    from go_daily_sales gds, go_products gp 
                    where year (gds.`Date`)  = %s and gp.Product_brand = %s and gds.Retailer_code = %s
                        and gp.Product_number = gds.Product_number 
                    order by -(gds.Unit_sale_price * gds.Quantity)
                    limit 5    
                    """
        cursore.execute(query, (anno, brand, retailer_code,))
        rows = cursore.fetchall()
        list_risultato = []
        for row in rows:
            r = row['Date'], float(row['Ricavo']), row['Retailer_code'], row['Product_number']
            list_risultato.append(r)
            print(r)
        return list_risultato


    @staticmethod
    def get_analisi_vendite(anno, brand, retailer_code):
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)
        query = """select gds.Retailer_code , sum(gds.Unit_sale_price * gds.Quantity) as turnover, year (gds.`Date`), count(gds.Retailer_code) as nrRetailers, count(gds.Product_number) as nrProducts 
                    from go_daily_sales gds , go_products gp 
                    where year (gds.`Date`)  = %s and gp.Product_brand = %s and gds.Retailer_code = %s
                        and gp.Product_number = gds.Product_number   
                            """
        cursore.execute(query, (anno, brand, retailer_code,))
        rows = cursore.fetchall()
        list_risultato = []
        for row in rows:
            r = float(row['turnover'])
            list_risultato.append(r)
            print(r)
        return list_risultato



if __name__ == "__main__":
    DAO.get_top_vendite(2016, 'TrailChef', 1258)
    DAO.get_retailers()