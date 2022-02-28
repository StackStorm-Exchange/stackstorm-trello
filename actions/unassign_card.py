from lib import action


class UnassignCardAction(action.BaseAction):
    def run(self, card_id, member_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        card = self._client().get_card(card_id)
        card.unassign(member_id)

        return card
