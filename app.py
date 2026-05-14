from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("sipspot.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()

    coffee_type = request.args.get("coffee_type", "Any")
    max_price = request.args.get("max_price", "Any")
    working = request.args.get("working", "Any")
    service_type = request.args.get("service_type", "Any")
    irish_coffee = request.args.get("irish_coffee", "Any")
    opens_from = request.args.get("opens_from", "")
    closes_after = request.args.get("closes_after", "")

    query = """
        SELECT DISTINCT
            cs.id,
            cs.name,
            cs.address,
            cs.rating,
            cs.work_friendly,
            cs.service_type,
            cs.irish_coffee,
            cs.opening_time,
            cs.closing_time,
            cs.notes,
            cs.image_filename
        FROM coffee_shops cs
        LEFT JOIN coffee_prices cp ON cs.id = cp.coffee_shop_id
        WHERE 1=1
    """
    params = []

    if coffee_type != "Any":
        query += " AND cp.coffee_type = ?"
        params.append(coffee_type)

    if max_price != "Any":
        query += " AND cp.price <= ?"
        params.append(float(max_price))

    if working != "Any":
        query += " AND cs.work_friendly = ?"
        params.append(working)

    if service_type != "Any":
        query += " AND cs.service_type = ?"
        params.append(service_type)

    if irish_coffee != "Any":
        if irish_coffee == "Yes":
            query += " AND cs.irish_coffee = 1"
        else:
            query += " AND cs.irish_coffee = 0"

    if opens_from:
        query += " AND cs.opening_time <= ?"
        params.append(opens_from)

    if closes_after:
        query += " AND cs.closing_time >= ?"
        params.append(closes_after)

    query += " ORDER BY cs.name"

    coffee_shops = conn.execute(query, params).fetchall()

    display_cards = []
    for shop in coffee_shops:
        if coffee_type != "Any":
            display_price = conn.execute(
                """
                SELECT coffee_type, price
                FROM coffee_prices
                WHERE coffee_shop_id = ? AND coffee_type = ?
                LIMIT 1
                """,
                (shop["id"], coffee_type)
            ).fetchone()
        else:
            display_price = conn.execute(
                """
                SELECT coffee_type, price
                FROM coffee_prices
                WHERE coffee_shop_id = ?
                ORDER BY
                    CASE
                        WHEN coffee_type = 'Americano' THEN 1
                        WHEN coffee_type = 'Espresso' THEN 2
                        WHEN coffee_type = 'Latte' THEN 3
                        ELSE 4
                    END,
                    price ASC
                LIMIT 1
                """,
                (shop["id"],)
            ).fetchone()

        display_cards.append({
            "id": shop["id"],
            "name": shop["name"],
            "address": shop["address"],
            "rating": shop["rating"],
            "work_friendly": shop["work_friendly"],
            "service_type": shop["service_type"],
            "irish_coffee": shop["irish_coffee"],
            "opening_time": shop["opening_time"],
            "closing_time": shop["closing_time"],
            "notes": shop["notes"],
            "image_filename": shop["image_filename"],
            "display_coffee_type": display_price["coffee_type"] if display_price else "No price",
            "display_price": display_price["price"] if display_price else None
        })

    conn.close()

    filters = {
        "coffee_type": coffee_type,
        "max_price": max_price,
        "working": working,
        "service_type": service_type,
        "irish_coffee": irish_coffee,
        "opens_from": opens_from,
        "closes_after": closes_after
    }

    return render_template("index.html", coffee_shops=display_cards, filters=filters)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/coffee/<int:shop_id>")
def coffee_details(shop_id):
    conn = get_db_connection()

    shop = conn.execute(
        """
        SELECT id, name, address, rating, work_friendly, service_type,
               irish_coffee, opening_time, closing_time, notes, image_filename
        FROM coffee_shops
        WHERE id = ?
        """,
        (shop_id,)
    ).fetchone()

    prices = conn.execute(
        """
        SELECT coffee_type, price
        FROM coffee_prices
        WHERE coffee_shop_id = ?
        ORDER BY
            CASE
                WHEN coffee_type = 'Americano' THEN 1
                WHEN coffee_type = 'Espresso' THEN 2
                WHEN coffee_type = 'Latte' THEN 3
                WHEN coffee_type = 'Flat White' THEN 4
                WHEN coffee_type = 'Cappuccino' THEN 5
                WHEN coffee_type = 'Irish Coffee' THEN 6
                ELSE 7
            END
        """,
        (shop_id,)
    ).fetchall()

    conn.close()

    if shop is None:
        return "Coffee shop not found", 404

    return render_template("details.html", shop=shop, prices=prices)


if __name__ == "__main__":
    app.run(debug=True)
