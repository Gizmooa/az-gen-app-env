# 💻 Pull Down Azure App Settings & Run It Locally

When you want to run or debug your Azure Web App locally, you need an `appsettings.json` file with all your settings — including secrets like connection strings and API keys. But those secrets usually live in Azure Key Vault, and your app settings only hold references to them.

Copy-pasting secrets manually every time is a huge pain, especially if you have a bunch of apps or environments. So, I made **az-gen-app-env** — a handy CLI that grabs your Azure App Service settings, fetches the real secrets from Key Vault, and spits out a ready-to-go `appsettings.json` file for your local setup.

No more copying, no more guessing — just quick and easy local dev!

## 🚀 Features

- Fetches app settings from Azure App Service
- Resolves secrets from Azure Key Vault
- Generates a clean `appsettings.json` file

## 🛠️ Installation

You’ll need **Python 3.13+**, **UV**, and the **Azure CLI** installed.

Start by cloning down the repo and jump into the repository

```bash
git clone https://github.com/Gizmooa/az-gen-app-env.git
cd az-gen-app-env
```

Then lets create the virtual environment using uv

```bash
uv sync
```

Now lets make sure you can run the command globally

```bash
uv tool install . -e
```

Lastly, make sure you are logged into Azure

```bash
az login
```

## ⚡️ Usage

Once you're set up, navigate to the project where you want to generate the `appsettings.json` and run:

```bash
az-gen-app-env <app_name> <resource_group> <subscription_id>
```

This will create an `appsettings.json` that can be used for your C#/.NET application.

## 🤔 Limitations

It could make sense to add support for other languages and frameworks in future iterations—like Python, PHP, Java, and Node.js. This can be done easily by adding more output methods and letting the user choose which one to generate.
