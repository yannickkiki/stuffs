from django.db.models import Count

from core.xlib.tasks import CronTask

from foxx.queue.models import Queue
from foxx.xlib.loggers import logger


class FixDuplicateCampaignPendingEmailCron(CronTask):

    def _get_queue_pending_campaign_qs(self):
        return Queue.objects.filter(cancelled=None, sent=None)\
            .exclude(templet__campaign=None)

    def get_queryset(self, **kwargs):
        """
        :return: list of dict{templet, email, count}
        """
        return self._get_queue_pending_campaign_qs()\
            .values('templet', 'email')\
            .annotate(count=Count('*'))\
            .filter(count__gt=1)

    def process(self, *args, **kwargs):
        for record in self.get_queryset():
            logger.info(f"FixDuplicateCampaignPendingEmailCron: Delete duplicates for record: {record}")

            qs = self._get_queue_pending_campaign_qs().filter(templet=record['templet'], email=record['email'])
            first_item = qs.order_by('id').first()
            result = qs.filter(id__gt=first_item.id).delete()

            logger.info(f"FixDuplicateCampaignPendingEmailCron: Deletion result: {result}")

    def get_stats(self):
        return {
            'templet_email_duplicated': self.get_queryset().count(),
        }


# Sql query if we want to move faster
query = """
    WITH queue_pending_campaign as (
        SELECT foxx.queue.id, foxx.queue.templet_id, foxx.queue.email_id
          FROM foxx.queue
           INNER JOIN core.campaign ON foxx.queue.templet_id = core.campaign.templet_id
          WHERE foxx.queue.scheduled IS NULL
            AND foxx.queue.cancelled IS NULL
    )
    DELETE FROM foxx.queue WHERE id IN (
        SELECT id
        FROM (
            SELECT id, row_number() over (partition by (templet_id, email_id) order by id) AS duplicate_number
            FROM queue_pending_campaign
        ) q
        WHERE q.duplicate_number > 1
    )
"""
