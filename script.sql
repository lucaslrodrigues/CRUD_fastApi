-- use userData;
create table users(
	id serial primary key,
	name varchar(45),
	login varchar(45),
	senha varchar(45)
);