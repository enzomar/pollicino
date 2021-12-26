import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from croniter import croniter
from pytz import utc

from helpers import command


class Scheduler(object):
    def __init__(self, start, state, topic_pub, duration_seconds=None):
        self.config = dict()
        self.config['topic_pub'] = topic_pub
        self.config['start'] = None
        self.config['duration_seconds'] = duration_seconds
        self.config['state'] = state
        self.scheduler = BlockingScheduler(timezone=utc)
        if start:
            if croniter.is_valid(start):
                self.config['start'] = start
        self.name = 'scheduler'

    def run(self):
        logging.info("Scheduler")
        cron_trigger = CronTrigger.from_crontab(self.config['start'], 'UTC')
        print(cron_trigger)
        if self.config['duration_seconds']:
            self.scheduler.add_job(
                func=command.square,
                trigger=cron_trigger,
                args=[self.config['state'], self.config['duration_seconds']])
        else:
            self.scheduler.add_job(
                func=command.switch,
                trigger=cron_trigger,
                args=[self.config['state']])
        self.scheduler.print_jobs()
        self.scheduler.start()


if __name__ == "__main__":
    s = Scheduler("0 0 * * *", "0 10 * * *", "topic_pub")
    croniter.is_valid("0 0 * * *")
    s.run()
