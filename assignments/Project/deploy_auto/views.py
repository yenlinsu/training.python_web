from pyramid.view import view_config
from .models import Deploy_Auto
from pyramid_zodbconn import get_connection
from deform import Form, ValidationFailure

import colander

@view_config(context=Deploy_Auto, renderer='templates/base.pt')
def my_view(request):
    conn = get_connection(request)
    root = conn.root()
    return {'project': 'Network Deployment Automation System', 'page': root['app_root']}

class Store(colander.MappingSchema):
    store_number = colander.SchemaNode(colander.Integer())
    city = colander.SchemaNode(colander.String())
    state = colander.SchemaNode(colander.String())
    country = colander.SchemaNode(colander.String())
    region = colander.SchemaNode(colander.String())
    network = colander.SchemaNode(colander.String())

class Store_Number(colander.MappingSchema):
    store_number = colander.SchemaNode(colander.Integer())

@view_config(context=Deploy_Auto, name='deploy', renderer='templates/deploy.pt')
def view_deploy(request):
    conn = get_connection(request)
    root = conn.root()
    schema = Store()
    myform = Form(schema, buttons=('submit',))
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = myform.validate(controls)
        except ValidationFailure, e:
            return {
				'project': 'Network Deployment Automation System',
				'page': root['app_root'],
				'form': e.render(),
				'values': False,
				}
        values = {
            'store_number': appstruct['store_number'],
            'city': appstruct['city'],
            'state': appstruct['state'],
            'country': appstruct['country'],
            'region': appstruct['region'],
            'network': appstruct['network']
            }
        return {
            'project': 'Network Deployment Automation System', 
            'page': root['app_root'],
            'form': myform.render(),
            'values': values
            }
    
    return {
        'project': 'Network Deployment Automation System', 
        'page': root['app_root'], 
        'form': myform.render(), 
        'values': None
        }

@view_config(context=Deploy_Auto, name='query', renderer='templates/query.pt')
def view_query(request):
    conn = get_connection(request)
    root = conn.root()
    schema = Store_Number()
    myform = Form(schema, buttons=('submit',))
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = myform.validate(controls)
        except ValidationFailure, e:
            return {
                'project': 'Network Deployment Automation System',
                'page': root['app_root'],
                'form': e.render(),
                'values': False,
                }
        values = {
            'store_number': appstruct['store_number'],
            }     
        return {
            'project': 'Network Deployment Automation System',
            'page': root['app_root'],
            'form': myform.render(),
            'values': values
            }

    return {
        'project': 'Network Deployment Automation System',
        'page': root['app_root'],
        'form': myform.render(),
        'values': None
        }
