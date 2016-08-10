from jira import JIRA as jra
from utils import ConfigManager

class Jira(object):

	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.jra = jra(host, basic_auth=(user, password))

	@classmethod
	def get_jira_service(cls):
		config_details = ConfigManager.get_details();
		jira = Jira(config_details['host'], config_details['user'], config_details['password'])
		return jira

	def get_issue(self, issue_key):
		issue = self.jra.issue(issue_key)
		return issue

	def get_issue_for_user(self, user, project, resolved):
		user = self.user if user is None else user 
		jql = "assignee = %s" % user
		jql = jql + " and project = %s"%project if project else jql
		jql = jql + " and resolution = Unresolved" if resolved else jql
		return self.jra.search_issues(jql)

class IssueMapper(object):
	def __init__(self, issue):
		self.issue = issue

	def get_short_rep(self):

		return "[%s] - %s" % (self.issue.fields.issuetype, self.issue.fields.summary)

	def get_long_rep(self):

		return "[Type] - %s\n[Title] - %s\n[Assignee] - %s\t[Reporter] - %s\n[Description]\n%s" % (self.issue.fields.issuetype, self.issue.fields.summary.strip(), self.issue.fields.assignee, self.issue.fields.reporter, self.issue.fields.description.strip())