import click
from utils import ConfigManager
from jira_service import Jira, IssueMapper


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
@click.option("--full", "-f", is_flag=True)
def issue(issue_key, full):
	"""Gets issue by issue key"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	mapper = IssueMapper(jra.get_issue(issue_key))
	rep = mapper.get_long_rep() if full else mapper.get_short_rep()
	print rep


@cli.command("ls")
@click.option("--project", "-p")
@click.option("--assignee", "-a")
@click.option("--unresolved", "-r", is_flag=True)
def list(project, assignee, unresolved):
	"""Lists Issues according to passed options"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	issues = jra.get_issue_for_user(assignee, project, unresolved) # shift list representation logic to IssueMapper
	issue_reps = map(lambda x:IssueMapper(x).get_short_rep(), issues)
	map(printf, issue_reps)

def printf(str):
	print str
if __name__ == '__main__':
    cli()