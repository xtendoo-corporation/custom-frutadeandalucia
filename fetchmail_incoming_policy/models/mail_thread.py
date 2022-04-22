# Copyright 2022 Xtendoo Software SLU (www.xtendoo.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import email
import email.policy
import xmlrpc.client as xmlrpclib

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.model
    def message_process(
        self,
        model,
        message,
        custom_values=None,
        save_original=False,
        strip_attachments=False,
        thread_id=None,
    ):
        message_copy = message
        if isinstance(message, xmlrpclib.Binary):
            message = bytes(message.data)

        if isinstance(message, str):
            message = message.encode("utf-8")
        message = email.message_from_bytes(message, policy=email.policy.SMTP)
        msg_dict = self.message_parse(message, save_original=save_original)
        message_id = msg_dict.get("message_id")
        message_from = msg_dict.get("message_from")
        message_to = msg_dict.get("message_to")

        print("#"*80)
        print("message_id", message_id)
        print("message_from", message_from)
        print("mesage_to", message_to)
        print("#"*80)

        if message_id:
            return super().message_process(
                model,
                message_copy,
                custom_values=custom_values,
                save_original=save_original,
                strip_attachments=strip_attachments,
                thread_id=thread_id,
            )
