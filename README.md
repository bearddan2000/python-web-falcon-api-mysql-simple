# python-web-falcon-api-mysql-simple

## Description
Simple web app that serves api
for a falcon project.

Uses sqlalchemy query a table `dog`.

## Tech stack
- python
  - falcon
  - uvicorn
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- mariadb

## Docker stack
- python:latest
- mariadb:latest

## To run
`sudo ./install.sh -u`
- [Availble at](http://localhost/dogs)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Falcon session setup](https://eshlox.net/2019/05/28/integrate-sqlalchemy-with-falcon-framework-second-version)
