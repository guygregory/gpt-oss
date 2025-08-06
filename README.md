# Deploy gpt-oss-120b on Azure OpenAI
<img width="719" height="633" alt="gpt-oss" src="https://github.com/user-attachments/assets/a9bb27cb-c851-478d-a102-d03554edcbeb" />

## Overview

This repo contains Python sample code for interacting with the gpt-oss-120b model deployed on Azure AI Foundry using Chat Completions. The gpt-oss models are OpenAI's open weight models that provide transparent access to its reasoning process.

## Prerequisites

- Python 3.7 or higher
- Azure subscription
- Azure CLI (optional, for deployment via command line)

## Deployment Guide

Follow these steps to deploy and use the gpt-oss-120b model:

### Step 1: Deploy an Azure AI Foundry Project*

Deploy an Azure AI Foundry Project if you don't already have one available.

\* According to Microsoft Learn, [gpt-oss will eventually be available in all regions](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#gpt-oss). At time of testing, these are the regions I could find it. I personally tested this using a Foundry Project in UK South.

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

Choose one of the Python samples:

#### Gradio example (see above screenshot)
```bash
python chat-gradio-aoai.py
```

#### Legacy Azure OpenAI API
```bash
python chat-basic-aoai.py
```

#### V1 Preview API
```bash
python chat-basic-aoai-v1.py
```

## Why are there two different APIs? Which should I use?
Starting in May 2025, you can now opt in to our next generation of v1 Azure OpenAI APIs which add support for:
- Ongoing access to the latest features with no need to update api-version each month.
- OpenAI client support with minimal code changes to swap between OpenAI and Azure OpenAI when using key-based authentication.

Code samples have been provided for both the v1 API Preview, and also the older API versions. The v1 API Preview samples have a v1.py suffix to distinguish them.

If you want the latest features, I would recommend using the v1 API Preview, with the `api-version` set to `preview`.
If you need a stable, GA version, and don't need the latest features, then you can use the older API. At time of writing, the latest GA API release is `2024-10-21`.

[Azure OpenAI in Azure AI Foundry Models API lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-lifecycle?tabs=key#api-evolution)

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
