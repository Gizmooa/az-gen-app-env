class AzGenAppEnvError(Exception):
    """Base exception for az-gen-app-env errors."""
    pass

class AppServiceAccessError(AzGenAppEnvError):
    """Raised when application settings cannot be fetched due to authorization issues."""
    pass

class KeyVaultAccessError(AzGenAppEnvError):
    """Raised when a Key Vault secret cannot be retrieved."""
    pass
