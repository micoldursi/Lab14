import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._grafo = nx.DiGraph()

    def getAllStores(self):
        stores = DAO.getAllStores()
        return stores

    def buildGraph(self, giorni):
        self._nodes = DAO.getAllNodes()
        for n1 in self._nodes:
            for n2 in self._nodes:
                if (n1 != n2):
                    if n1.order_date-n2.order_date < giorni : # n1 piu recente
                        #metto arco orientato dal piu recente
                    elif n2.order_date-n1.order_date < giorni : #n2 piu recente

        pass
