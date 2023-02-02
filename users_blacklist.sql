create table users_blacklist (
    id int not null primary key,
    email varchar(500) not null,
    game_id int not null,
    reason varchar(500) not null
)