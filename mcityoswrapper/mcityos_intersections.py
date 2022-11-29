from . import session

prefix = 'https://octane.mvillage.um.city/api'

class McityOSIntersections(object):

        def __init__(self, id):
                self.id = id

        @staticmethod
        def intersections():
                path = prefix + '/intersections'
                response = session.get(path)
                print(response)
                print("Running...")
                return response.json()

        def intersection(self):
                path = 'https://octane.mvillage.um.city/api/intersection/{}'.format(self.id)
                response = session.get(path)
                return response.json()
