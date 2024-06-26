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
                    where year (gds.`Date`)  = COALESCE(%s, year (gds.`Date`))
                        and gp.Product_brand = COALESCE(%s, gp.Product_brand)
                        and gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                        and gp.Product_number = gds.Product_number 
                    order by -(gds.Unit_sale_price * gds.Quantity)
                    limit 5    
                    """
        cursore.execute(query, (anno, brand, retailer_code,))
        rows = cursore.fetchall()
        list_risultato = []
        if len(rows) == 0:
            list_risultato.append("Nessuna vendita")
            print("Nessuna vendita")
        else:
            for row in rows:
                list_risultato.append(row)
        cursore.close()
        connessione.close()
        return list_risultato


    @staticmethod
    def get_analisi_vendite(anno, brand, retailer_code):
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)
        query = """
                select tab1.count_key_combinations as num_sales,
                    sum(gds.Unit_sale_price * gds.Quantity) as turnover,
                    count(distinct(gds.Retailer_code)) as nrRetailers,
                    count(distinct(gds.Product_number)) as nrProducts
                from go_daily_sales gds , go_products gp,
                        (select count(*) as count_key_combinations
                        from go_daily_sales gds , go_products gp
                        where year (gds.`Date`)  = COALESCE(%s, year (gds.`Date`)) 
                              and gp.Product_brand = COALESCE(%s, gp.Product_brand)
                              and gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                              and gp.Product_number = gds.Product_number) as tab1
                where year (gds.`Date`)  = COALESCE(%s, year (gds.`Date`))
                    and gp.Product_brand = COALESCE(%s, gp.Product_brand)
                    and gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                    and gp.Product_number = gds.Product_number 
                """
        cursore.execute(query, (anno, brand, retailer_code, anno, brand, retailer_code,))
        rows = cursore.fetchall()
        list_risultato = []
        if rows[0]['num_sales'] == None:
            list_risultato.append("Nessuna vendita")
            print("Nessuna vendita")
        else:
            r = rows[0]['num_sales'], rows[0]['turnover'], rows[0]['nrRetailers'], rows[0]['nrProducts']
            list_risultato.append(r)
            print(r)
        cursore.close()
        connessione.close()
        return list_risultato



if __name__ == "__main__":
    DAO.get_top_vendite(2016, 'Seeker', 1111)
    # DAO.get_retailers()
    # DAO.get_analisi_vendite(None, 'Seeker', 1479)