#!/bin/bash

# Based on https://github.com/debezium/debezium-examples/tree/master/tutorial
source ../services/.env

# envsubst < connect/debezium-postgres-inventory-connector-template.json > connect/debezium-postgres-inventory-connector.json
CONNECT_URL=$DEBEZIUM_HOST
POSTGRES_CONNECT_CONFIG=connect/debezium-postgres-inventory-connector.json

echo "### Creating Postgres CDC connect ###"
curl -i -X POST $CONNECT_URL/connectors \
    -H "Accept:application/json" \
    -H "Content-Type:application/json" \
    -d @$POSTGRES_CONNECT_CONFIG
echo .


