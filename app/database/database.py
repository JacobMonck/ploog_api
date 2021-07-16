import asyncio
from asyncpg import Pool, create_pool

credentials = {
    "username": "postgres",
    "password": "postgres"
    }


class Database:
    pool: Pool

    async def db_init(self) -> None:
        self.pool = await create_pool(**credentials)

        with open("database/init.sql") as f:
            await self.pool.execute(f.read())

    async def sync_guild(self) -> None:
        self.pool.execute()