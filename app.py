from flask import Flask, flash, jsonify, request, json
from BuildingCost.town_cost import TownCost
from BuildingCost.block_cost import BlockCost
from BuildingCost.floor_cost import FloorCost
from BuildingCost.unit_cost import UnitCost


app = Flask(__name__)

town = [1, 2, 3, 4]
block = [5, 6, 7, 8, 9]
floor = [10, 11, 12, 13, 14]
unit = [15, 16, 17, 18]

price = {"town":[], "floor":[], "block": [], "unit":[]}


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Complex Cost API!'

@app.route('/town-cost',methods=['POST'])
def town_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in town:
            tc = TownCost(int(cost))
            price["town"].append([id, tc])
            return "", 204
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500 #raise ValueError("Id is not valid", 500)
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return 204

@app.route('/town-cost',methods=['Get'])
def show_town_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["town"]:
            if i[0] == id:
                return jsonify({"id": i[0], "cost": str(i[1].__dict__)}), 200
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return 204


@app.route('/town-cost',methods=['Delete'])
def delete_town_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["town"]:
            if i[0] == id:
                price["town"].remove(i)
                return "", 204
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


@app.route('/block-cost',methods=['POST'])
def block_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in block:
            bc = BlockCost(int(cost))
            price["block"].append([id, bc])
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200


@app.route('/block-cost',methods=['GET'])
def show_block_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["block"]:
            if i[0] == id:
                return jsonify({"id": i[0], "cost": str(i[1].__dict__)}), 200
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return 204


@app.route('/block-cost',methods=['Delete'])
def delete_block_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["block"]:
            if i[0] == id:
                price["block"].remove(i)
                return "", 204
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200




@app.route('/floor-cost',methods=['POST'])
def floor_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in floor:
            fc = FloorCost(int(cost))
            price["floor"].append([id, fc])
            return "", 204
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200



@app.route('/floor-cost',methods=['Get'])
def show_floor_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["floor"]:
            if i[0] == id:
                return jsonify({"id": i[0], "cost": str(i[1].__dict__)}), 200
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return 204


@app.route('/floor-cost',methods=['Delete'])
def delete_floor_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["floor"]:
            if i[0] == id:
                price["floor"].remove(i)
                return "", 204
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200



@app.route('/unit-cost',methods=['POST'])
def unit_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in unit:
            uc = UnitCost(int(cost))
            price["unit"].append([id, uc])
            return "", 204
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200

@app.route('/unit-cost',methods=['Get'])
def show_unit_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["unit"]:
            if i[0] == id:
                return jsonify({"id": i[0], "cost": str(i[1].__dict__)}), 200
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return 204


@app.route('/unit-cost',methods=['Delete'])
def delete_unit_cost():
    if "id" in request.args:
        id = request.args.get("id")
        for i in price["unit"]:
            if i[0] == id:
                price["unit"].remove(i)
                return "", 204
            else: return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200



if __name__ == '__main__':
    app.run(debug=True)