# ☕ Sip Spot

<p align="center">
  <strong>CS50 Final Project</strong><br>
  A practical coffee finder for Temple Bar, Dublin
</p>

<p align="center">
  <a href="https://youtu.be/7rjtKGH6a_I">🎥 Watch Video Demo</a>
</p>

---

## 📌 Overview

**Sip Spot** is a web application designed to help users find coffee shops in the Temple Bar area of Dublin based on practical and useful information.

The project was created to solve a real everyday problem: people often want to stop for a coffee in Temple Bar, but they do not always know which place best matches what they need at that moment.

Temple Bar is one of the busiest and most famous areas in Dublin. It attracts tourists, visitors, workers, students, and local customers. Because of that, choosing the right coffee shop is not always simple. Some places are better for takeaway, some are better for sitting down, some are more suitable for working, some serve Irish coffee, and some close much earlier than people might expect.

Sip Spot was built to make that decision easier by bringing useful café information together in one place.

---

## 🎯 Problem It Solves

Instead of showing only a basic list of cafés, Sip Spot helps users compare coffee shops using categories that actually influence real decisions.

For example, a user may want:

- an Americano under a certain price
- a place that is good for working
- a café with sit-in availability
- a place that serves Irish coffee
- a coffee shop that opens earlier
- a place that closes later

These details may seem small, but together they can strongly influence where someone chooses to go.

---

## 🧭 Why Temple Bar

One of the main design choices of the project was to keep the scope intentionally narrow.

Version 1 focuses only on coffee shops located in **Temple Bar, Dublin**. This was done for two reasons:

1. It keeps the project realistic and manageable for the CS50 final project.  
2. It gives the application a clearer local identity.

Rather than trying to build a platform for every café in Dublin, Sip Spot begins with one specific area and solves one specific local problem well.

This project is also personally meaningful because it is informed by direct experience with the coffee shop environment in central Dublin, making the concept more real and less generic.

---

## ✨ Main Features

### Practical filtering
Users can search coffee shops by:

- coffee type
- maximum price
- work-friendly suitability
- sit-in or takeaway availability
- Irish coffee availability
- opening time
- closing time

### Integrated results section
The matching results appear directly on the **Home Page**, creating a smoother and more direct user experience.

Each result card includes:

- coffee shop image
- coffee shop name
- address
- selected coffee type and price
- rating
- practical badges
- notes
- link to the details page

### Coffee shop details page
Each coffee shop has a dedicated page showing:

- full image
- address
- rating
- practical categories
- opening and closing times
- notes
- full list of coffee types and prices

### About page
The project also includes an About page explaining:

- the purpose of Sip Spot
- the decision to focus on Temple Bar
- the practical categories used in the app

---

## 🖥️ How the Application Works

The user begins on the **Home Page**, where the branding, hero section, and filter form are displayed.

From there, the user can select practical filters such as coffee type, price, work-friendly atmosphere, sit-in or takeaway availability, Irish coffee availability, and opening or closing time.

Once the form is submitted, **Flask** receives the selected values and builds a query against the **SQLite** database.

The database stores:

- coffee shop information in one table
- coffee prices in a second related table

This allows the application to filter a coffee shop by a specific drink and compare prices in a structured way.

After the query is processed, the application displays matching coffee shops directly on the Home Page.

If the user wants more information, they can open a **details page** for a selected coffee shop. The application also includes an **About page** that explains the project’s purpose and design choices.

---

## 🎨 Design and User Experience

A major part of the development process involved not only functionality but also presentation.

The interface was designed to feel:

- modern
- warm
- coffee-inspired
- practical
- easy to scan

The visual identity includes:

- a custom Sip Spot logo
- a large hero section
- branded colours
- coffee shop photography
- styled result cards
- a more editorial About page

The Home Page was built as both the introduction and the main search experience. Rather than forcing the user through too many separate steps, the filtering process happens directly on the home screen, and the results appear in the same overall flow.

