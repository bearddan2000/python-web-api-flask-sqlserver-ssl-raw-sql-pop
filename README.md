# python-web-api-flask-sqlserver-ssl-raw-sql-pop

## Description
Creates an api of `pop` by using raw sql for a flask project.
Has the ability to query by parameters.
If path is not found, will default to 404 error.

Remotely tested with *testify*.

Sql server uses self-signed ssl.

## Tech stack
- python
  - flask
  - sqlalchemy
  - testify
  - requests
- mssql

## Docker stack
- alpine:edge
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- Get all pops: http://localhost/pop
  - Schema id, name, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/pop/<id>
  - Read: http://localhost/pop/<id>
  - Update: curl -i -X POST localhost/pop/<id>/<name>/<color>
  - Delete: curl -i -X DELETE localhost/pop/<id>

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
