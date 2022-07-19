# Dodos: todo list CLI 
We have 10 Software Engineers in the company and although they can usually build very sophisticated software, they always forget things. We have tries to tech them JIRA, but they refuse to use any tool that does not have command line interface (CLI). After some back-and-forth we have agreed to invest time in developing and in-house CLI tool to store todo items.

We have discussed a set of functional requirements (how the program shall work) and built a mini-specification below. We have asked these Software Engineers to build the tool for themselves, but they repeatedly forgot it, since they done have a system to record this todo item! To break this vicious cycle we ask you to build the tool - you are the last hope to save the productivity of this company!

### Code Quality Requirements

We plan to hand over the tool to developers once they are able to use. They tend to be very picky about code quality, so there are several things we need to make sure are done on the project:

- Code must be formatted with black.
- Code must have tests for all commands and validation logic.
- Code must be stored in git repository, all changed are done via pull requests.
- Functions must have type annotations and code must pass mypy check.

We have set the automated checkers in this repository. Just run following commands (or setup your IDE to do it) 
before pushing your changes. Otherwise, you won't be able to merge your PR.
```
mypy .
black .
pytest tests
``` 

## Command Line Interface Specification

This section contains description of the command line interface the developers expect. Please feel free to ask questions or propose updates!

### List

* `python -m dodos list --today`
* `python -m dodos list --week`
* `python -m dodos list --month`
* `python -m dodos list --range 05.04.2022-15.04.2022`

| ID | Description | Due Date | Complete |
| --- | --- | --- | --- |
| 1 | Buy groceries | 03.03.2022 | True |
| 2 | Prepare present for Sean | 05.04.2022 | False |

### Create

* `python -m dodos create --description=“Buy a new toy for the cat.” --due=02.04.2022`

### Complete
* `python -m dodos complete 2`
* `python -m dodos uncomplete 2`

2 in these examples is an ID of an item.

### Update

* `python -m dodos update 2 --description=“New description goes here”`
* `python -m dodos update 2 --due=06.06.2022`
* `python -m dodos update 2 --description=“New description goes here” --due=06.06.2022`
* `python -m dodos update 2 --description=“New description goes here” --due=06.06.2022`

### Search

* `python -m dodos search “present”`

Output of search command is the same as for list, all items with the word `present` shall be returned.

### Generate

`python -m dodos generate 100`

Generates 100 random todos for fun and testing.

### Errors

All unexpected arguments to the command shall result in clear human-readable errors.

## Milestones

In large projects it is important to understand what how to split it into small deliverables that build on top of each other. It may be tricky to do, so we came up with initial proposal below.

We know that no plan survives contact with reality, but as a wise man said “Plans Are Useless, but Planning Is Essential"! We hope that the initial plan will help to work on the project in managable chunks. 

### M1: Environment Setup [DONE]

- Create git repository on Github
- Add .gitignore
- Install black and make sure it runs on save
- Install mypy and make sure you know how to run it
- Create/update [README.md](http://README.md) and document how to run black/mypy on the codebase.

### M2: Project Scaffolding

- `list` command works and returns dummy data in required format
- Inputs are validated on the `list` command.
- Tests exist to cover command argument validation logic.

### M3: Basic persistence

- `create` command works, `list` commands return `create`d items.
- Tests exist to cover `create` logic and argument validation.

### M4: Generating dummy data

- `generate` command works.

### M5: Complete commands

- `update`/`complete`/`search` commands work.
- Tests exist to cover `update`/`complete`/`search` logic and argument validation.

### M6: Introducing a change (simulate real world scenario)

- Add `Assignee` field and add it to the `create`/`update`/`search/generate` commands.
