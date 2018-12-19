alter table channel
	add partner_id int;

alter table channel
	add constraint channel_channel_id_fk
		foreign key (partner_id) references channel;
