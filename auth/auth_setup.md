## Create new bucket
1. In Supabase Studio, go to Storage > New bucket > Enter the name
2. Disable public bucket
3. Go to additional configurations > restrict file upload size for bucket and allowed mime types as required
4. and click 'Save'

## Create Users
1. In Supabase Studio UI, go to Authentication > Add user > Create new user (check 'Auto Confirm User' when adding team members so that the email confirmation process is skipped)
2. User will be added to Authentication Database with email address and password

## Enable access policies
### Set up Row Level Security (RLS) for tables:
RLS must be enabled for:
- ALL tables in schema "public"
- The table "storage.objects"

To activate RLS, execute the following command in the Supabase Studio SQL editor (top right): ```ALTER TABLE {schemaname.tablename} ENABLE ROW LEVEL SECURITY;```

### Set up access policies for buckets:
Each bucket file equals an entry in storage.objects table, so bucket policies are implemented on this table.
1. RLS needs to be activated for storage.objects (see _Set up Row Level Security (RLS) for tables_).
2. Run commands from policy_bucket_access.sql in Supabase Studio SQL editor (top right), adjust auth.uid to users which are intended to access the bucket (uid for each user can be found in Auth Table)
3. The functionality can be tested by running restricted_bucket_access_test.py
### View active access policies for buckets
1. In Supabase Studio UI, go to Authentication > Policies
2. Choose Schema "storage" > scroll to "objects"

Note:
- SERVICE_ROLE_KEY is only for admins as it grants full access
- ANON_KEY is for individual users and grants access to all tables / files which are not explicitly secured by RLS / policy

For further information on authentication visit the [supabase docs](https://supabase.com/docs/guides/storage/security/access-control)