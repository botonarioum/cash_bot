create table events
(
	id serial not null,
	title varchar(255) not null,
	price int default 0 not null,
	channel_id int not null constraint events_channel_id_fk references channel
);

create unique index events_id_uindex
	on events (id);

alter table events
	add constraint events_pk
		primary key (id);
