import azure.functions as func
import logging
import os
import json
from azure.cosmos import CosmosClient, exceptions

# Retrieve environment variables
COSMOS_DB_CONNECTION_STRING = os.getenv('COSMOS_DB_CONNECTION_STRING')
COSMOS_DB_DATABASE_NAME = os.getenv('COSMOS_DB_DATABASE_NAME', 'myDatabase')
COSMOS_DB_CONTAINER_NAME = os.getenv('COSMOS_DB_CONTAINER_NAME', 'myContainer')

app = func.FunctionApp()

@app.function_name(name="Subscriber1")
@app.service_bus_topic_trigger(
    connection="ServiceBusConnection",  # Connection string setting name
    topic_name="myServiceBusTopic",  # Name of the Service Bus topic
    subscription_name="subscription1",  # Name of the subscription
)
def subscriber1_function(message: func.ServiceBusMessage):
    logging.info('Received a message from Subscription 1.')

    try:
        # Parse the message body
        message_body = json.loads(message.get_body().decode('utf-8'))
        order_id = message_body.get('orderId')
        customer_name = message_body.get('customerName')
        items = message_body.get('items')

        if not order_id or not customer_name or not items:
            raise ValueError('Order ID, Customer Name, or Items are missing in the message.')

        # Initialize the Cosmos DB client
        cosmos_client = CosmosClient.from_connection_string(COSMOS_DB_CONNECTION_STRING)
        database = cosmos_client.get_database_client(COSMOS_DB_DATABASE_NAME)
        container = database.get_container_client(COSMOS_DB_CONTAINER_NAME)

        # Upsert the order data into Cosmos DB
        container.upsert_item({
            'id': order_id,
            'customerName': customer_name,
            'items': items,
            'status': 'Processed'
        })

        logging.info(f"Order {order_id} for customer {customer_name} processed and stored in Cosmos DB.")

    except ValueError as e:
        logging.error(f"Invalid message data: {e}")
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Cosmos DB error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
