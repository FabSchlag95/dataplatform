CREATE SCHEMA IF NOT EXISTS playground AUTHORIZATION supabase_admin;

-- allow the backend/client role to see and use the schema
GRANT USAGE ON SCHEMA playground TO authenticated;
GRANT CREATE ON SCHEMA playground TO authenticated;