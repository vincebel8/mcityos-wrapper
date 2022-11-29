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

        def trigger_railcrossing(id):
                url = prefix + '/railcrossing/{}'.format(id)

                json_data = {
                    'state': {
                        'manualCall': True,
                        'manualCallTimeOverride': 10,
                    },
                }

                response = session.patch(url, json=json_data)
                return response.json()
