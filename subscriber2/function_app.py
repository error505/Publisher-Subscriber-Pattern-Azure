import azure.functions as func
import logging
import os
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Retrieve environment variables
STORAGE_CONNECTION_STRING = os.getenv('STORAGE_CONNECTION_STRING')
STORAGE_CONTAINER_NAME = os.getenv('STORAGE_CONTAINER_NAME', 'orders-container')

app = func.FunctionApp()

@app.function_name(name="Subscriber2")
@app.service_bus_topic_trigger(
    connection="ServiceBusConnection",  # Connection string setting name
    topic_name="myServiceBusTopic",  # Name of the Service Bus topic
    subscription_name="subscription2",  # Name of the subscription
)
def subscriber2_function(message: func.ServiceBusMessage):
    logging.info('Received a message from Subscription 2.')

    try:
        # Parse the message body
        message_body = json.loads(message.get_body().decode('utf-8'))
        order_id = message_body.get('orderId')
        customer_name = message_body.get('customerName')
        items = message_body.get('items')

        if not order_id or not customer_name or not items:
            raise ValueError('Order ID, Customer Name, or Items are missing in the message.')

        # Initialize the Azure Blob Storage client
        blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(STORAGE_CONTAINER_NAME)

        # Ensure the container exists
        container_client.create_container()

        # Create a blob file name using the order ID
        blob_name = f"order-{order_id}.json"

        # Upload the order data to Azure Blob Storage
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(json.dumps(message_body), overwrite=True)

        logging.info(f"Order {order_id} for customer {customer_name} processed and stored in Azure Blob Storage.")

    except ValueError as e:
        logging.error(f"Invalid message data: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
