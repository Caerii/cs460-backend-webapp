# cs460-backend-webapp

This application is the backend for a database application.

# Project Specification

Teams will design and implement a web-based university management system. The system will make use of the university database that you have been working on since the beginning of this semester, but with some extension. The system will utilize the Django web framework to connect to MySQL and to hold together all components: loading data from the database, representing the data as Python objects, and dynamically creating a web page for displaying the data. The user interface will be built using Django templates.

Your system will provide functionalities to support three kinds of users: admins, profs, and students, as follows:

Admin can do the following: 
F1. Roster: Create a list of professors sorted by one of the following criteria chosen by the admin: (1) by name (2) by dept, or (3) by salary. 
F2. Salary: Create a table of min/max/average salaries by dept.
F3. Performance: Given a professor's name, an academic year, and a semester, show the following for the professor: the total number of course sections taught during the semester, the total number of students taught, the total dollar amount of funding the professor has secured, and the total number of papers the professor has published.
Professors can do the following:
F4. Create the list of course sections and the number of students enrolled in each section that the professor taught in a given semester
F5. Create the list of students enrolled in a course section taught by the professor in a given semester
Students can do the following:
F6. Query the list of course sections offered by dept in a given year and semester.

# TODO:

- [ ] Interface with the database.
- [x] Create a Django project.
- [x] Create a Django app.
- [x] Create a login system.
- [ ] Create a user interface with clean buttons and CSS styling.
- [ ] Add CRUD functionality to the database tables.
- [ ] Add the ability to search the database.
- [ ] Add the ability to sort the database.
- [ ] Add the ability to filter the database.
- [ ] Add the ability to group the database.
- [ ] Add the ability to aggregate the database.
- [ ] Add customizability to the user interface.
- [x] Have pages for each of the types of users (admins, profs, and students).
- [ ] Add the ability to export the database to a CSV file.

