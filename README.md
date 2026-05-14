# ☕ Sip Spot

### CS50 Final Project  
**Video Demo:** https://youtu.be/7rjtKGH6a_I

---

## Overview

Sip Spot is a web application designed to help users find coffee shops in the Temple Bar area of Dublin based on practical and useful information.

The project was created to solve a real everyday problem: people often want to stop for a coffee in Temple Bar, but they do not always know which place best matches what they need at that moment.

Temple Bar is one of the busiest and most famous areas in Dublin. It attracts tourists, visitors, workers, students, and local customers. Because of that, choosing the right coffee shop is not always as simple as it seems. Some places are better for takeaway, some are better for sitting down, some are more suitable for working, some serve Irish coffee, and some close much earlier than people might expect.

Sip Spot was built to make that decision easier by bringing useful café information together in one place.

---

## Problem It Solves

Sip Spot focuses on practical decision-making.

Instead of showing only a basic list of coffee shops, the application helps users compare cafés based on real categories that affect the experience. A user may want:

- an Americano under a certain price
- a place that is good for working
- a café with seating
- somewhere that is still open later in the day

These details may seem small, but together they can strongly influence where someone chooses to go.

---

## Why Temple Bar

One of the main design choices of the project was to keep the scope intentionally narrow.

Version 1 focuses only on coffee shops located in Temple Bar. This was done for two reasons:

1. It keeps the project realistic and manageable for the CS50 final project.  
2. It gives the application a clearer identity.

Rather than trying to build a platform for every café in Dublin, Sip Spot begins with one specific area and solves one specific local problem well.

This project is also personally meaningful because it is informed by direct experience with the coffee shop environment in central Dublin. That makes the idea less generic and more connected to real day-to-day use.

---

## How the Application Works

The user begins on the **Home Page**, where the branding, hero section, and filter form are displayed.

From there, the user can choose practical filters such as:

- coffee type
- maximum price
- work-friendly suitability
- sit-in or takeaway availability
- Irish coffee availability
- opening time
- closing time

Once the form is submitted, Flask receives the selected filter values and uses them to build a query against the SQLite database.

The database stores coffee shop information in one table and coffee prices in another related table. This makes it possible to filter a coffee shop by a specific drink and compare prices in a structured way.

After the query is processed, the application displays matching coffee shops in a styled results section on the Home Page.

Each result card includes:

- photo
- shop name
- address
- selected coffee price information
- rating
- practical badges
- notes
- link to a dedicated details page

If the user wants more information, they can open a dedicated **details page** for that coffee shop. On this page, the application shows a larger image, address, practical information, notes, rating, and the complete list of coffee types and prices stored for that shop.

The user can also visit the **About page** from the top navigation. This page explains the purpose of the project, the reason for focusing on Temple Bar, and the thinking behind the practical filter categories.

---

## Main Features

### Coffee shop filtering
Users can filter coffee shops by:

- coffee type
- maximum price
- whether the place is good for working
- sit-in or takeaway availability
- Irish coffee availability
- opening time
- closing time

### Results section on the Home Page
The application displays matching coffee shops directly on the Home Page.

Each card includes:

- coffee shop image
- coffee shop name
- address
- selected coffee type and price
- rating
- practical badges
- notes
- link to the details page

### Coffee shop details page
The details page shows:

- full image
- address
- rating
- practical categories
- opening and closing times
- notes
- a complete list of coffee types and prices stored for that shop

### About page
The application also includes an About page that explains:

- the purpose of the project
- the reason for focusing on Temple Bar
- the practical idea behind the filter categories

---

## Design and User Experience

A major part of the development process involved not only functionality but also presentation.

The interface was designed to feel modern, warm, and coffee-inspired. The visual identity includes:

- a custom Sip Spot logo
- a large hero section
- branded colours
- coffee shop photography
- styled result cards

The Home Page was built as both the introduction and the main search experience. Rather than forcing the user through too many separate steps, the filtering process happens directly on the home screen, and the results appear in the same overall flow.

This makes the application easier to use and keeps the user experience simple.

The details page supports the final decision-making stage, while the About page adds context and makes the website feel more complete.

---

## Tech Stack

Sip Spot was built with:

- **Python**
- **Flask**
- **SQLite**
- **HTML**
- **CSS**

