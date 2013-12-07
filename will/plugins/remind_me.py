import datetime
import requests
from will.plugin_base import WillPlugin
from will.decorators import respond_to, scheduled, one_time_task, hear, randomly, crontab, route, rendered_template
import will.settings as settings



class RemindMePlugin(WillPlugin):

    @respond_to("remind me to (?P<reminder_text>.*?) (at|on) (?P<remind_time>.*)")
    def remind_me_at(self, message, reminder_text=None, remind_time=None):
        now = datetime.datetime.now()
        parsed_time = self.parse_natural_time(remind_time)
        natural_datetime = self.to_natural_day_and_time(parsed_time)

        formatted_reminder_text = "@%(from_handle)s, you asked me to remind you %(reminder_text)s" % {
            "from_handle": message.sender.nick,
            "reminder_text": reminder_text,
        }
        self.schedule_say(message, formatted_reminder_text, parsed_time)
        self.say(message, "%(reminder_text)s %(natural_datetime)s. Got it." % locals())


    @respond_to("remind me to (?P<reminder_text>.*?) in (?P<time>.*)")
    def remind_me_in(self, message, reminder_text=None, time=None):
        self.say(message, "Remind you to %s in %s?" % (reminder_text, time))