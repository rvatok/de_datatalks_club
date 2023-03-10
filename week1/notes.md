DataTalksClub Course 


main playlist on Youtube
https://www.youtube.com/watch?v=T0KR4zcNXIY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=2

dphi tech same Course 
https://dphi.tech/learn/data-engineering/week-1/1113/docker-postgres


docker run -it \
	-e POSTGRES_USER=“root” \
	-e POSTGRES_PASSWORD=“root” \
	-e POSTGRES_DB=“ny_taxi” \
	-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
	-p 5440:5432 \
	--network pg-network \
	--name database \
	postgres:13  

With PGUSER 
docker run -it \
	-e PGUSER=“root”\
	-e POSTGRES_USER=“root” \
	-e POSTGRES_PASSWORD=“root” \
	-e POSTGRES_DB=ny_taxi \
	-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
	-p 5433:5432 \
	--network pg-network \
   	--name pg-database \
	postgres:13  

We will now run the pgAdmin container on another terminal:
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \
    dpage/pgadmin4

Docker build -t taxi_ingest:v001 .

URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"
docker run -it \
--network=de_datatalks_club_default \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips \
    --url=${URL}

URL="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
docker run -it \
--network=de_datatalks_club_default \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=zones \
    --url=${URL}

