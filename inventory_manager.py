class InventoryManager:
    ARCHIVED = 0
    UNARCHIVED = 1
    def __init__(self, db):
        self._db = db
    def create_item(self, item, ref, quantity):
        self._db.execute(
            "INSERT INTO inventory (item, ref, quantity, archive) VALUES(?, ?, ?, ?)",
            (item, ref, quantity, self.UNARCHIVED)
        )

    def get_item_by_id(self, id):
        cur = self._db.execute("SELECT * FROM inventory WHERE id = ?", (id,))
        r = cur.fetchone()
        return {
            "id": r[0],
            "item": r[1],
            "ref": r[2],
            "quantity": r[3],
            "archive": r[4],
            "comment": r[5]
        }


    def get_archived_inventory(self):
        results = self._db.execute("SELECT * FROM inventory WHERE archive = 0")
        return [
            {
                "id": r[0],
                "item": r[1],
                "ref": r[2],
                "quantity": r[3],
                "archive": r[4],
                "comment": r[5]
            } for r in results
        ]

    def get_unarchived_inventory(self):
        results = self._db.execute("SELECT * FROM inventory WHERE archive = 1")
        return [
            {
                "id": r[0],
                "item": r[1],
                "ref": r[2],
                "quantity": r[3],
                "archive": r[4],
                "comment": r[5]
            } for r in results
        ]
