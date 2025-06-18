import click

from fetcher import fetch_app_settings
from resolver import resolve_secrets
from parser import build_nested_dict
from exceptions import AppServiceAccessError, KeyVaultAccessError
from output import write_appsettings_json

@click.group(help="🚀 Generate appsettings.json from Azure App Service environment variables and Key Vault secrets.")
def cli():
    pass

@cli.command()
@click.argument("app_name")
@click.argument("resource_group")
@click.argument("subscription_id")
@click.option("--output", "-o", default="appsettings.json", help="📄 Output file path")
def generate(app_name, resource_group, subscription_id, output):
    """
    Fetch app settings from Azure, resolve Key Vault secrets, and generate appsettings.json file.
    """
    try:
        click.echo(f"🔍 Fetching app settings for '{app_name}'...")
        flat_settings = fetch_app_settings(app_name, resource_group, subscription_id)

        click.echo("🔐 Resolving Key Vault secrets...")
        resolved = resolve_secrets(flat_settings)

        click.echo("🧩 Parsing settings into nested structure...")
        nested = build_nested_dict(resolved)

        click.echo(f"💾 Writing appsettings.json to '{output}'...")
        write_appsettings_json(nested, output)

        click.secho("✅ Done!", fg="green")

    except AppServiceAccessError as e:
        click.secho(f"🚫 [App Service Error] {e}", fg="red")
        raise SystemExit(2)
    except KeyVaultAccessError as e:
        click.secho(f"🚫 [Key Vault Error] {e}", fg="red")
        raise SystemExit(3)
    except Exception as e:
        click.secho(f"💥 [Unexpected Error] {e}", fg="red")
        raise SystemExit(99)

if __name__ == "__main__":
    cli()
