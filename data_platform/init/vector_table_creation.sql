-- Enable the vector extension
create extension if not exists vector
with schema extensions;

-- Table creation
create table if not exists public.example_embeddings_table (
  id serial primary key,
  title text not null,
  body text not null,
  embedding extensions.vector(384) not null
);