This design decision made the application more intuitive and more suitable for quick real-world use.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Routing, backend logic, template rendering |
| **SQLite** | Local database storage |
| **HTML** | Page structure |
| **CSS** | Styling, layout, visual identity |

---

## 🗂️ Project Structure

### `app.py`
The main application file.  
It handles Flask setup, routes, filter logic, database queries, and page rendering.

### `init_db.py`
Creates the SQLite database structure and defines the project tables.

### `seed_data.py`
Inserts the coffee shop data and coffee prices into the database.

### `sipspot.db`
The SQLite database used by the project.

### `templates/`
Stores the HTML templates used by Flask.

- `layout.html` → shared base layout  
- `index.html` → Home Page with filters and integrated results  
- `details.html` → coffee shop details page  
- `about.html` → About page  

### `static/`
Stores all styling and visual assets.

- `styles.css` → full project styling  
- `images/` → logo files, hero image, and coffee shop images  

### `docs/`
Stores the project planning documents:

- official scope
- official features
- pages structure
- database plan
- project structure
- development plan

---

## 🗄️ Database Design

The application uses a simple SQLite database with **two main tables**.

### `coffee_shops`
Stores the main coffee shop information, including:

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
Stores coffee types and prices for each coffee shop.

This structure was chosen because one coffee shop can have multiple coffee types with different prices. Keeping prices in a separate table makes the data more organised and makes filtering by coffee type and price easier.

---

## 🧠 Key Design Decisions

### 1. Narrow and realistic scope
One of the most important design decisions was to keep the project focused on practical use rather than unnecessary complexity.

Instead of trying to include maps, accounts, reviews, and all cafés in Dublin, Sip Spot focuses on one area, one clear user problem, and one manageable Version 1.

### 2. Integrated results on the Home Page
Rather than building a separate results page, the results appear directly on the Home Page. This keeps the experience more direct and easier to follow.

### 3. Web application instead of mobile app
A mobile app might seem like the more obvious format for a coffee finder, but a web application was the best match for the tools used in CS50 and for the realistic scope of the project.

### 4. Separate price table
The use of a separate `coffee_prices` table was important because each coffee shop can have several drinks with different prices. This made the database more flexible and more suitable for filtering.

### 5. Stronger visual identity
The project evolved from a simple Flask structure into a more polished branded website, with careful attention to layout, typography, images, branding, and overall presentation.

---

## 📍 Scope of Version 1

### Included
- Temple Bar coffee shop listings
- integrated results section on the Home Page
- coffee shop details pages
- practical filtering
- styled result cards
- About page
- branding and custom logo
- image-based presentation

### Not Included
- user accounts
- favourites
- map integration
- live business data
- user-submitted reviews
- recommendation algorithms
- automatic routing
- mobile app development

These ideas may be part of future versions, but they are outside the scope of the first release.

---

## 🚀 Why This Project Stands Out

Sip Spot is not just a general café list.

It focuses on practical questions that users genuinely ask in real life, for example:

- Where can I get an Americano under a certain price?
- Which place is good for working?
- Which café has sit-in availability?
- Which places serve Irish coffee?
- Which coffee shops are already open?
- Which coffee shops close later?

This practical focus makes the project more useful than a simple directory and gives it a stronger local identity.

---

## 🔍 Final Reflection

Sip Spot is a practical coffee finder built around a real local problem in Temple Bar.

It combines:

- structured coffee shop data
- practical filters
- styled result cards
- detailed information pages
- a strong visual identity

The project is intentionally small in scope, but strong in focus. It demonstrates the use of Flask, SQLite, HTML, CSS, templating, filtering logic, and relational data while also showing attention to user experience, organisation, and presentation.

Sip Spot is not meant to be a complete city-wide coffee platform yet. Instead, it is a clear, realistic, and well-scoped Version 1 that solves a real everyday problem and leaves room for future growth.
