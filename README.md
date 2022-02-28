# Trello Integration Pack

Integration pack that provides support for Trello, an online Task Tracking tool

## Configuration

Copy the example configuration in [trello.yaml.example](./trello.yaml.example)
to `/opt/stackstorm/configs/trello.yaml` and edit as required.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

### Action Configuration

For actions, the configuration should contain:

* `api_key` - User API Key
* `token` - User oAuth Token for R/W Access

Note: Each action in this pack also takes `api_key` and `token` as parameters.
If provided, actions will prefer the runtime credentials over the system provided
credentials.

### Sensor Configuration

Parameters in `list_actions_sensor` for every trello list:

* `list_id` - Trello List ID we monitor for new actions (required)
* `board_id` - Board ID where Trello List is located (required)
* `api_key` - Trello API key (optional)
* `token` - Trello API token (optional)
* `filter` - Filter actions by type(s) (eg. createCard, deleteCard) (optional)

For the full list of available filters, see
[Trello API docs](https://trello.com/docs/api/list/index.html#get-1-lists-idlist-actions).

API credentials work at any level with lower priority for top-level config credentials:
`list config` > `lists config` > `global config`.

It means that every Trello list can have its own unique credentials to work with different accounts.

See the example [configuration](trello.yaml.example) for more examples:

```yaml
---
  api_key: ""
  token: ""

  list_actions_sensor:
    #api_key: ""
    #token: ""
    lists:
    - list_id: 55e7456df81e21e9b4aea429
      board_id: c39TEFLt
      #api_key: ""
      #token: ""

    - list_id: 55f95fc7f6352543770088be
      board_id: c39TEFLt
      filter:
        - updateCard
        - deleteCard
```

Keep in mind, that a Sensor with invalid config (bad credentials) will die after 3 connection retries.

### Obtaining Credentials
#### API Token

API Token can be retrieved from https://trello.com/app-key while logged into your
account.

#### oAuth Token

To obtain an oAuth token, refer to the documentation at
https://trello.com/docs/gettingstarted/#getting-a-token-from-a-user

## Supported Actions

 name                  | description                                               
---------------------- | ----------------------------------------------------------
 `add_board`          | Create a new board                                        
 `add_card`           | Add a new card to a list
 `add_card_comment`   | Add a comment to a card                                   
 `add_list`           | Add a new list to a board                                 
 `close_board`        | Close a board                                             
 `close_card`         | Close a card                                              
 `close_list`         | Close a list belonging to a board                         
 `find_board_by_name` | Lookup a board ID based on name. Returns one or more IDs  
 `find_card_by_name`  | Lookup a card ID based on name. Returns one or more IDs   
 `find_list_by_name`  | Lookup a list ID based on name. Returns one or more IDs
 `find_member_by_name`  | Lookup a member ID based on name. Returns one or more IDs   
 `move_card`          | Move a card from one board/list to another board/list     
 `view_boards`        | Return a dictionary of all boards and their IDs           
 `view_cards`         | View all cards on a board                                 
 `view_lists`         | View all lists belonging to a board                       
 `view_organizations` | List all organizations for user                           

## Sensors

### TrelloListSensor

Listens for the new Actions (changes) in Trello List(s) and dispatches trigger for each new event occurred.

#### Output

When `TrelloListSensor` receives new data, it emits:
* trigger: `trello.new_action`
* and returns data:
  * `trigger.id` - Action ID (string)
  * `trigger.data` - Main data returned, specific for action, depends on action type (object)
  * `trigger.date` - When action occurred (string)
  * `trigger.idMemberCreator` - User ID who initiated the action (string)
  * `trigger.type` - Action type (ex: createCard) (string)
  * `trigger.memberCreator` - Extended info about user who initiated action (object)

Example:
```json
{
    "id": "4efe3147c72846af4e00006d",
    "data": {
        "list": {
            "id": "4eea4ffc91e31d174600004a",
            "name": "To Do Later"
        },
        "board": {
            "id": "4eea4ffc91e31d1746000046",
            "name": "Example Board"
        },
        "old": {
            "name": "To Do Eventually"
        }
    },
    "date": "2011-12-30T21:46:47.843Z",
    "idMemberCreator": "4ee7deffe582acdec80000ac",
    "type": "updateList",
    "memberCreator": {
        "id": "4ee7deffe582acdec80000ac",
        "avatarHash": null,
        "fullName": "Joe Tester",
        "initials": "JT",
        "username": "joetester"
    }
}
```

## Examples

> Note that every action has structured output, meaning you can use returned results in action chains.

### `trello.view_lists` of the board

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

### `trello.add_card` to the board list

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

### `trello.view_cards` of the board list

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
