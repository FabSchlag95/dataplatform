CREATE SCHEMA IF NOT EXISTS llm AUTHORIZATION supabase_admin;

-- allow the backend/client role to see and use the schema
GRANT USAGE ON SCHEMA llm TO authenticated;
GRANT CREATE ON SCHEMA llm TO authenticated;