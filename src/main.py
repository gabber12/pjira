import click
from utils import ConfigManager
from jira_service import Jira


@click.group()
def cli():
	"""Simple Jira Command Line Client"""
	pass

@cli.command()
@click.option("--host", prompt=True)
@click.option("--user", prompt=True)
@click.option("--password", prompt=True, hide_input=True,
              confirmation_prompt=True)
def configure(host, user, password):
	"""Configure client with HOST, USER, PASSWORD"""
	ConfigManager.save_details(host, user, password)

@cli.command()
@click.argument("issue_key")
def issue(issue_key):
	"""Gets issue by issue key"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	print jra.get_issue(issue_key)


@cli.command("ls")
def list():
	"""Lists Issues according to passed options"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	

if __name__ == '__main__':
    cli()