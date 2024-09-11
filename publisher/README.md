# Publisher (Azure Function)

This folder contains the Python code for the publisher service that sends messages to the Azure Service Bus topic. The publisher simulates a webshop sending order details (such as what items have been ordered) to be processed by various subscribers.

## 📑 Files

- **`function_app.py`**: The Python code for the Azure Function that publishes messages to the Azure Service Bus.
- **`requirements.txt`**: Lists all dependencies required by the Azure Function.
- **`deploy-publisher.yml`**: GitHub Action workflow to automate the deployment of the publisher.

## 🚀 How to Deploy

### Prerequisites

1. **Azure Subscription**: You need an active Azure account to deploy resources.
2. **Azure Service Bus**: Ensure you have an Azure Service Bus namespace, topic, and subscriptions created (using the Bicep template in the `/infrastructure` folder).
3. **GitHub Repository**: This repository should be cloned to your local machine for any modifications or testing.
4. **GitHub Secrets Configuration**: 
   - **`AZURE_CREDENTIALS`**: Azure Service Principal credentials in JSON format.
   - **`AZURE_FUNCTIONAPP_PUBLISH_PROFILE`**: Publish profile for the Azure Function App.
   - **`ServiceBusConnection`**: Connection string for the Azure Service Bus namespace.

### Steps to Deploy the Publisher

1. **Add Required Secrets to GitHub**:
   - Go to your repository's **Settings > Secrets and variables > Actions > New repository secret**.
   - Add the following secrets:
     - **`AZURE_CREDENTIALS`**: Your Azure service principal credentials.
     - **`AZURE_FUNCTIONAPP_PUBLISH_PROFILE`**: The publish profile for your Azure Function App.
     - **`ServiceBusConnection`**: The connection string for your Azure Service Bus namespace.

2. **Push Changes to the `main` Branch**:
   - Commit and push the changes to the `main` branch of your repository. This will automatically trigger the GitHub Action workflow to deploy the publisher Azure Function.

3. **Monitor the Deployment**:
   - Go to the **Actions** tab in your GitHub repository.
   - Select the **Deploy Publisher Azure Function** workflow to monitor the deployment progress.

### 📂 Folder Structure

- **`function_app.py`**: Azure Function code to publish messages.
- **`requirements.txt`**: Python dependencies for the Azure Function.
- **`.github/workflows/deploy-publisher.yml`**: GitHub Actions workflow file for deployment.

## 📝 Usage Instructions

### How to Publish Messages

1. **Trigger the Publisher Function**:
   - Use an HTTP client (such as Postman or `curl`) to send a POST request to the publisher Azure Function endpoint (`/publishOrder`).
   
2. **Example HTTP Request**:

   ```bash
   curl -X POST https://<your-function-app-name>.azurewebsites.net/api/publishOrder \
   -H "Content-Type: application/json" \
   -d '{
       "orderId": "12345",
       "customerName": "John Doe",
       "items": ["Laptop", "Smartphone", "Headphones"]
   }'
   ```

   Replace `<your-function-app-name>` with the name of your deployed Azure Function App.

3. **Expected Response**:

   - If successful, you should receive a response:

   ``` json
   Order published successfully.
   ```

   - If there is an error, you will receive an appropriate error message indicating the issue.

## 🔧 Customization

- **Service Bus Topic Name**: You can customize the topic name by modifying the `SERVICE_BUS_TOPIC_NAME` environment variable in the GitHub Action or Azure Portal.
- **Order Message Content**: Modify the structure and content of the messages in the `function_app.py` file according to your requirements.

## 💡 Additional Notes

- **Scaling**: This function can be scaled based on the Azure Function consumption plan, allowing it to handle varying loads efficiently.
- **Security**: Ensure your Azure Service Bus connection string (`ServiceBusConnection`) is kept secure and not exposed in your code or logs.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
