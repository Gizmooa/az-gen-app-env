import re
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import HttpResponseError
from exceptions import KeyVaultAccessError

SECRET_REF_PATTERN = re.compile(
    r"@Microsoft\.KeyVault\(VaultName=(.*?);SecretName=(.*?)\)"
)

def resolve_secrets(settings: dict) -> dict:
    resolved = {}
    credential = DefaultAzureCredential()

    for key, value in settings.items():
        match = SECRET_REF_PATTERN.match(value)
        if match:
            vault_name, secret_name = match.groups()
            vault_url = f"https://{vault_name}.vault.azure.net"
            client = SecretClient(vault_url=vault_url, credential=credential)

            try:
                resolved_value = client.get_secret(secret_name).value
                resolved[key] = resolved_value
            except HttpResponseError as e:
                raise KeyVaultAccessError(
                    f"Failed to retrieve secret '{secret_name}' from Key Vault '{vault_name}'.\n"
                    f"Details: {e.message}"
                )
        else:
            resolved[key] = value

    return resolved
