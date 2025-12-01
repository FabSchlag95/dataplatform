# Supabase Docker

## NGINX
To set up the proxy host, first go to http://172.17.5.77:81/
and log in with user credentials, given in .env.nginx. 

Then add a proxy host for `http://scalec-supabase-dev.th-brandenburg.de/`;

Add this to custom proxy host:

`
location / {
  auth_basic "Restricted";
  auth_basic_user_file /data/access/1;
  proxy_set_header  Authorization $http_authorization;
  proxy_pass_header Authorization;
  proxy_pass $forward_scheme://studio:3000;
}

location /mlflow/api/ {
    proxy_pass http://mlflow_server:5000/api/;
    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Port $server_port;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Prefix /mlflow/api/;
    client_max_body_size 100M;
}

location /mlflow {
    auth_basic "Restricted";
    auth_basic_user_file /data/access/1;
    proxy_pass http://mlflow_server:5000;
    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Port $server_port;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Prefix /mlflow;
    client_max_body_size 100M;
}

location /rest/ {
  proxy_pass http://kong:8000;
}

location /storage {
  auth_basic "Restricted";
  auth_basic_user_file /data/access/1;
  proxy_set_header  Authorization $http_authorization;
  proxy_pass_header Authorization;
  proxy_pass $forward_scheme://kong:8000;
}

location /auth {
  auth_basic "Restricted";
  auth_basic_user_file /data/access/1;
  proxy_set_header  Authorization $http_authorization;
  proxy_pass_header Authorization;
  proxy_pass $forward_scheme://kong:8000;
}`
