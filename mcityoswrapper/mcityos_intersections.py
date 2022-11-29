from . import session

prefix = 'https://octane.mvillage.um.city/api'

class McityOSIntersections(object):

        @staticmethod
        def get_intersections():
                url = prefix + '/intersections'
                response = session.get(url)
                print(response)
                print("Running...")
                return response.json()

        def get_intersection(id):
                url = prefix + '/intersection/{}'.format(id)
                response = session.get(url)
                return response.json()
