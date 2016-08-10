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
$ jira ls # All issue for current user
$ jira ls -a gabber12 # Filter by assignee
$ jira ls -p apache    # Filter by project
$ jira ls -u # Get Only unresolved issues


$ jira issue JIRA-100 # View Issue details
$ jira issue JIRA-100 -f # View Full Issue details
```