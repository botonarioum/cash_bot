create table transition
(
  id         serial                              not null,
  channel_id int                                 not null,
  status     varchar(10)                         not null,
  created_at timestamp default current_timestamp not null
);

create unique index transition_id_uindex
  on transition (id);

alter table transition
  add constraint transition_pk
    primary key (id);

alter table transition
  add constraint transition_channel_id_fk
    foreign key (channel_id) references channel;
