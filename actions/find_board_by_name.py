from lib import action


class FindBoardByNameAction(action.BaseAction):
    def run(self, name, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        boards = []
        for board in self._client().list_boards():
            if board.name.decode() == name and not board.closed:
                boards.append(board.id)

        if not boards:
            return False

        return boards
