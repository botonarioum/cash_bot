alter table event
	add created_at timestamp default current_timestamp not null;
