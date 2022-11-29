from mcityoswrapper import McityOS
from pytest import fixture

@fixture
def intersection_keys():
        return ['id', 'instrument']

def test_intersection():
        mcityos_instance = McityOS(1)
        response = mcityos_instance.intersection()

        assert isinstance(response, dict)
        assert response['intersection']['instrument'] == 'signal', "signal in response"
        assert set(intersection_keys()).issubset(response['intersection'].keys()), "All keys should be in the response"

def test_intersections():
        response = McityOS.intersections()
        print(response)
        assert isinstance(response, dict)
        assert isinstance(response['intersections'], list)
