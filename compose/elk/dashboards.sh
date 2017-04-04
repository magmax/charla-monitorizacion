#!/bin/bash

docker-compose exec metricbeat sh -c './scripts/import_dashboards -es http://elasticsearch:9200 -user elastic -pass changeme'
