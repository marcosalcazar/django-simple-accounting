"""Module containing data-transfer-objets. We want to encapsulate the creation
of the details of a JournalEntry, then, the .create() method for JournalEntry
receives a list of JournalEntryDetailDTO with the information for them.
"""


class JournalEntryDetailDTO(object):
    def __init__(self, account, amount_debit, amount_credit):
        """
        :param account: models.Account
        :param amount_debit: Decimal
        :param amount_credit: Decimal

        Remember: amount_debit OR amount_credit for each detail, not both.
        Else, an AccountancyException will be raised
        """
        self.account = account
        self.amount_debit = amount_debit
        self.amount_credit = amount_credit