---

## Project Structure

### `app.py`
The main Python file of the application.  
It handles Flask setup, routes, database queries, filter logic, and page rendering.

### `init_db.py`
Creates the SQLite database structure and defines the tables used in Version 1.

### `seed_data.py`
Inserts the coffee shop data and coffee prices into the database. It is used during development and testing.

### `sipspot.db`
The SQLite database file used by the project. It stores coffee shop information and coffee prices.

### `templates/layout.html`
The base HTML layout shared across the application. It contains the site header, navigation, and shared page structure.

### `templates/index.html`
The Home Page. It includes the hero section, filter form, and the integrated results section.

### `templates/details.html`
Shows the complete details for one selected coffee shop, including full pricing information.

### `templates/about.html`
Explains the purpose of Sip Spot and the main design ideas behind the project.

### `static/styles.css`
Contains the full CSS styling of the project, including layout, typography, cards, buttons, responsive behaviour, and branding.

### `static/images/`
Stores the hero image, coffee shop images, and logo files used throughout the application.

### `docs/`
Stores the planning documents created during development, including:

- project scope
- official features
- page structure
- database plan
- project structure
- development plan

---

## Database Design

The application uses a simple SQLite database with two main tables.

### `coffee_shops`
This table stores the main coffee shop information, including:

- name
- address
- rating
- work-friendly suitability
- service type
- Irish coffee availability
- opening time
- closing time
- notes
- image filename

### `coffee_prices`
This table stores coffee types and prices for each coffee shop.

This two-table structure was chosen because one coffee shop can have multiple coffee types with different prices. Keeping prices in a separate table makes the data more organised and makes filtering by coffee type and price easier.

---

## Key Design Decisions

### 1. Narrow and realistic scope
One of the most important design decisions was to keep the project focused on practical use rather than unnecessary complexity.

It would have been possible to imagine a larger app with maps, accounts, reviews, and many more locations, but that would have weakened the project by making it too broad for Version 1.

Instead, the final design focuses on:

- one area
- one core user problem
- one clear user experience

### 2. Web application instead of mobile app
A mobile app might seem like the more obvious format for a coffee finder, but the web application was the best match for the tools and skills used in CS50.

It also remains accessible and responsive while being more realistic for the final project.

### 3. Visual refinement
The project evolved from a very basic Flask structure into a more polished branded website, including:

- logo design
- stronger cards
- a styled hero section
- a consistent visual language

This made the project feel more like a real product rather than only a technical exercise.

### 4. Separate price table
The use of a separate `coffee_prices` table was important because each coffee shop can have several drinks with different prices.

This made the database more flexible and made filtering by coffee type and price much easier than a single-table structure would have allowed.

---

## Scope of Version 1

### Included
- Temple Bar coffee shop listings
- integrated results section on the Home Page
- coffee shop details pages
- practical filtering
- styled result cards
- About page
- branding and custom logo
- local image-based presentation

### Not included
- user accounts
- favourites
- map integration
- live business data
- user-submitted reviews
- recommendation algorithms
- automatic routing
- mobile app development

These ideas may be part of a future version, but they are outside the scope of the first release.

---

## Why This Project Is Different

One of the most important parts of this project is that it is not just a general café list.

It focuses on practical questions that users genuinely ask in real life, for example:

- Where can I get an Americano under a certain price?
- Which place is good for working?
- Which café has sit-in availability?
- Which places serve Irish coffee?
- Which coffee shops are already open?
- Which coffee shops close later?

This practical focus makes the project more useful than a simple directory. It also gives the application a clear purpose and a stronger local identity.

---

## Final Reflection

Sip Spot is a practical coffee finder built around a real local problem in Temple Bar.

It combines structured coffee shop data, practical filters, styled result cards, and detailed information pages in order to help users choose the right coffee shop for their needs.

The project is intentionally small in scope, but strong in focus. It demonstrates the use of Flask, SQLite, HTML, CSS, templating, filtering logic, and relational data while also showing attention to user experience, project structure, and visual identity.

Sip Spot is not meant to be a complete city-wide coffee platform yet. Instead, it is a clear, realistic, and well-scoped Version 1 that solves a real everyday problem and leaves room for future growth.
