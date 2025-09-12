# First steps for setting up and filling the data_platform
## 1. Setting up the project
- Clone the code from the Github repository to the desired destination
- Open the project and run the following commands:
    ```
    # Switch to the data_platform directory
    cd data_platform
    # Pull the latest images
    docker compose pull
    ```
- Copy the '.env.example' file to a new '.env' file at the same level as docker-compose.yml (```cp .env.example .env```)
- Adjust entries in '.env' file as indicated (the real '.env' file will never be checked into the Github Repository!)
- Run the following command:
    ```
    # Start doker services (in detached mode)
    docker compose up -d
    ```
- The dashboard UI (Supabase Studio) is now available and can locally be accessed at http://localhost:8000 (take required credentials DASHBOARD_USERNAME and DASHBOARD_PASSWORD from '.env' file)
## 2. Adding users
- In Supabase Studio UI, go to Authentication > Add user > Create new user (check 'Auto Confirm User' when adding team members so that the email confirmation process is skipped)
- User will be added to Authentication Database with email address and password
## 3. Creating record-based storage
### 3.1 Standard table
- In Supabase Studio UI, go to Database > SQL editor (top right)
- Enter commands from table_creation.sql to add first example table, modified individually if necessary
### 3.2 Table with vector storage
- In Supabase Studio UI, go to Database > SQL editor (top right)
- Enter commands from vector_table_creation.sql to add first example table with vector data type, modified individually if necessary
## 4. Creating file-based storage
- In Supabase Studio, go to Storage > New bucket > Enter the name and click 'Save'
- Add files using the upload button or drag and drop