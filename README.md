Project Overview: 
Squirrel tracker is a web application developed with Django Framework with which people can keep track of all the spotted squirrels in Central Park, NYC. With this app, people are allowed to add, update, and view squirrel sightings. 
The squirrel data used in this project: https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv


Install/Running:
-Click the link below to run the web application:
https://solid-arcadia-302914.df.r.appspot.com/

OR 
-use command line by clone 

Management Commands:

Import: A command that can be used to import the data from the 2018 census file (in CSV format). 
The file path should be specified at the command line after the name of the management command.
python manage.py import_squirrel_data /path/to/file.csv

Export: A command that can be used to export the data in CSV format. 
The file path should be specified at the command line after the name of the management command.
python manage.py export_squirrel_data /path/to/file.csv

Main Features:

1. Import and Export data using csv format.
2. View squirrel sites in Central Park.
3. Add/Edit squirrel sites.



Group Name & Section: Group 17, Section 1

Group Members: UNIs: [hz2706,zl2979]
