# Subscriber 1 (Azure Function)

This folder contains the Python code for **Subscriber 1**, an Azure Function that listens to messages from **Subscription 1** on the Azure Service Bus topic and processes them by storing the data in **Azure Cosmos DB**.

## 📑 Files

- **`function_app.py`**: The Python code for the Azure Function that processes messages.
- **`requirements.txt`**: Lists the dependencies required by the Azure Function.
- **`deploy-subscriber1.yml`**: GitHub Action workflow to automate the deployment of Subscriber 1.

## 🚀 How to Deploy

### Prerequisites

1. **Azure Subscription**: You need an active Azure account to deploy resources.
2. **Azure Service Bus**: Ensure the Azure Service Bus namespace, topic, and subscription (`subscription1`) are created (using the Bicep template in the `/infrastructure` folder).
3. **Azure Cosmos DB**: Ensure the Azure Cosmos DB account, database, and container are created (using the Bicep template in the `/infrastructure` folder).
4. **GitHub Secrets Configuration**:
   - **`AZURE_CREDENTIALS`**: Azure Service Principal credentials in JSON format.
   - **`AZURE_FUNCTIONAPP_PUBLISH_PROFILE`**: Publish profile for the Azure Function App.
   - **`ServiceBusConnection`**: Connection string for the Azure Service Bus namespace.
   - **`COSMOS_DB_CONNECTION_STRING`**: Connection string for the Azure Cosmos DB account.

### Steps to Deploy Subscriber 1

1. **Add Required Secrets to GitHub**:
   - Go to your repository's **Settings > Secrets and variables > Actions > New repository secret**.
   - Add the following secrets:
     - **`AZURE_CREDENTIALS`**: Your Azure service principal credentials.
     - **`AZURE_FUNCTIONAPP_PUBLISH_PROFILE`**: The publish profile for your Azure Function App.
     - **`ServiceBusConnection`**: The connection string for your Azure Service Bus namespace.
     - **`COSMOS_DB_CONNECTION_STRING`**: The connection string for your Azure Cosmos DB account.

2. **Push Changes to the `main` Branch**:
   - Commit and push the changes to the `main` branch of your repository. This will automatically trigger the GitHub Action workflow to deploy the Subscriber 1 Azure Function.

3. **Monitor the Deployment**:
   - Go to the **Actions** tab in your GitHub repository.
   - Select the **Deploy Subscriber 1 Azure Function** workflow to monitor the deployment progress.

## 📂 Folder Structure

- **`function_app.py`**: Azure Function code to process messages.
- **`requirements.txt`**: Python dependencies for the Azure Function.
- **`.github/workflows/deploy-subscriber1.yml`**: GitHub Actions workflow file for deployment.

## 📝 Usage Instructions

### How Subscriber 1 Processes Messages

1. **Service Bus Trigger**:
   - The function is automatically triggered when a message is published to **Subscription 1** on the Azure Service Bus topic.

2. **Processing Logic**:
   - The function extracts the order details from the message and stores them in Azure Cosmos DB.

3. **Monitoring**:
   - You can monitor the function's execution and logs in the Azure portal under the **Function App > Monitor** section.

## 🔧 Customization

- **Cosmos DB Details**: Modify the Cosmos DB database and container names in the environment variables or code as needed.
- **Message Processing Logic**: Update the message processing logic in `function_app.py` to handle different types of data.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.