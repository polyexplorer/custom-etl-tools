#!/bin/bash

CONNECT_URL=http://localhost:8085
SINK_SNOWPIPE_CONNECT_CONFIG=connect/snowflake-sink-connector.json

echo "### Creating Snowpipe sink connector ###"
curl -i -X POST $CONNECT_URL/connectors \
    -H "Accept:application/json" \
    -H "Content-Type:application/json" \
    -d @$SINK_SNOWPIPE_CONNECT_CONFIG
echo .
