import json





def build_response(status_code, response):
        return {
            "statusCode": status_code,
            "headers": {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PATCH,DELETE",
            },
            "body": json.dumps(response),
        }




def handler(event, context):

    http_method = event.get("httpMethod")

    if http_method == 'GET': 
        return get_products(event)
    elif http_method == 'POST':
        return create_products(event)
    
    elif http_method == 'PATCH': 
        return update_products(event)
    
    elif http_method == 'DELETE':
        return delete_products(event)
    
    




def create_products(event):
    return build_response(200,'successfully created')

def get_products(event):

    return build_response(200 ,'successfully get' )

def update_products(event):
    return build_response(200, 'successfully updated')

def delete_products(event):
    return build_response(200 , 'successfully deleted')





