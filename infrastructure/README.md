# Infrastructure Deployment with Bicep and GitHub Actions

This folder contains the **Bicep template** and a **GitHub Action** workflow to automate the deployment of the Azure infrastructure needed for the **Publisher-Subscriber Pattern** implementation.

## 📑 Files

- **`azure-resources.bicep`**: A Bicep template file that defines all necessary Azure resources, including:
  - **Azure Service Bus**: Namespace, topic, and subscriptions.
  - **Azure Functions**: For the publisher and subscribers.
  - **Azure App Service**: (Optional) for the publisher.
  - **Azure Cosmos DB**: For data storage by Subscriber 1.
  - **Azure Storage Account**: For data storage by Subscriber 2.
- **`deploy-bicep.yml`**: GitHub Action workflow file to automate the deployment of the infrastructure using the Bicep template.

## 🚀 How to Deploy the Infrastructure

To deploy the infrastructure, follow these steps:

1. **Configure GitHub Secrets**:
   - Go to your repository's **Settings > Secrets and variables > Actions > New repository secret**.
   - Add the following secrets:
     - **`AZURE_CLIENT_ID`**: Your Azure service principal's client ID.
     - **`AZURE_CLIENT_SECRET`**: Your Azure service principal's client secret.
     - **`AZURE_TENANT_ID`**: Your Azure tenant ID.

2. **Trigger the GitHub Action**:
   - **Push changes** to the `main` branch or **manually trigger** the workflow via the **GitHub Actions** tab.

3. **Monitor the Deployment**:
   - Go to the **Actions** tab in your GitHub repository.
   - Select the **Deploy Azure Infrastructure with Bicep** workflow to monitor the deployment progress.

## 🔧 Prerequisites

- **Azure Subscription**: You need an active Azure account to deploy resources.
- **Service Principal Credentials**: Required for the GitHub Action to authenticate and deploy resources to Azure.
- **GitHub Repository**: Clone this repository to your local machine to make changes.

## 📂 Folder Structure

- **`azure-resources.bicep`**: Bicep template for Azure resources.
- **`.github/workflows/deploy-bicep.yml`**: GitHub Actions workflow file for deployment.

## 💡 Understanding the GitHub Action

The **GitHub Action** workflow is defined in the `deploy-bicep.yml` file and performs the following steps:

1. **Checkout Code**: Uses `actions/checkout@v2` to check out the repository code.
2. **Set Up Azure CLI**: Uses `azure/cli@v2.1.0` to set up the Azure CLI environment.
3. **Deploy Bicep Template**: Logs in to Azure using a service principal and deploys the Bicep template to the specified resource group.

### `deploy-bicep.yml` Workflow

Here’s the workflow file:

```yaml
name: Deploy Azure Infrastructure with Bicep

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy-infrastructure:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Azure CLI
      uses: azure/cli@v2.1.0
      with:
        azcliversion: 'latest'
        inlineScript: |
          # Log in to Azure
          az login --service-principal -u ${{ secrets.AZURE_CLIENT_ID }} -p ${{ secrets.AZURE_CLIENT_SECRET }} --tenant ${{ secrets.AZURE_TENANT_ID }}

          # Deploy Bicep Template
          az deployment group create --resource-group <your-resource-group> --template-file infrastructure/azure-resources.bicep
```

## 🛠️ Customizing the Deployment

You can customize the deployment by modifying the **Bicep template** (`azure-resources.bicep`) to change resource configurations, such as the service bus topic name, function app names, and other resource properties.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.