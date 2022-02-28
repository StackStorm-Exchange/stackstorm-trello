from lib import action


class FindLabelByNameAction(action.BaseAction):
    def run(self, name, board_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        labels = []
        board = self._client().get_board(board_id)
        for label in board.get_labels('all'):
            if label.name.decode() == name:
                labels.append(label.id)

        if not labels:
            return False

        return labels
