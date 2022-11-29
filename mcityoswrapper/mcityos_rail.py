from . import session

prefix = 'https://octane.mvillage.um.city/api'

class McityOSRail(object):

        def __init__(self, id):
                self.id = id

        @staticmethod
        def railcrossings():
                path = prefix + '/railcrossings'
                response = session.get(path)
                print(response)
                print("Running...")
                return response.json()

        def railcrossing(self):
                path = 'https://octane.mvillage.um.city/api/railcrossing/{}'.format(self.id)
                response = session.get(path)
                return response.json()
