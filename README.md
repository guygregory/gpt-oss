# Deploy gpt-oss-120b on Azure OpenAI

Python code samples for OpenAI's gpt-oss model on Azure OpenAI.

## Overview

This repository contains Python sample code for interacting with the gpt-oss-120b model deployed on Azure AI Foundry. The gpt-oss model is OpenAI's reasoning model that provides transparent access to its reasoning process.

## Prerequisites

- Python 3.7 or higher
- Azure subscription
- Azure CLI (optional, for deployment via command line)

## Deployment Guide

Follow these steps to deploy and use the gpt-oss model:

### Step 1: Deploy an Azure AI Foundry Project

Deploy an Azure AI Foundry Project in one of the supported regions:
- `eastus`
- `francecentral`
- `southcentralus`
- `uksouth`
- `westcentralus`
- `westeurope`

📖 **Detailed instructions**: [Create Azure AI Foundry Projects](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry&pivots=fdp-project)

### Step 2: Deploy the gpt-oss-120b Model

Deploy the gpt-oss-120b model using one of the following methods:

#### Option A: Azure Portal
1. Navigate to your Azure AI Foundry Project
2. Go to the Model catalog
3. Search for and select "gpt-oss-120b"
4. Click "Deploy" and follow the deployment wizard

#### Option B: Azure CLI
```bash
az cognitiveservices account deployment create \
  --resource-group <your-resource-group> \
  --name <foundry-resource-name> \
  --deployment-name "gpt-oss-120b" \
  --model-name gpt-oss-120b \
  --model-version 1 \
  --model-format "OpenAI-OSS" \
  --sku-name GlobalStandard \
  --sku-capacity 1
```

Replace `<your-resource-group>` and `<foundry-resource-name>` with your actual values.

### Step 3: Set Up the Project

1. **Clone this repository**:
   ```bash
   git clone https://github.com/guygregory/gpt-oss.git
   cd gpt-oss
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   ```bash
   cp .env.sample .env
   ```

4. **Update the `.env` file** with values from your Azure AI Foundry Project:
   - `AZURE_OPENAI_API_ENDPOINT`: Your foundry endpoint (format: `https://<FOUNDRY_RESOURCE_NAME>.openai.azure.com/`)
   - `AZURE_OPENAI_V1_API_ENDPOINT`: Your foundry v1 endpoint (format: `https://<FOUNDRY_RESOURCE_NAME>.openai.azure.com/openai/v1/`)
   - `AZURE_OPENAI_API_KEY`: Your API key (found under "Keys and Endpoint" in your project)
   - `AZURE_OPENAI_API_MODEL`: Your deployment name (default: `gpt-oss-120b`)

### Step 4: Run the Sample Code

Choose one of the Python samples based on your preferred API:

#### Legacy Azure OpenAI API
```bash
python chat-basic-aoai.py
```

#### V1 Preview API
```bash
python chat-basic-aoai-v1.py
```

Both samples will:
1. Send a simple chat message to the gpt-oss model
2. Display the model's reasoning process
3. Show the final response

## Sample Code Features

### chat-basic-aoai.py (Legacy API)
- Uses the `AzureOpenAI` client from the OpenAI Python SDK
- Connects via the standard Azure OpenAI endpoint
- API version: `2025-04-01-preview`

### chat-basic-aoai-v1.py (V1 Preview API)
- Uses the standard `OpenAI` client with Azure base URL
- Connects via the v1 preview endpoint
- Provides access to the latest API features

## Environment Variables Reference

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `AZURE_OPENAI_API_ENDPOINT` | Azure OpenAI endpoint (legacy) | Yes | `https://myproject.openai.azure.com/` |
| `AZURE_OPENAI_V1_API_ENDPOINT` | Azure OpenAI v1 endpoint | Yes | `https://myproject.openai.azure.com/openai/v1/` |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | Yes | `abc123...` |
| `AZURE_OPENAI_API_MODEL` | Model deployment name | No (default: gpt-oss-120b) | `gpt-oss-120b` |
| `AZURE_OPENAI_API_VERSION` | API version | No (default: 2025-04-01-preview) | `2025-04-01-preview` |

## Troubleshooting

### Common Issues

1. **Authentication Error**: Verify your API key and endpoint URL are correct
2. **Model Not Found**: Ensure the deployment name matches your Azure deployment
3. **Region Not Supported**: Verify you deployed in one of the supported regions
4. **Rate Limiting**: The gpt-oss model has usage quotas; check your deployment capacity

### Getting Help

- Check the [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- Review Azure OpenAI service logs in the Azure portal
- Verify your deployment status in the Azure AI Foundry project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
