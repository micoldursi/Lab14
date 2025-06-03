import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._choiceDD = None



    def handleCreaGrafo(self, e):
        if self._choiceDD is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare uno store"))
            return

        giorniTxt = self._view._txtIntK.value
        if giorniTxt == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico."))
            return

        try:
            giorni = int(giorniTxt)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un intero."))
            return

        if giorniTxt <= 0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un intero positivo."))
            return

        self._model.buildGraph(self._choiceDD, giorniTxt)
        return

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def fillDDStore(self):
        stores = self._model.getAllStores()
        for store in stores:
            self._view._ddStore.options.append(
                ft.dropdown.Option(data=store,
                                   key=store.store_id,
                                    on_click=self._readDDValue))

    def _readDDValue(self, e):
        if e.control.data is None:
            print("error in reading dd")
            self._choiceDD = None
        self._choiceDD = e.control.data