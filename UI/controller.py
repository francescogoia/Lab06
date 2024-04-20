from time import strftime

import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._model.initialize()

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fill_anno(self):
        return self._model._years
    def fill_brand(self):
        return self._model._product_brands

    def get_top_vendite(self, e):
        anno = self._view._dd_anno.value
        brand = self._view._dd_brand.value
        retailer = self._view._dd_retailer.value
        result = self._model.get_top_vendite(anno, brand, retailer)
        for i in result:
            self._view.txt_result.controls.append(ft.Text(f"Data: {i['Date']}; "
                                                          f"Ricavo: {i['Ricavo']}; "
                                                          f"Retailer: {i['Retailer_code']}; "
                                                          f"Product: {i['Product_number']}"))
        self._view.update_page()

    def get_analisi_vendite(self, e):
        anno = self._view._dd_anno.value
        brand = self._view._dd_brand.value
        retailer = self._view._dd_retailer.value
        result = self._model.get_analisi_vendite(anno, brand, retailer)
        for i in result:
            if i == "Nessun risultato":
                self._view.txt_result.controls.append(ft.Text("Nessun risultato"))
            else:
                self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite: \n"
                                                          f"Giro d'affari: {i[1]} \n"
                                                          f"Numero vendite: {i[0]} \n"
                                                          f"Numero retailer coinvolti: {i[2]} \n"
                                                          f"Numero di prodotti coinvolti: {i[3]}"))
        self._view.update_page()

