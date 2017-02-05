import click
from utils import ConfigManager, EditorMode, ask_for_confirmation, prompt
from jira_service import Jira, IssueMapper
import editor

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

@cli.command()
@click.argument("issue_key")
def move(issue_key):
	"""Transition issues"""
	jra = Jira.get_jira_service();	# Check for exception and ask user to configure
	issue = jra.get_issue(issue_key)
	possible_transitions = jra.get_transitions(issue)
	print map(lambda x: printf(x['id']+" "+x['name']), possible_transitions)
	res = prompt("Please enter the id of transition: ", map(lambda x: x['id'], possible_transitions))
	print jra.transition_issue(issue, res)

@cli.command("ls")
@click.option("--project", "-p", help="Project name")
@click.option("--assignee", "-s", help ="Filter by assignee")
@click.option("--all", "-a", is_flag=True, help="Get all issues")
def list(project, assignee, all):
	"""Lists Issues"""
	jra = Jira.get_jira_service();
	issues = jra.get_issue_for_user(assignee, project, all) # shift list representation logic to IssueMapper
	issue_reps = map(lambda x:IssueMapper(x).get_short_rep(), issues)
	if len(issue_reps) == 0:
		printf("No issue found for you")
	map(printf, issue_reps)

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@cli.command("create")
@click.argument("project")
@click.argument("type")
@click.option("--summary", "-s", help="Summary")
@click.option("--desc", "-d" , help="Description", default = "")
@click.option("--edit_mode", "-e" , is_flag = True)
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to create the issue?')
def create(project, type,summary, desc, edit_mode):
	"""Creates issue under a project"""
	if edit_mode:
		interface =EditorMode('issue')
		interface.open()
		data = interface.parse()
		summary = data['summary']	
		desc = data['description']
		if not ask_for_confirmation('Are you sure you want to create issue(Y/N): '):
			print 'Operation Aborted'
			return None
	jra = Jira.get_jira_service();
	issue = jra.create_issue(project, summary, desc, type)
	print IssueMapper(issue).get_long_rep()

@cli.command("comment")
@click.argument("issue_key")
@click.argument("comment")
def comment(issue_key, comment):
	"""Creates issue under a project"""
	jra = Jira.get_jira_service();
	print jra.add_comment(issue_key, comment)


def printf(str):
	click.echo(str)
