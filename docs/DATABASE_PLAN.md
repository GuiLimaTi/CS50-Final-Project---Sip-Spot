# Database Plan - Sip Spot

## Project Title
Sip Spot

## Purpose of This Document
This document explains the database structure planned for Sip Spot. Its purpose is to define what information needs to be stored, how the data is organised, and how the database supports the main features of the application.

The database is designed to be simple, practical, and strong enough for Version 1 of the project. It focuses only on the information needed to support coffee shop listings, filtering, and detailed coffee shop pages.

---

## Database Goal
The goal of the Sip Spot database is to store useful and structured information about coffee shops in the Temple Bar area of Dublin.

The database must support the core user experience of the project, including:

- displaying coffee shop listings
- filtering shops by practical categories
- showing coffee types and prices
- opening a full details page for each coffee shop

Because Sip Spot is a Version 1 project for the CS50 final submission, the database should remain focused and manageable rather than overly complex.

---

## Recommended Database for Version 1
Sip Spot will use **SQLite** for Version 1.

SQLite is the best choice for this project because it is:

- lightweight
- easy to set up
- well suited for Flask projects
- appropriate for a small local dataset
- realistic for a student final project

This makes it a strong and practical option for storing structured coffee shop data without adding unnecessary complexity.

---

## Main Tables for Version 1
Version 1 of Sip Spot will use **two main tables**:

1. `coffee_shops`
2. `coffee_prices`

This structure keeps the database organised while allowing one coffee shop to store multiple coffee types and prices.

---

## Table 1: `coffee_shops`
This is the main table of the application.

It stores the core information for each coffee shop, including its identity, practical features, and general user-facing details.

### Columns

#### `id`
- Integer
- Primary key
- Autoincrement

Unique identifier for each coffee shop.

#### `name`
- Text
- Not null

Stores the coffee shop name.

#### `address`
- Text
- Not null

Stores the coffee shop address.

#### `rating`
- Real
- Not null

Stores the rating value of the coffee shop.

This rating is intended to represent the general public score used in the project, such as a Google rating.

Example values:
- 4.7
- 4.3
- 3.9

This allows users to compare cafés not only by price, but also by overall evaluation.

#### `work_friendly`
- Text
- Not null

Stores whether the coffee shop is suitable for working or studying.

Example values:
- Yes
- No
- Limited

#### `service_type`
- Text
- Not null

Stores whether the coffee shop offers sit-in service, takeaway service, or both.

Example values:
- Sit-in and takeaway
- Takeaway only
- Sit-in only

#### `irish_coffee`
- Integer
- Not null

Stores whether Irish coffee is available.

Example values:
- `1` = Yes
- `0` = No

#### `opening_time`
- Text
- Not null

Stores the opening time of the coffee shop.

Example:
- `08:00`

#### `closing_time`
- Text
- Not null

Stores the closing time of the coffee shop.

Example:
- `17:00`

#### `notes`
- Text
- Optional

Stores extra information or a short description of the place.

Examples:
- quiet in the morning
- better for takeaway
- good place for tourists
- limited seating upstairs

#### `image_filename`
- Text
- Not null

Stores the image file associated with the coffee shop.

Example:
- `cool-hand.jpg`

This supports the visual presentation of coffee shop cards and details pages.

---

## Table 2: `coffee_prices`
This table stores coffee types and prices for each coffee shop.

A separate table is necessary because one coffee shop can offer multiple drinks, and each drink may have a different price.

### Columns

#### `id`
- Integer
- Primary key
- Autoincrement

Unique identifier for each coffee price entry.

#### `coffee_shop_id`
- Integer
- Not null
- Foreign key referencing `coffee_shops(id)`

Connects each price entry to one coffee shop.

#### `coffee_type`
- Text
- Not null

Stores the type of coffee.

Example values:
- Americano
- Espresso
- Cappuccino
- Latte
- Flat White
- Irish Coffee

#### `price`
- Real
- Not null

Stores the price of that coffee type at that specific shop.

Example:
- `3.50`

---

## Relationship Between Tables

### `coffee_shops` → `coffee_prices`
The relationship between the two tables is:

- **one coffee shop**
- **many coffee price entries**

This means that one row in `coffee_shops` can be connected to several rows in `coffee_prices`.

### Example
A single coffee shop may have entries such as:

- Americano = €3.20
- Espresso = €2.80
- Latte = €4.00
- Irish Coffee = €8.50

This structure makes it possible to store detailed coffee menus without repeating the full coffee shop information every time.

---

## Why Two Tables Are Better Than One
Using two tables is better than placing everything in one large table.

This approach is more suitable because:

- one coffee shop can have many coffee types
- it avoids repeating coffee shop information
- it keeps the structure more organised
- it makes filtering by coffee type and price easier
- it is more scalable if the project expands later

A single-table design would be more limited and less flexible.

---

## Data Needed for Main Features

### For the Home Page Filters
The database must support filtering by:

- coffee type
- maximum price
- work-friendly suitability
- service type
- Irish coffee availability
- opening time
- closing time

These are the practical categories that define the main user experience of Sip Spot.

### For the Results Display
The database should return enough information to show coffee shop cards clearly, including:

- coffee shop name
- short address
- selected coffee type and price
- rating
- work-friendly category
- service type
- Irish coffee availability
- opening time
- closing time
- notes
- image filename for visual display

### For the Coffee Shop Details Page
The database should return the full information for one selected coffee shop, including:

- all general shop details
- all available coffee types
- all prices related to that shop

This allows the details page to provide a fuller and more useful view than the results cards.

---

## Example of How the Data Works

### Example row from `coffee_shops`
- `id`: 1
- `name`: Bean Corner
- `address`: Temple Bar, Dublin 2
- `rating`: 4.6
- `work_friendly`: Yes
- `service_type`: Sit-in and takeaway
- `irish_coffee`: 1
- `opening_time`: 08:00
- `closing_time`: 17:00
- `notes`: Quiet in the morning, busier in the afternoon
- `image_filename`: bean-corner.jpg

### Example rows from `coffee_prices`
- `coffee_shop_id`: 1, `coffee_type`: Americano, `price`: 3.20
- `coffee_shop_id`: 1, `coffee_type`: Espresso, `price`: 2.50
- `coffee_shop_id`: 1, `coffee_type`: Latte, `price`: 4.00
- `coffee_shop_id`: 1, `coffee_type`: Irish Coffee, `price`: 8.50

---

## What Is Included in Version 1
Version 1 of the database includes:

- one main table for coffee shop information
- one related table for coffee types and prices
- enough information to support filtering and detail display
- a simple and manageable relational structure

---

## What Is Not Included in Version 1
The following database features are outside the scope of Version 1:

- user accounts
- favourite lists
- review submissions
- ratings by users
- ranking history
- map coordinates
- API-based live updates

---

## Possible Future Database Expansion
In future versions, the database could include additional tables such as:

- `users`
- `favourites`
- `reviews`
- `areas`
- `rankings`

This would allow the app to grow beyond the first version.

---

## Final Database Summary
Sip Spot Version 1 will use a simple SQLite database with two main tables: `coffee_shops` and `coffee_prices`. This structure is enough to support the core experience of the application, including coffee shop listings, price filtering, practical comparisons, and detailed coffee shop pages. The structure is intentionally simple so the project remains realistic, functional, and well-organised.
