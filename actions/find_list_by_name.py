from lib import action


class FindListByNameAction(action.BaseAction):
    def run(self, name, board_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        lists = []
        board = self._client().get_board(board_id)
        for lst in board.all_lists():
            if lst.name.decode() == name and not lst.closed:
                lists.append(lst.id)

        if not lists:
            return False

        return lists
