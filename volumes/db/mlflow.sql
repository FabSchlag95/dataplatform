CREATE SCHEMA IF NOT EXISTS mlflow AUTHORIZATION supabase_admin;
GRANT USAGE, CREATE ON SCHEMA mlflow TO supabase_admin;


CREATE SCHEMA IF NOT EXISTS creator AUTHORIZATION supabase_admin;

-- allow the backend/client role to see and use the schema
GRANT USAGE ON SCHEMA creator TO authenticated;
GRANT CREATE ON SCHEMA creator TO authenticated;