from inventory_item import InventoryItem

class InventoryManager:
    ARCHIVED = 1
    UNARCHIVED = 0
    def __init__(self, db):
        self._db = db

    def unarchive_item(self, quantity, id):
        self._db.execute("UPDATE inventory SET archive = ?, quantity = ? WHERE id = ?", (self.UNARCHIVED, quantity, id))

    def update_item(self, id, item, ref, quantity):
        self._db.execute(
            "UPDATE inventory SET item = ?, ref = ?, quantity = ? WHERE id = ?",
            (item, ref, quantity, id)
        )

    def archive_item(self, comment, id):
        self._db.execute(
            "UPDATE inventory SET archive = ?, comment = ? WHERE id = ?",
            (self.ARCHIVED, comment, id)
        )

    def create_item(self, item, ref, quantity):
        self._db.execute(
            "INSERT INTO inventory (item, ref, quantity, archive) VALUES(?, ?, ?, ?)",
            (item, ref, quantity, self.UNARCHIVED)
        )

    def get_item_by_id(self, id):
        cur = self._db.execute("SELECT * FROM inventory WHERE id = ?", (id,))
        r = cur.fetchone()
        return InventoryItem(*r)

    def delete_item(self, id):
        self._db.execute("DELETE FROM inventory WHERE id = ?", (id,))

    def get_archived_inventory(self):
        results = self._db.execute("SELECT * FROM inventory WHERE archive = ?", (self.ARCHIVED,))
        return [InventoryItem(*r) for r in results]

    def get_unarchived_inventory(self):
        results = self._db.execute("SELECT * FROM inventory WHERE archive = ?", (self.UNARCHIVED,))
        return [InventoryItem(*r) for r in results]
