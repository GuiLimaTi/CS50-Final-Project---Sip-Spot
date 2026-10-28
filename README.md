# Sip Spot – Coffee Finder for Temple Bar, Dublin

A Flask web app that helps people choose a coffee shop in Temple Bar by the things that actually matter in the moment: drink and price, work-friendliness, sit-in or takeaway, Irish coffee and opening hours. My final project for Harvard's CS50x.

**Languages:** Python, SQL, HTML, CSS · **Framework:** Flask · **Database:** SQLite · **Status:** Completed (Version 1, 2026)

**Video demo:** https://youtu.be/7rjtKGH6a_I

## Overview

Temple Bar is one of Dublin's busiest areas, and choosing a café there isn't always simple: some are better for takeaway, some for sitting down to work, some serve Irish coffee, and some close earlier than people expect. Sip Spot brings that practical information together in one place.

The first version deliberately covers a small, well-defined area (six Temple Bar coffee shops and 33 drink prices) so the problem could be solved properly instead of partially for the whole city. The idea comes from my own experience working in Dublin's coffee scene.

## Features

- **Practical filters:** coffee type, maximum price, work-friendly, sit-in or takeaway, Irish coffee, opening time and closing time
- **Results on the home page:** each card shows the photo, address, selected drink and price, rating, badges and notes
- **Details page** for every coffee shop, with opening hours and the full price list
- **About page** explaining the purpose of the project and the filters
- Custom branding: logo, hero image, colour palette and café photography

## Tech stack

| Technology | Purpose |
|---|---|
| Python + Flask | Routing, filter logic and template rendering |
| SQLite | Coffee shop and price data |
| Jinja | Dynamic HTML templates |
| HTML + CSS | Layout, styling and visual identity |

## How it works

1. The user picks filters on the home page.
2. Flask reads the selected values and builds a SQL query.
3. The query joins `coffee_shops` with `coffee_prices` to filter by drink and price.
4. Matching cafés appear as result cards on the same page, each linking to a details page.

### Database design

| Table | Contents |
|---|---|
| `coffee_shops` | Name, address, rating, work-friendly, service type, Irish coffee, opening and closing times, notes, image |
| `coffee_prices` | Coffee type and price for each shop (one shop has many prices) |

Keeping prices in a separate table makes it easy to filter by a specific drink and compare prices across cafés.

## How to run

```bash
pip install -r requirements.txt
python init_db.py      # create the tables
python seed_data.py    # load the coffee shops and prices
flask run
```

## Project structure

```
app.py            Flask app: routes, filters and queries
init_db.py        Creates the database tables
seed_data.py      Inserts coffee shops and prices
sipspot.db        SQLite database
templates/        layout, index (home + results), details, about
static/           styles.css and images
docs/             Planning documents: scope, features, pages, database and development plan
```

## Design decisions

- **Narrow scope:** one area and one clear problem, rather than maps, accounts and every café in Dublin
- **Results on the home page:** fewer clicks and a faster experience for someone deciding on the spot
- **Web app instead of a mobile app:** the best fit for the tools covered in CS50 and a realistic Version 1
- **Separate price table:** flexible filtering by drink and price

## Future improvements

- Map view and walking distance
- More areas of Dublin
- User favourites and reviews
- Live opening hours from an external data source

## What I learned

- Planning a project before coding: scope, features, pages and database
- Designing a small relational database and querying it from Flask
- Building filters that translate user choices into SQL safely
- Paying attention to user experience, not just functionality

---

**Guilherme Lima** · Aspiring IT Support Technician · [LinkedIn](https://www.linkedin.com/in/glimaalmeida) · [GitHub](https://github.com/GuiLimaTi)
