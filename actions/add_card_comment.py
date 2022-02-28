from lib import action


class AddCardCommentAction(action.BaseAction):
    def run(self, card_id, comment, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        card = self._client().get_card(card_id)
        card.comment(comment)

        return card
