from flask import Blueprint, render_template, request
from database.cliente import CLIENTS


client_route = Blueprint('client', __name__)

@client_route.route('/')
def clients_list():
    """ List all clients registered in the database """
    return render_template('clients_list.html', clients=CLIENTS)

@client_route.route('/', methods=['POST'])
def insert_client():
    """ Insert the data of a new client into the database """
    
    data = request.json
    
    new_user = {
        "id": len(CLIENTS) + 1,
        "name": data['name'],
        "email": data['email'],
    }
    
    CLIENTS.append(new_user)
    
    return render_template('item_client.html', client=new_user)
    
@client_route.route('/new')
def form_client():
    """ Form to register a new client """
    return render_template('form_client.html')

@client_route.route('/<int:client_id>')
def client_details(client_id):
    """ Show the details of a client """
    return render_template('client_details.html')

@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    """ Form to edit the data of a client """
    return render_template('form_edit_client.html')

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    """ Update the data of a client in the database """
    pass


@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    """ Delete a client from the database """

    CLIENTS = [ c for c in CLIENTS if c['id'] != client_id ]