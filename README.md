# python-jira
A simple Atlassian jira cli client written in python

## Build
Source is setuptools friendly, all you need is pip.

```sh
$ git clone https://github.com/gabber12/python-jira.git
$ cd python-jira
$ pip install --editable
$ pjira --help
```

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
$ jira create JIRA -s "Suitable summary text"\ 
				   -d "Suitable description text"\
				   -t "Bug"[Default - Story]

# Comment on an issue
$ jira comment JIRA-100 'Added jira comment'

# Transition issues to possible states.
$ jira move JIRA-100
101 On Hold
90 Start Development
Please enter the id of transition: 90
$ jira move JIRA-100
91 Send for code review
101 On Hold 
Please enter the id of transition: 101

```
