# Development Plan - Sip Spot

## Project Title
Sip Spot

## Purpose of This Document
This document defines the development plan for Sip Spot. Its purpose is to organise the implementation process in a clear, realistic, and manageable order.

The main goal is to build the project step by step, starting with functionality and structure, and only then moving into styling, refinement, and final polish. This approach helps keep the project focused and reduces unnecessary confusion during development.

---

## General Development Strategy
Sip Spot should be developed in stages.

The recommended order is:

1. Create the real project structure
2. Set up the Flask application
3. Create the SQLite database
4. Insert real or sample coffee shop data
5. Build the main pages
6. Connect the database to the interface
7. Implement the filter system
8. Build the coffee shop details page
9. Improve design and branding
10. Review, test, and refine
11. Prepare the project for final submission

This order makes sure the core logic works before too much time is spent on visual details.

---

## Stage 1: Create Project Structure
The first step is to create the actual folders and files needed for the project.

### Tasks
- create the main project folder
- create `app.py`
- create `sipspot.db`
- create `README.md`
- create `requirements.txt`
- create the `templates/` folder
- create the `static/` folder
- create the `docs/` folder
- create the `images/` folder inside `static/`
- move all planning documents into `docs/`

### Goal
To prepare a clean and organised development environment from the beginning.

---

## Stage 2: Set Up the Flask Application
Once the structure is ready, the next step is to set up a basic Flask app.

### Tasks
- import Flask
- create the Flask application
- create the first route (`/`)
- render `index.html`
- run the application in the browser
- confirm that the app works correctly

### Goal
To make sure the project opens successfully as a web application.

---

## Stage 3: Create the Database
After Flask is working, the next step is to create the database structure in SQLite.

### Tasks
- create the `coffee_shops` table
- create the `coffee_prices` table
- define primary keys
- define foreign key relationships
- save the structure in `sipspot.db`

### Goal
To prepare the project for storing structured coffee shop data.

---

## Stage 4: Insert Initial Data
Before filters and details pages can work properly, the database needs meaningful data.

### Tasks
- insert real or sample coffee shops from Temple Bar
- insert addresses
- insert rating values
- insert work-friendly categories
- insert sit-in / takeaway information
- insert Irish coffee availability
- insert opening and closing times
- insert notes
- insert coffee types and prices in `coffee_prices`

### Goal
To create a realistic dataset for development, testing, and interface building.

---

## Stage 5: Build the Main Pages
After the app and database are ready, the main pages should be created.

### Tasks
- create `layout.html`
- create `index.html`
- create `details.html`
- create `about.html` if included in Version 1

### Goal
To establish the main user flow and the overall structure of the application.

---

## Stage 6: Display Database Data
Once the pages exist, the next step is to display real database content in the interface.

### Tasks
- query coffee shop data from the database
- show coffee shop information on the page
- show coffee prices
- display coffee shop cards
- confirm that the backend and frontend are connected properly

### Goal
To make the application show real useful data instead of static placeholders.

---

## Stage 7: Build the Filter System
This is one of the most important development stages.

### Tasks
- create the filter form on the home page
- filter by coffee type
- filter by maximum price
- filter by work-friendly category
- filter by sit-in / takeaway
- filter by Irish coffee availability
- filter by opening time
- filter by closing time
- show only the matching coffee shops in the results section on the home page

### Goal
To implement the main practical feature of Sip Spot.

---

## Stage 8: Build the Coffee Shop Details Page
After the filters are working, users should be able to open one coffee shop and view full details.

### Tasks
- create a route for each selected coffee shop
- query one coffee shop by `id`
- retrieve all coffee types and prices for that shop
- display full information on `details.html`
- add a link or button from the results section to the details page

### Goal
To allow users to make a more informed decision before visiting a coffee shop.

---

## Stage 9: Improve Design and Branding
Once the main logic is working, the visual identity becomes a priority.

### Tasks
- style the layout with CSS
- improve spacing and typography
- style the header and navigation
- design the hero section
- style the filter box
- improve the coffee shop result cards
- design the details page
- design the About page
- add and position the logo
- add coffee shop images
- make the layout more responsive

### Goal
To make the application visually strong, consistent, and easier to use.

---

## Stage 10: Review and Test
After the design and functionality are in place, the project should be reviewed carefully.

### Tasks
- test all routes
- test all filters
- test the details page
- test navigation links
- check for missing data
- check for database inconsistencies
- correct wording if necessary
- review design consistency
- make sure the application matches the official scope

### Goal
To make the project stable, clear, and ready for final presentation.

---

## Stage 11: Prepare for Final Submission
The final stage focuses on turning the project into a complete CS50 final submission.

### Tasks
- finalise `README.md`
- explain the purpose and structure of the project clearly
- describe the main files and design choices
- prepare the video demo
- review the project structure one last time
- make sure the project is ready to present

### Goal
To prepare Sip Spot for a strong and complete final submission.

---

## Priority Rule
During development, the main priority should always be:

1. Functionality
2. Correct data handling
3. Clear structure
4. Visual design
5. Final polish

This means the application should work correctly before too much time is spent on optional visual adjustments.

---

## What Should Be Avoided Too Early
At the beginning of development, it is better to avoid:

- spending too much time on visual perfection
- adding optional features before the core logic is finished
- changing the scope too often
- building pages or systems that are outside Version 1
- adding features such as accounts, favourites, or maps before the main experience is complete

---

## Version 1 Development Focus
For Version 1, the most important development targets are:

- coffee shop listings
- coffee shop filtering
- coffee shop details
- clear and practical design
- a strong Temple Bar focus

These are the elements that define the core experience of Sip Spot.

---

## Final Development Summary
Sip Spot should be developed in a structured order, beginning with project setup, then Flask, then the database, then data insertion, then page creation, then filtering, then the details page, followed by branding improvements, review, and final submission preparation.

This development method keeps the project realistic, manageable, and focused on the most important goal: building a useful and well-presented coffee finder for Temple Bar.
