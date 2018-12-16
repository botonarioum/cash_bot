create table area
(
	id serial not null,
	title varchar(255) not null,
	token varchar(255) not null
);

create unique index area_id_uindex
	on area (id);

create unique index area_token_uindex
	on area (token);

alter table area
	add constraint area_pk
		primary key (id);
