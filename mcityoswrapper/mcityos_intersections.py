from . import session

prefix = 'https://octane.mvillage.um.city/api'

class McityOSIntersections(object):

        def __init__(self, id):
                self.id = id

        @staticmethod
        def get_intersections():
                url = prefix + '/intersections'
                response = session.get(url)
                print(response)
                print("Running...")
                return response.json()

        def get_intersection(self):
                url = prefix + '/intersection/{}'.format(self.id)
                response = session.get(url)
                return response.json()
