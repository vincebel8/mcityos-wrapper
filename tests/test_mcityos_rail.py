from mcityoswrapper import McityOSRail
from pytest import fixture

@fixture
def rail_keys():
        return ['id', 'instrument']

def test_railcrossing(rail_keys):
        mcityos_instance = McityOSRail(1)
        response = mcityos_instance.get_railcrossing()

        assert isinstance(response, dict)
        assert response['railcrossing']['instrument'] == 'gated', "gated in response"
        assert set(rail_keys).issubset(response['railcrossing'].keys()), "Keys should be in the response"

def test_railcrossings():
        response = McityOSRail.get_railcrossings()
        print(response)
        assert isinstance(response, dict)
        assert isinstance(response['railcrossings'], list)
