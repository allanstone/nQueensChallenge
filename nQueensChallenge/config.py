# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

#DATABASE_URI = 'postgres+psycopg2://postgres:post123@localhost:5432/testdb'
# if running in a container this should be the url
DATABASE_URI = 'postgres+psycopg2://postgres:post123@db:5432/testdb'

