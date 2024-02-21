from django.db import connections
from django.http import HttpResponse

def check_database_connection(request):
    try:
        # Use the default database connection
        connection = connections['default']

        # Execute a simple query to check the connection
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')

        # If the query is successful, the connection is established
        return HttpResponse('Database connection is successful')
    except Exception as e:
        # If there is an exception, the connection is not successful
        return HttpResponse(f'Database connection failed: {e}', status=500)
 
