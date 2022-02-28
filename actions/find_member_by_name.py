from lib import action


class FindMemberByNameAction(action.BaseAction):
    def run(self, name, board_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        members = []
        board = self._client().get_board(board_id)
        for member in board.all_members():
            if member.username.decode() == name:
                members.append(member.id)

        if not members:
            return False

        return members
