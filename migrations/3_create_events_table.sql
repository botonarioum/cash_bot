create table event
(
	id serial not null,
	title varchar(255) not null,
	price int default 0 not null,
	channel_id int not null constraint event_channel_id_fk references channel
);

create unique index event_id_uindex
	on event (id);

alter table event
	add constraint event_pk
		primary key (id);
