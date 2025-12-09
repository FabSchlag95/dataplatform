CREATE SCHEMA IF NOT EXISTS mlflow AUTHORIZATION supabase_admin;
GRANT USAGE, CREATE ON SCHEMA mlflow TO supabase_admin;


CREATE SCHEMA IF NOT EXISTS creator AUTHORIZATION supabase_admin;

GRANT USAGE ON SCHEMA creator TO anon, authenticated, service_role;
GRANT ALL ON ALL TABLES IN SCHEMA creator TO anon, authenticated, service_role;
GRANT ALL ON ALL ROUTINES IN SCHEMA creator TO anon, authenticated, service_role;
GRANT ALL ON ALL SEQUENCES IN SCHEMA creator TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA creator GRANT ALL ON TABLES TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA creator GRANT ALL ON ROUTINES TO anon, authenticated, service_role;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA creator GRANT ALL ON SEQUENCES TO anon, authenticated, service_role;