from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.sql import text

class Raw():
    TABLE = 'master.dbo.pop'
    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db

    def jsonify_results(self, collection: CursorResult) -> dict:
        results = [
            {
                "id": item.id,
                "name": item.name,
                "color": item.color
            } for item in collection]

        return {"results": results}
    
    def all(self):
        collection = self.db.session.execute(text(f"SELECT * FROM {self.TABLE}"))
        return self.jsonify_results(collection)

    def commit_refresh(self, args: dict, stm) -> dict:
        self.db.session.execute(statement=stm,params=args)
        self.db.session.commit()
        return self.all()

    def filter_by(self, pop_id: int):
        stm = text(f"SELECT * FROM {self.TABLE} WHERE id = :pop_id")
        collection = self.db.session.execute(statement=stm,params={"pop_id": int(pop_id)})
        return self.jsonify_results(collection)

    def delete_by(self, pop_id: int):
        stm = text(f"DELETE FROM {self.TABLE} WHERE id = :pop_id")
        return self.commit_refresh(args={"pop_id": int(pop_id)}, stm=stm)
    
    def insert_entry(self, pop_name: str, pop_color: str):
        args = {"pop_name": pop_name, "pop_color": pop_color}
        stm = text(f"INSERT INTO {self.TABLE}(name, color) VALUES(:pop_name, :pop_color)")
        return self.commit_refresh(args=args, stm=stm)

    def update_entry(self, pop_id: int, pop_name: str, pop_color: str):
        args = {"pop_id": pop_id, "pop_name": pop_name, "pop_color": pop_color}
        stm = text(f"UPDATE {self.TABLE} SET name=:pop_name, color=:pop_color WHERE id=:pop_id")
        return self.commit_refresh(args=args, stm=stm)
