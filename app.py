from flask import Flask, flash, jsonify, request
from BuildingCost.town_cost import TownCost
from BuildingCost.block_cost import BlockCost
from BuildingCost.floor_cost import FloorCost
from BuildingCost.unit_cost import UnitCost


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
            tc = TownCost()
            tc.set_item(int(cost))
            price["town"].append({"id" : int(id), "cost" : int(cost)})
            flash('You cost successfully inserted')
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500 #raise ValueError("Id is not valid", 500)
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return 204

@app.route('/town-cost',methods=['Get'])
def show_town_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["town"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(matching_dicts[0])), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


@app.route('/block-cost',methods=['POST'])
def block_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in block:
            bc = BlockCost()
            bc.set_item(int(cost))
            price["block"].append({"id" : int(id), "cost" : int(cost)})
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200


app.route('/block-cost',methods=['GET'])
def show_block_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["block"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(matching_dicts[0])), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200



@app.route('/floor-cost',methods=['POST'])
def floor_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in floor:
            fc = FloorCost()
            fc.set_item(int(cost))
            price["floor"].append({"id" : int(id), "cost" : int(cost)})
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200



app.route('/floor-cost',methods=['Get'])
def show_floor_cost():
    if "id" in request.args:
        id = request.args("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["floor"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(matching_dicts[0])), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


@app.route('/unit-cost',methods=['POST'])
def unit_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in unit:
            uc = UnitCost()
            uc.set_item(int(cost))
            price["unit"].append({"id" : int(id), "cost" : int(cost)})
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200

app.route('/unit-cost',methods=['Get'])
def show_unit_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["unit"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(matching_dicts[0])), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


if __name__ == '__main__':
    app.run(debug=True)