from . import session

prefix = 'https://octane.mvillage.um.city/api'

class McityOSRail(object):

        @staticmethod
        def get_railcrossings():
                url = prefix + '/railcrossings'
                response = session.get(url)
                print(response)
                print("Running...")
                return response.json()

        def get_railcrossing(id):
                url = prefix + '/railcrossing/{}'.format(id)
                response = session.get(url)
                return response.json()

        def trigger_railcrossing(self):
                url = prefix + '/railcrossing/{}'.format(self.id)
                body = "{ 'state': { 'manualCall': true, 'manualCallTimeOverride': 10 } }"
                response = session.patch(url, body)
                return response.json()
