# Changelog

# 1.1.0

* Added the `add_card_comment` action to add a comment to an existing card
* Added the `add_card_label` action to add a label to an existing card
* Added the `assign_card` action to assign a card to a member of the trello board
* Added the `find_label_by_name` action to find a label's id by name
* Added the `unassign_card` action to unassign a board member from a card
* Updated the existing find by name (`find_board_by_name`, `find_card_by_name`, and `find_list_by_name`) actions to correctly return the object's name as a string and not a byte to enable proper string comparison.

# 1.0.0

* Drop Python 2.7 support

# 0.4.5

- Python 3 fixups
- Add explicit support for Python 2 and 3

# 0.4.4

- Minor linting fixes

# 0.4.3

- Added ability to change a board in move_card action ([issue #6](https://github.com/StackStorm-Exchange/stackstorm-trello/issues/6))

# 0.4.2

- Minor linting

# 0.4.0

- Updated action `runner_type` from `run-python` to `python-script`

## v0.3.0

* Switched from `config.yaml` to `config.schema.yaml`

## v0.2.0

* Added `TrelloListSensor` which monitors Trello List(s) for new actions/changes

## v0.1.1

* Added optional `description` parameter to `trello.add_card` action
* Added basic examples how to use actions in README
* Updated requirements.txt to use pypy package instead of GitHub repo

## v0.1.0

* Initial release
