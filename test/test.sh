docker compose up -d || { docker compose down; exit 1; }

docker container exec test-spark-env sh -c "spark-submit  --packages org.postgresql:postgresql:42.7.9 /tmp/spark-env/spark-etl.py" || { docker compose down; exit 1; }

docker container exec -u postgres test-db-dest bash -c "psql -v ON_ERROR_STOP=on -f /tmp/test-db-dest-env/test.sql" || { docker compose down; exit 1; }

docker compose down
