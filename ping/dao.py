from . import models

class PingDao():

    def create(self, data):
        ping = models.PingData(
            first_name = data.get('first_name'),
            last_name = data.get('last_name')
        )
        ping.save()

        return ping

    def list(self):
        pings = models.PingData.objects
        return pings

    def retrieve(self, item_id):
        ping = models.PingData.objects.get(pk=item_id)
        return ping

    def update(self, item_id, data):
        ping = self.retrieve(item_id)
        ping.first_name = data.get('first_name', ping.first_name)
        ping.last_name = data.get('last_name', ping.last_name)
        ping.save()

        return ping

    def delete(self, item_id):
        ping = self.retrieve(item_id)
        ping.delete()

        return ping
