from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.core.exceptions import HttpResponseError
from exceptions import AppServiceAccessError

def fetch_app_settings(app_name: str, resource_group: str, subscription_id: str) -> dict:
    credential = DefaultAzureCredential()
    client = WebSiteManagementClient(credential, subscription_id)
    try:
        settings = client.web_apps.list_application_settings(resource_group, app_name)
        return settings.properties
    except HttpResponseError as e:
        raise AppServiceAccessError(
            f"Failed to fetch settings for '{app_name}' in resource group '{resource_group}'.\n"
            f"Details: {e.message}"
        )
