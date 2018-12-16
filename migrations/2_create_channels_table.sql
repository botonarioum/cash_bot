create table channel
(
	id serial not null constraint channel_pkey primary key,
	area_id integer not null constraint channel_area_id_fkey references area,
	channel_id integer not null,
	first_name varchar(255),
	last_name varchar(255),
	created_at timestamp not null,
	updated_at timestamp not null
);

create index channel_area_id
	on channel (area_id);
