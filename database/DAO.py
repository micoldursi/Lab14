from database.DB_connect import DBConnect
from model.order import Order
from model.store import Store


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllStores():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from stores"

        cursor.execute(query)

        for row in cursor:
            results.append(Store(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from orders where store_id = 1"

        cursor.execute(query)

        for row in cursor:
            results.append(Order(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getPesoArco(n1, n2):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select oi1.order_id, sum(oi1.quantity) as q1, oi2.order_id, sum(oi2.quantity) as q2
                from order_items oi1, order_items oi2 
                where oi1.order_id = 1 and oi2.order_id  = 4"""

        cursor.execute(query)

        for row in cursor:
            results.append(row["q1"] + row["q2"]) #peso tot

        cursor.close()
        conn.close()
        return results
