from mcityoswrapper import McityOSIntersections
from pytest import fixture

@fixture
def intersection_keys():
        return ['id', 'instrument']

def test_intersection(intersection_keys):
        mcityos_instance = McityOSIntersections(1)
        response = mcityos_instance.get_intersection()

        assert isinstance(response, dict)
        assert response['intersection']['instrument'] == 'signal', "signal in response"
        assert set(intersection_keys).issubset(response['intersection'].keys()), "All keys should be in the response"

def test_intersections():
        response = McityOSIntersections.get_intersections()
        print(response)
        assert isinstance(response, dict)
        assert isinstance(response['intersections'], list)
