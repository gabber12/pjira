import click
from utils import ConfigManager, InvalidConfiguration
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
@click.option("--project", "-p", help="Project name")
@click.option("--assignee", "-s", help ="Filter by assignee")
@click.option("--all", "-a", is_flag=True, help="Get all issues")
def list(project, assignee, all):
	"""Lists Unresolved Issues"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	issues = jra.get_issue_for_user(assignee, project, all) # shift list representation logic to IssueMapper
	issue_reps = map(lambda x:IssueMapper(x).get_short_rep(), issues)
	map(printf, issue_reps)

@cli.command("create")
@click.argument("project")
@click.option("--summary", "-s", help="Summary")
@click.option("--desc", "-d" , help="Description", default = "")
@click.option("--type", "-t", help="Issue Type - Bug, Story ..\nDefault = Story", default = "Story")
def create(project, summary, description, type):
	"""Creates issue under a project"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	issue = jra.create_issue(project, summary, description, type)
	print IssueMapper(issue).get_long_rep()

@cli.command("comment")
@click.argument("issue_key")
@click.option("--comment", "-c", help="Comment text", prompt=True)
def create(issue_key, comment):
	"""Creates issue under a project"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	print jra.add_comment(issue_key, comment)



def printf(str):
	print str

if __name__ == '__main__':
	try:
		cli()
	except InvalidConfiguration, e:
		print str(e)