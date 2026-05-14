# Sip Spot

#### Video Demo: https://youtu.be/7rjtKGH6a_I

## Description
Sip Spot is a web application designed to help users find coffee shops in the Temple Bar area of Dublin based on practical and useful information. The project was created to solve a real and practical problem: people often want to stop for a coffee in Temple Bar, but they do not always know which place best matches what they need at that moment.

Temple Bar is one of the busiest and most famous areas in Dublin. It attracts tourists, visitors, workers, students, and local customers. Because of that, choosing the right coffee shop is not always as simple as it seems. Some places are better for takeaway, some are better for sitting down, some are more suitable for working, some serve Irish coffee, and some close much earlier than people might expect. Sip Spot was built to make this decision easier by bringing useful café information together in one place.

The project is focused on practical decision-making. Instead of showing only a basic list of coffee shops, Sip Spot helps users compare cafés based on real categories that affect the experience. A user may want an Americano under a certain price, a place that is good for working, a café with seating, or somewhere that is still open later in the day. These details may seem small, but together they can strongly influence where someone chooses to go.

One of the main design choices of the project was to keep the scope intentionally narrow. Version 1 focuses only on coffee shops located in Temple Bar. This was done for two reasons. First, it keeps the project realistic and manageable for the CS50 final project. Second, it gives the application a clearer identity. Rather than trying to build a platform for every café in Dublin, Sip Spot begins with one specific area and solves one specific local problem well.

This project is also personally meaningful because it is informed by direct experience with the coffee shop environment in central Dublin. That makes the idea less generic and more connected to real day-to-day use. Instead of inventing a random app concept, Sip Spot was designed around a situation that people genuinely face when they want a coffee break in a crowded part of the city.

## How the Application Works
The user begins on the Home Page, where the project branding, hero section, and filter form are displayed. From there, the user can choose practical filters such as coffee type, maximum price, work-friendly suitability, sit-in or takeaway availability, Irish coffee availability, and opening or closing time.

Once the form is submitted, Flask receives the selected filter values and uses them to build a query against the SQLite database. The database stores coffee shop information in one table and coffee prices in another related table. This makes it possible to filter a coffee shop by a specific drink and compare prices in a structured way.

After the query is processed, the application displays matching coffee shops in a styled results section on the Home Page. Each result card includes a photo, the shop name, address, selected coffee price information, rating, practical badges, notes, and a link to a dedicated details page. This allows users to compare options quickly without leaving the main flow of the site.

If the user wants more information, they can open a dedicated details page for that coffee shop. On this page, the application shows a larger image, address, practical information, notes, rating, and the complete list of coffee types and prices stored for that shop. This gives the user a clearer view before choosing where to go.

The user can also visit the About page from the top navigation. This page explains the purpose of the project, the reason for focusing on Temple Bar, and the thinking behind the practical filter categories.

## Main Features
Sip Spot includes a set of practical features designed to support this goal.

Users can filter coffee shops by:
- coffee type
- maximum price
- whether the place is good for working
- sit-in or takeaway availability
- Irish coffee availability
- opening time
- closing time

The application then displays matching coffee shops in a styled results section on the Home Page. Each result card includes:
- coffee shop image
- coffee shop name
- address
- selected coffee type and price
- rating
- practical badges
- notes
- link to the details page

If the user wants more information, they can open a full details page for a selected coffee shop. The details page shows:
- full image
- address
- rating
- practical categories
- opening and closing times
- notes
- a complete list of coffee types and prices stored for that shop

The application also includes an About page that explains the purpose of the project, the reason for focusing on Temple Bar, and the practical idea behind the filter categories.

## Design and User Experience
A major part of the development process involved not only functionality but also presentation. The interface was designed to feel modern, warm, and coffee-inspired. The visual identity includes a custom Sip Spot logo, a large hero section, branded colours, coffee shop photography, and styled result cards.

The Home Page was built as both the introduction and the main search experience. Rather than forcing the user through too many separate steps, the filtering process happens directly on the home screen, and the results appear in the same overall flow. This makes the application easier to use and keeps the user experience simple.

