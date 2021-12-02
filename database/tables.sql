create table clients(
    id serial primary key,
    surname varchar(32) not null,
    name varchar(32) not null,
    birth_date date not null
);

create table drones(
    id serial primary key,
    status integer not null,
    position_x integer not null,
    position_y integer not null,
    position_z integer not null,
    temperature integer not null,
    velocity integer not null,
    battery integer not null,
    time timestamp not null
    );

create table rents(
    id serial primary key,
    idDrone integer references drones(id),
    idClient integer references clients(id),
    start_rent timestamp not null,
    end_rent timestamp,
    cost decimal
);