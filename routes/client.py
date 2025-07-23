from flask import Blueprint, render_template
from database.cliente import CLIENTS


client_route = Blueprint('client', __name__)

@client_route.route('/')
def clients_list():
    """ List all clients registered in the database """
    return render_template('clients_list.html', clients=CLIENTS)

@client_route.route('/', methods=['POST'])
def insert_client():
    """ Insert the data of a new client into the database """
    pass

@client_route.route('/new')
def form_client():
    """ Form to register a new client """
    return render_template('form_client.html')

@client_route.route('/<int:client_id>')
def client_details(id):
    """ Show the details of a client """
    return render_template('client_details.html')

@client_route.route('/<int:client_id>/edit')
def form_edit_client(id):
    """ Form to edit the data of a client """
    return render_template('form_edit_client.html')

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(id):
    """ Update the data of a client in the database """
    pass


@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(id):
    """ Delete a client from the database """
    pass