The details page was designed to support the final decision-making stage, while the About page adds context and makes the website feel more complete. Together, these pages create a small but coherent Version 1 experience.

## Project Structure
The project is built with Flask, SQLite, HTML, and CSS.

### `app.py`
This is the main Python file of the application. It handles Flask setup, routes, database queries, filter logic, and page rendering.

### `init_db.py`
This file creates the SQLite database structure and defines the tables used in Version 1.

### `seed_data.py`
This file inserts the coffee shop data and coffee prices into the database. It is used during development and testing.

### `sipspot.db`
This is the SQLite database file used by the project. It stores coffee shop information and coffee prices.

### `templates/layout.html`
This is the base HTML layout shared across the application. It contains the site header, navigation, and shared page structure.

### `templates/index.html`
This is the Home Page. It includes the hero section, filter form, and the integrated results section.

### `templates/details.html`
This page shows the complete details for one selected coffee shop, including full pricing information.

### `templates/about.html`
This page explains the purpose of Sip Spot and the design ideas behind the project.

### `static/styles.css`
This file contains the full CSS styling of the project, including layout, typography, cards, buttons, responsive behaviour, and branding.

### `static/images/`
This folder stores the hero image, coffee shop images, and logo files used throughout the application.

### `docs/`
This folder stores the planning documents created during development, including the project scope, features, page structure, database plan, project structure, and development plan.

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

## Key Design Decisions
One of the most important design decisions was to keep the project focused on practical use rather than unnecessary complexity. It would have been possible to imagine a larger app with maps, accounts, reviews, and many more locations, but that would have weakened the project by making it too broad for Version 1. Instead, the final design focuses on one area, one core user problem, and one clear user experience.

Another important decision was to build the project as a web application rather than a mobile application. A mobile app might seem like the more obvious format for a coffee finder, but the web application was the best match for the tools and skills used in CS50. It also remains accessible and responsive while being more realistic for the final project.

There was also a strong focus on visual refinement. The project evolved from a very basic Flask structure into a more polished branded website, including logo design, stronger cards, a styled hero section, and a consistent visual language. This made the project feel more like a real product rather than only a technical exercise.

A final key design decision involved the data model. The use of a separate `coffee_prices` table was important because each coffee shop can have several drinks with different prices. This made the database more flexible and made filtering by coffee type and price much easier than a single-table structure would have allowed.

## Scope of Version 1
Version 1 is intentionally focused and does not try to include every possible feature.

It includes:
- Temple Bar coffee shop listings
- integrated results section on the Home Page
- coffee shop details pages
- practical filtering
- styled result cards
- About page
- branding and custom logo
- local image-based presentation

It does not include:
- user accounts
- favourites
- map integration
- live business data
- user-submitted reviews
- recommendation algorithms
- automatic routing
- mobile app development

These ideas may be part of a future version, but they are outside the scope of the first release.

## Why This Project Is Different
One of the most important parts of this project is that it is not just a general café list. It focuses on practical questions that users genuinely ask in real life, for example:

- Where can I get an Americano under a certain price?
- Which place is good for working?
- Which café has sit-in availability?
- Which places serve Irish coffee?
- Which coffee shops are already open?
- Which coffee shops close later?

This practical focus makes the project more useful than a simple directory. It also gives the application a clear purpose and a stronger local identity.

## Final Reflection
Overall, Sip Spot is a practical coffee finder built around a real local problem in Temple Bar. It combines structured coffee shop data, practical filters, styled result cards, and detailed information pages in order to help users choose the right coffee shop for their needs.

The project is intentionally small in scope, but strong in focus. It demonstrates the use of Flask, SQLite, HTML, CSS, templating, filtering logic, and relational data while also showing attention to user experience, project structure, and visual identity.

Sip Spot is not meant to be a complete city-wide coffee platform yet. Instead, it is a clear, realistic, and well-scoped Version 1 that solves a real everyday problem and leaves room for future growth.
