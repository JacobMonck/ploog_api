from fastapi import FastAPI, Response
from database.database import Database
from database.models import Guild

app = FastAPI()

db = Database()

@app.on_event("startup")
async def startup():
    """Connects to PostgreSQL on startup"""
    await db.db_init()


@app.get("/")
async def root():
    return Response(status_code=200)


@app.post("/guilds/{guild_id}/sync")
async def sync_guild(guild_id: int):
    await db.sync_g


@app.get("/guilds/{guild_id}/prefix")
async def get_prefix(guild_id: int):
    if cached_prefix := await cache.pool.get(f"prefix:{guild_id}"):
        print("returned from cache")
        return cached_prefix

    if database_prefix := await pool.sync_guild(guild_id):
        await cache.pool.set(f"prefix:{guild_id}", database_prefix)
        return database_prefix


@app.patch("/guilds/{guild_id}/prefix")
async def set_prefix(guild_id: int, prefix: str):
    await pool.set_prefix(guild_id, prefix)
    await cache.pool.set(f"prefix:{guild_id}", prefix)


@app.get("/guilds/{guild_id}/submissions_channel")
async def get_submissions_channel(guild_id: int):
    await pool.get_submissions_channel(guild_id)


@app.patch("/guilds/{guild_id}/submissions_channel")
async def set_submissions_channel(guild_id: int, channel_id: int):
    await pool.set_submissions_channel(guild_id, channel_id)


@app.get("/guilds/{guild_id}/moderation_channel")
async def get_moderation_channel(guild_id: int) -> None:
    await pool.get_moderation_channel(guild_id)


@app.patch("/guilds/{guild_id}/submissions_channel")
async def set_moderation_channel(guild_id: int, channel_id: int):
    await pool.set_moderation_channel(guild_id, channel_id)


@app.get("/guilds/{guild_id}/approved_channel")
async def get_approved_channel(guild_id: int) -> None:
    await pool.get_approved_channel(guild_id)


@app.patch("/guilds/{guild_id}/approved_channel")
async def set_approved_channel(guild_id: int, channel_id: int):
    await pool.set_approved_channel(guild_id, channel_id)
