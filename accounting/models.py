# -*- coding: utf-8 -*-
from decimal import Decimal

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel

from accounting.exceptions import AccountingException


class AccountManager(TreeManager):
    @staticmethod
    def get_base_account(account_type):
        types = [at[0] for at in Account.ACCOUNT_TYPES]
        if account_type not in types:
            raise AccountingException(_('Invalid account type'))
        return Account.objects.get(code=account_type)


class Account(TimeStampedModel, MPTTModel):
    ASSET = 1
    LIABILITY = 2
    EQUITY = 3
    REVENUE = 4
    EXPENSE = 5

    ASSET_LABEL = _('Asset')
    LIABILITY_LABEL = _('Liability')
    EQUITY_LABEL = _('Equity')
    REVENUE_LABEL = _('Revenue')
    EXPENSE_LABEL = _('Expense')

    ACCOUNT_TYPES = (
        (ASSET, ASSET_LABEL),
        (LIABILITY, LIABILITY_LABEL),
        (EQUITY, EQUITY_LABEL),
        (REVENUE, REVENUE_LABEL),
        (EXPENSE, EXPENSE_LABEL),
    )
    INCOME_STATEMENT_ACCOUNTS = (
        (REVENUE, REVENUE_LABEL),
        (EXPENSE, EXPENSE_LABEL),
    )
    EQUITY_TYPES = (
        (ASSET, ASSET_LABEL),
        (LIABILITY, LIABILITY_LABEL),
    )
    BALANCE_SHEET_ACCOUNTS = (
        (ASSET, ASSET_LABEL),
        (LIABILITY, LIABILITY_LABEL),
        (EQUITY, EQUITY_LABEL),
    )

    code = models.CharField(max_length=255, verbose_name=_('Code'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children',
                            verbose_name=_('Parent'))
    mandatory = models.BooleanField(default=False,
                                    verbose_name=_('Is Mandatory'))

    objects = AccountManager()

    class MPTTMeta:
        order_insertion_by = ['code']

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)


class JournalEntryManager(models.Manager):
    def create(self, description, generator, details, **kwargs):
        """Entry point for creating a new JournalEntry.

        :param description: str
        :param generator: object
        :param details: list of DetailDTO
        """

        if len(details) <= 1:
            raise AccountingException(
                _("Amount of details should be 2 or more"))

        if sum([d.amount_credit - d.amount_debit for d in details]) != 0:
            raise AccountingException(
                _("Sum of debits and credits has to be the same"))

        for d in details:
            if (d.amount_credit == Decimal(0) and d.amount_debit == Decimal(0)) or (
                    d.amount_credit != Decimal(0) and d.amount_debit != Decimal(0)):
                raise AccountingException(
                    _("For each detail, at least one amount has to be different than 0, but not both"))

        kwargs.update(description=description,
                      generator=generator)
        je = super(JournalEntryManager, self).create(**kwargs)

        for d in details:
            _JournalEntryDetail.objects.create(entry=je,
                                               account=d.account,
                                               amount_debit=d.amount_debit,
                                               amount_credit=d.amount_credit)
        return je


class JournalEntry(TimeStampedModel):
    CREATION = (
        ('M', _('Manual')),
        ('A', _('Automatic'))
    )
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name=_('Date'))
    description = models.CharField(max_length=255, null=True, blank=True,
                                   verbose_name=_('Description'))
    generator_content_type = models.ForeignKey(ContentType,
                                               null=True)
    generator_object_id = models.PositiveIntegerField(null=True)
    generator = GenericForeignKey('generator_content_type',
                                  'generator_object_id')
    creation = models.CharField(max_length=1, verbose_name=_('Creation'))

    objects = JournalEntryManager()


class JournalEntryOpenStatement(JournalEntry):
    account = models.OneToOneField(Account, related_name='open_statement',
                                   verbose_name=_('Account'))

    objects = JournalEntryManager()


class _JournalEntryDetail(TimeStampedModel):
    entry = models.ForeignKey(JournalEntry, verbose_name=_('Entry'))
    account = models.ForeignKey(Account, verbose_name=_('Account'))
    amount_debit = models.DecimalField(max_digits=30, decimal_places=2,
                                       default=Decimal(0),
                                       verbose_name=_('Debit'),
                                       validators=[
                                           MinValueValidator(Decimal('0.00'))])
    amount_credit = models.DecimalField(max_digits=30, decimal_places=2,
                                        default=Decimal(0),
                                        verbose_name=_('Credit'),
                                        validators=[
                                            MinValueValidator(Decimal('0.00'))])
