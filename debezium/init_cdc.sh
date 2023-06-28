#!/bin/bash

# Based on https://github.com/debezium/debezium-examples/tree/master/tutorial
source ../.env
template=$(cat connect/debezium-postgres-inventory-connector-template.json) 
# Load the ENV Vars in the Template:
template=${template//SOURCE_HOST/$SOURCE_HOST}
template=${template//SOURCE_PORT/$SOURCE_PORT}
template=${template//SOURCE_USER/$SOURCE_USER}
template=${template//SOURCE_PASS/$SOURCE_PASS}
template=${template//SOURCE_DB/$SOURCE_DB}
template=${template//DEBEZIUM_SERVER_NAME/$DEBEZIUM_SERVER_NAME}
template=${template//SOURCE_SCHEMA/$SOURCE_SCHEMA}
template=${template//SOURCE_SCHEMA/$SOURCE_SCHEMA}
CONNECT_URL=$DEBEZIUM_HOST
POSTGRES_CONNECT_CONFIG=$template
echo $POSTGRES_CONNECT_CONFIG
echo "### Creating Postgres CDC connect ###"
curl -i -X POST $CONNECT_URL/connectors \
    -H "Accept:application/json" \
    -H "Content-Type:application/json" \
    -d "$POSTGRES_CONNECT_CONFIG"
echo .


