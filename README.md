# python-jira
A simple Atlassian jira cli client written in python


## QuickStart
Intial configuration include providing Jira details.

```sh
$ jira configure
HOST: jira.xyz.com
USER: gabber12
PASSWORD: ********
```

## Usage

```sh
# List Jira issues
$ jira ls # All issue unresolved for current user
$ jira ls -s gabber12 # Filter by assignee
$ jira ls -p apache    # Filter by project
$ jira ls -a # Get All issues issues

# View particular jira issue details
$ jira issue JIRA-100 # View Issue details
$ jira issue JIRA-100 -f # View Full Issue details

# Create a new Jira issue
$ jira create JIRA -s Suitable summary text\ 
				   -d Suitable description text\
				   -t issue type (defaults to Story)

# Comment on an issue
$ jira comment JIRA-100 -c 'Added jira comment'

```