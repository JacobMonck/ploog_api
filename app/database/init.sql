CREATE TABLE IF NOT EXISTS server_config(
    guild_id bigint UNIQUE PRIMARY KEY NOT NULL,
    prefix varchar(255) DEFAULT 'a!' NOT NULL,
    submissions_channel bigint UNIQUE,
    moderation_channel bigint UNIQUE,
    approved_channel bigint UNIQUE
);

CREATE TABLE IF NOT EXISTS reactions(
    submissions_message bigint UNIQUE PRIMARY KEY NOT NULL
)