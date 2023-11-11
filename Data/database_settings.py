import aiosqlite

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        
    async def create_tables(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER,
                    username TEXT,
                    start_time datetime,
                    end_time datetime,
                    month_paid INTEGER,
                    real_paid INTEGER
                )
            """)
            await db.commit()
            
    async def create_user(self, tg_id:int, username:str):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (tg_id, username, None, None, 0, 0))
            await db.commit()
    
    async def get_user(self, tg_id:int):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute("SELECT * FROM users WHERE user_id = ?", (tg_id,))
            return await cursor.fetchone()[0]
        
db = DB('database.db')