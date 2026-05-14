# Project Structure - Sip Spot

## Project Title
Sip Spot

## Purpose of This Document
This document defines the folder and file structure of the Sip Spot web application.

Its purpose is to keep the project organised, clear, and easy to develop. It also helps separate the application files from the planning and support documents.

The structure chosen for Version 1 is intentionally simple, because the project is designed to remain realistic, manageable, and appropriate for the CS50 final project.

---

## Main Files

### `app.py`
This is the main Python file of the application.

It contains:

- Flask app setup
- route definitions
- database connection logic
- filter handling
- database queries
- rendering of templates

This is the core file that controls how the application works.

---

### `init_db.py`
This file is responsible for creating the database tables.

It is used to initialise the SQLite database structure before real data is inserted.

It contains:

- database connection
- table creation logic
- schema definition for Version 1

Its purpose is to prepare the database correctly from the beginning.

---

### `seed_data.py`
This file is responsible for inserting data into the database.

It contains the coffee shop records and their related coffee prices used in Version 1.

It is useful for:

- populating the database
- resetting data during development
- testing the application with realistic entries

---

### `sipspot.db`
This is the SQLite database file.

It stores the structured data used by the application, including:

- coffee shop information
- coffee types
- prices
- opening and closing times
- sit-in / takeaway information
- work-friendly information
- Irish coffee availability
- notes

This is the main data source of Sip Spot.

---

### `README.md`
This is the main documentation file required for the CS50 final project.

It explains:

- the purpose of the project
- the problem it solves
- the main design decisions
- the technologies used
- the structure of the application

It is one of the most important files for final submission.

---

### `requirements.txt`
This file lists the Python packages needed to run the project.

For Version 1, it mainly supports:

- Flask
- any required dependencies for the local environment

Its purpose is to make the project easier to install and run.

---

## Templates Folder

The `templates/` folder stores the HTML templates used by Flask.

### `layout.html`
This is the base template shared across the site.

It contains:

- page header
- navigation
- common layout structure
- shared branding

Other templates extend this file.

---

### `index.html`
This is the Home Page template.

It contains:

- the hero section
- the filter form
- the results section
- coffee shop result cards

It is the main page of the application.

---

### `details.html`
This template displays one selected coffee shop in full detail.

It contains:

- coffee shop image
- name
- address
- rating
- practical information
- price list
- notes
- navigation back to results

It supports the final decision-making stage for the user.

---

### `about.html`
This template explains the purpose of the project.

It contains:

- what Sip Spot is
- the problem it solves
- why Temple Bar was chosen
- the practical categories used
- the technologies behind the application

It helps make the site feel more complete and professional.

---

## Static Folder

The `static/` folder stores styling and visual assets.

### `styles.css`
This file contains the CSS styling for the whole application.

It includes:

- page layout
- typography
- spacing
- button styling
- card styling
- hero section design
- responsive adjustments
- visual branding rules

It controls the visual identity of Sip Spot.

---

### `images/`
This folder stores the visual assets used by the website.

It includes:

- hero image
- coffee shop photos
- horizontal logo
- square icon logo

These files support both branding and page presentation.

---

## Docs Folder

The `docs/` folder stores the planning and support documents created during the project process.

### `OFFICIAL_SCOPE.md`
Defines the scope and limits of Version 1.

### `OFFICIAL_FEATURES.md`
Defines the official features included in the project.

### `PAGES_STRUCTURE.md`
Explains the role and purpose of each page.

### `DATABASE_PLAN.md`
Defines the database structure and tables.

### `PROJECT_STRUCTURE.md`
Defines the project folder and file organisation.

### `DEVELOPMENT_PLAN.md`
Defines the development stages and implementation order.

---

## Why This Structure Was Chosen
This structure was chosen because it is:

- simple
- clear
- realistic
- suitable for a Flask project
- appropriate for a CS50 final project

It separates:

- application logic
- HTML templates
- CSS styling
- image assets
- database files
- planning documents

This makes the project easier to maintain, easier to understand, and easier to present.

---

## Version 1 Structure Summary
Version 1 of Sip Spot uses a simple Flask-based structure with:

- one main Python application file
- two helper database scripts
- one SQLite database
- one templates folder
- one static folder with CSS and images
- one docs folder for planning and support files

This structure is strong enough for the first version of the project while still remaining manageable.

---

## Possible Future Expansion
If Sip Spot expands in the future, the structure could later include:

- JavaScript files
- additional CSS files
- more templates
- user authentication files
- favourites system files
- admin tools
- API integration files
- more database scripts

For Version 1, however, the current structure is the best option because it keeps the project focused and organised.
