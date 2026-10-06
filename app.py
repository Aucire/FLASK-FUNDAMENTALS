from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'name':"Bread",
        'price':311.50
    }
]

@app.route("/products", methods=["GET"])
def get_product():
    return jsonify(data), 200


@app.post("/products")
def post_product():
    incoming = request.get_json()
    data.append(incoming)

    return jsonify("Posted successfully"), 201


if __name__ == "__main__":
    app.run(debug=True)