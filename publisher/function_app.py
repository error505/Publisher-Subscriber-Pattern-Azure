import azure.functions as func
import logging
import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Get Service Bus connection details from environment variables
SERVICE_BUS_CONNECTION_STR = os.getenv('ServiceBusConnection')
SERVICE_BUS_TOPIC_NAME = os.getenv('SERVICE_BUS_TOPIC_NAME', 'myServiceBusTopic')

app = func.FunctionApp()

@app.route(route="publishOrder", auth_level=func.AuthLevel.ANONYMOUS)
def publish_order(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing order request to publish to Azure Service Bus.')

    try:
        # Get order details from the HTTP request body
        order_data = req.get_json()
        order_id = order_data.get('orderId')
        customer_name = order_data.get('customerName')
        items = order_data.get('items')

        if not order_id or not customer_name or not items:
            raise ValueError('Order ID, Customer Name, or Items are missing.')

        # Connect to the Service Bus
        servicebus_client = ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STR)
        sender = servicebus_client.get_topic_sender(topic_name=SERVICE_BUS_TOPIC_NAME)

        # Create and send the message to the Service Bus topic
        with sender:
            message = ServiceBusMessage(body=str(order_data))
            sender.send_messages(message)

        logging.info(f"Order {order_id} for customer {customer_name} with items {items} published to Service Bus topic.")

        # Return a success response
        return func.HttpResponse(
            "Order published successfully.",
            status_code=200
        )

    except ValueError as e:
        logging.error(f"Error processing order: {e}")
        return func.HttpResponse(
            f"Invalid order data: {str(e)}",
            status_code=400
        )
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return func.HttpResponse(
            "An unexpected error occurred while processing the order.",
            status_code=500
        )
