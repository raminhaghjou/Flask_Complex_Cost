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

tc = TownCost()
bc = BlockCost()
fc = FloorCost()
uc = UnitCost()

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Complex Cost API!'

@app.route('/town-cost',methods=['POST'])
def town_cost():
    if "id" in request.form and "cost" in request.form:
        id = request.form["id"]
        cost = request.form["cost"]
        if int(id) in town:
            # tc = TownCost()
            tc.set_item(int(cost))
            # price["town"].append({"id" : int(id), "cost" : int(cost)})
            price["town"].append({"id" : int(id), "cost" : tc.__getitem__(int(id))})
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
            return jsonify(str(tc.__getitem__(int(id)))), 200#jsonify(str(matching_dicts[0])), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200

@app.route('/town-cost',methods=['Delete'])
def delete_town_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["town"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            tc.__delitem__(int(id))
            price["town"].remove(matching_dicts[0])
            return "",200
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
            # bc = BlockCost()
            bc.set_item(int(cost))
            # price["block"].append({"id" : int(id), "cost" : int(cost)})
            price["block"].append({"id" : int(id), "cost" : tc.__getitem__(int(id))})
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
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["block"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(bc.__getitem__(int(id)))), 200 #jsonify(str(matching_dicts[0])), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


@app.route('/block-cost',methods=['Delete'])
def delete_block_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["block"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            bc.__delitem__(int(id))
            price["block"].remove(matching_dicts[0])
            return "",200
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
            # fc = FloorCost()
            fc.set_item(int(cost))
            price["floor"].append({"id" : int(id), "cost" : fc.__getitem__(int(id))})
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200



@app.route('/floor-cost',methods=['Get'])
def show_floor_cost():
    if "id" in request.args:
        id = request.args("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["floor"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(fc.__getitem__(int(id)))), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


@app.route('/floor-cost',methods=['Delete'])
def delete_floor_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["floor"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            fc.__delitem__(id)
            price["floor"].remove(matching_dicts[0])
            return "",200
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
            # uc = UnitCost()
            uc.set_item(int(cost))
            price["unit"].append({"id" : int(id), "cost" : uc.__getitem__(int(id))})
            return "", 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 403
        
    else:
        return jsonify({"Error": "Missing input parameters [id or cost]"})
    
    return "Success", 200

@app.route('/unit-cost',methods=['Get'])
def show_unit_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["unit"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            return jsonify(str(uc.__getitem__(int(id)))), 200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200


@app.route('/unit-cost',methods=['Delete'])
def delete_unit_cost():
    if "id" in request.args:
        id = request.args.get("id")
        matching_dicts = list(filter(lambda x: x["id"] == int(id), price["unit"]))
        if len(matching_dicts) > 0:                                            #any(id in d for d in cost_town["town"]):
            uc.__delitem__(id)
            price["unit"].remove(matching_dicts[0])
            return "",200
        else:
            return jsonify({"Error": "Id is not valid","id" : id}), 500
        
    else:
        return jsonify({"Error": "Missing input parameters [id]"})
    
    return "Success", 200



if __name__ == '__main__':
    app.run(debug=True)