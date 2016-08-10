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
		return issue.fields.summary