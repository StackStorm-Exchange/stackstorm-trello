# Trello Integration Pack

Integration pack that provides support for Trello, an online Task Tracking tool

## Configuration

* `api_key` - User API Key
* `token` - User oAuth Token for R/W Access

Note: Each action in this pack also takes `api_key` and `token` as parameters.
If provided, actions will prefer the runtime credentials over the system provided
credentials.

### Obtaining Credentials
#### API Token

API Token can be retrieved from https://trello.com/app-key while logged into your
account.

#### oAuth Token

To obtain an oAuth token, refer to the documentation at https://trello.com/docs/gettingstarted/#getting-a-token-from-a-user

## Supported Actions
```
+---------------------------+--------+--------------------+------------------------------------------------------+
| ref                       | pack   | name               | description                                          |
+---------------------------+--------+--------------------+------------------------------------------------------+
| trello.add_board          | trello | add_board          | Create a new board                                   |
| trello.add_card           | trello | add_card           | Add a new card to a list                             |
| trello.add_list           | trello | add_list           | Add a new list to a board                            |
| trello.close_board        | trello | close_board        | Close a board                                        |
| trello.close_card         | trello | close_card         | Close a card                                         |
| trello.close_list         | trello | close_list         | Close a list belonging to a board                    |
| trello.find_board_by_name | trello | find_board_by_name | Lookup a board ID based on name. Returns one or more |
|                           |        |                    | IDs                                                  |
| trello.find_card_by_name  | trello | find_card_by_name  | Lookup a Card ID based on name. Returns one or more  |
|                           |        |                    | IDs                                                  |
| trello.find_list_by_name  | trello | find_list_by_name  | Lookup a list ID based on name. Returns one or more  |
|                           |        |                    | IDs                                                  |
| trello.move_card          | trello | move_card          | Move a card from one board/list to another           |
|                           |        |                    | board/list                                           |
| trello.view_boards        | trello | view_boards        | Return a dictionary of all boards and their IDs      |
| trello.view_cards         | trello | view_cards         | View all cards on a board                            |
| trello.view_lists         | trello | view_lists         | View all lists belonging to a board                  |
| trello.view_organizations | trello | view_organizations | List all organizations for user                      |
+---------------------------+--------+--------------------+------------------------------------------------------+
```

## Sensors
### TrelloListSensor
Listens for the new Actions in Trello List, which is specified via [config](config.yaml), and dispatches trigger for each new event occurred.

Optionally you can specify in config which actions to listen via `filter` parameter.
For list of available filters see [Trello API docs](https://trello.com/docs/api/list/index.html#get-1-lists-idlist-actions).

When receives new data, Sensor emits:
* trigger: `trello.new_action`
* returns data:
  * `payload.id` - Action ID (string)
  * `payload.data` - Main data returned, specific for action, depends on action type (object)
  * `payload.date` - When action occurred (string)
  * `payload.idMemberCreator` - User ID who initiated the action (string)
  * `payload.type` - Action type (ex: createCard) (string)
  * `payload.memberCreator` - Extended info about user who initiated action (object)


## Examples
> Note that every action has structurised output, meaning you can use returned results in action chains.

#### `trello.view_lists` of the board
```sh
# st2 run trello.view_lists board_id=c39TEFLt

id: 55e74fea9c993817796d3f89
status: succeeded
result:
{
    "stdout": "",
    "result": {
        "55e7456df81e21e9b4aea429": {
            "name": "test-list",
            "closed": false
        }
    },
    "stderr": "",
    "exit_code": 0
}
```

#### `trello.add_card` to the board list
```sh
# st2 run trello.add_card name='New Task' description='Refactor software' board_id=c39TEFLt list_id=55e7456df81e21e9b4aea429

id: 55e750599c993817796d3f8c
status: succeeded
result:
{
    "stdout": "",
    "result": "55e7505d97a7ad01d49d6eaa",
    "stderr": "",
    "exit_code": 0
}
```

#### `trello.view_cards` of the board list
```sh
# st2 run trello.view_cards board_id=c39TEFLt list_id=55e7456df81e21e9b4aea429

id: 55e750b19c993817796d3f8f
status: succeeded
result:
{
    "stdout": "",
    "result": {
        "55e7505d97a7ad01d49d6eaa": {
            "url": "https://trello.com/c/LCaJeIc6/5-new-task",
            "name": "New Task",
            "closed": false,
            "description": "Refactor software"
        }
    },
    "stderr": "",
    "exit_code": 0
}
```
