-- Table creation
create table if not exists example_table (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  created_at timestamptz default now()
);

-- Insertion
insert into example_table (title)
values ('example_title_for_first_entry');