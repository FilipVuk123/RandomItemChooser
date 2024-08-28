from flask import Flask, render_template, request
import secrets

app = Flask(__name__)

def choose_random_item(items):
    """
    Chooses a random item from the provided list of items.

    Parameters:
    items (list): A list of items to choose from.

    Returns:
    any: A randomly chosen item from the list.
    """
    if not items:
        return "The list is empty. Please provide a list with at least one item."

    chosen_item = secrets.choice(items)
    return chosen_item

@app.route("/", methods=["GET", "POST"])
def index():
    selected_item = None
    if request.method == "POST":
        # Get the input from the form
        items_input = request.form["items"]
        # Split the input string into a list of items
        item_list = [item.strip() for item in items_input.split(",")]
        # Choose a random item from the list
        selected_item = choose_random_item(item_list)

    return render_template("index.html", selected_item=selected_item)

if __name__ == "__main__":
    app.run(debug=True)
