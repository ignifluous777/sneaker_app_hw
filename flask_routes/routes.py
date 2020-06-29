from flask import Flask, request, jsonify
from models.sneaker_listing import SneakList

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def show_status():
    return jsonify({"status": "success"})

@app.route("/sneaklist/view_by_lister", methods=["GET", "POST"])
def show_by_lister():
    lister = request.get_json().get("lister")
    lister_list = SneakList.view_by_lister(lister)
    return jsonify({"Sneaker_list_by_lister": lister_list})

@app.route("/sneaklist/add", methods=["POST"])
def add_sneak():
    data = request.get_json()
    if data is None:
        return jsonify({"success": False})
    new_listing = SneakList(**data)
    success = new_listing.insert()
    return jsonify({"success": success})

@app.route("/sneaklist/update", methods=["POST"])
def update_sneak():
    data = request.get_json()
    if data is None:
        return jsonify({"success": False})
    new_listing = SneakList(**data)
    success = new_listing.update()
    return jsonify({"success": success})

@app.route("/sneaklist/delete")
def delete_item():
    pk = request.get_json().get("pk")
    if pk is None:
        return jsonify({"success": False})
    success = SneakList.delete(pk)
    return jsonify({"success": success})

@app.route("/sneaklist/view_below_price", methods=["GET", "POST"])
def view_below_price():
    given_price = request.get_json().get("given_price")
    below_price_list = SneakList.view_below_price(given_price)
    return jsonify({"Sneaker_list_below_given_price": below_price_list})

@app.route("/sneaklist/view_by_manufac/", methods=["GET", "POST"])
def view_by_manufac():
    manufac = request.get_json().get("manufac")
    manufac_list = SneakList.view_by_manufac(manufac)
    return jsonify({"Sneaker_list_by_manufacturer": manufac_list})

@app.route("/view_by_50below")
def view_by_50below():
    below50_list = SneakList.view_by_50below()
    return jsonify({"Sneaker_list_by_below_50percent_original_price": below50_list})

if __name__ == "__main__":
    app.run()
