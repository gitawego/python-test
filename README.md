# python test

## virtualenv

A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

see [virtualenv guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for detail

```shell
# install virtualenv
pip install virtualenv

# initialize virtualenv
virtualenv your_project_name

# to begin use virtualenv
source your_project_name/Scripts/activate
```
