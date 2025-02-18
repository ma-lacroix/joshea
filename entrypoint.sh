#!/bin/sh
rmdir /joshea/app/db
mkdir -p /joshea/app/db
echo '{"workflows": {}}' > /joshea/app/db/meta_data.json
echo '{}' > /joshea/app/db/runs_data.json
exec flask run