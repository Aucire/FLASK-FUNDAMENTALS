from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'name':"Bread",
        'price':311.50
    },
    {
        'id': 2,
        "name": 'wfwerfe',
        'price': 324324
    }
]

@app.route("/products", methods=["GET"])
def get_product():
    return jsonify(data), 200


@app.post("/products")
def post_product():
    incoming = request.get_json()
    
    new_id = max((i['id'] for i in data),default=0 )+ 1
    incoming['id'] = new_id
    
    data.append(incoming)
    return jsonify("Posted successfully"), 201


@app.delete("/products/<int:my_id>")
def delete_pro(my_id):
    for item in data:
        if item['id'] == my_id:
            data.remove(item)
            return jsonify("Product deleted successfully"), 200
        
    return jsonify("No product found...!"), 404


@app.patch("/products/<int:my_id>")
def patch(my_id):
    incoming = request.get_json()

    for item in data:
        if item['id'] == my_id:
            item['name'] =  incoming['name']
            return jsonify("Product patched successfully."), 200

    return jsonify("Product not found"), 404
        
if __name__ == "__main__":
    app.run(debug=True)