from mcityoswrapper import McityOSRail
from pytest import fixture

@fixture
def rail_keys():
        return ['id', 'instrument']


@vcr.use_cassette('tests/vcr_cassettes/get-railcrossings.yml')
def test_get_railcrossings():
        response = McityOSRail.get_railcrossings()

        assert isinstance(response, dict)
        assert isinstance(response['railcrossings'], list)


@vcr.use_cassette('tests/vcr_cassettes/get-railcrossing.yml')
def test_get_railcrossing(rail_keys):
        response = McityOSRail.get_railcrossing(1)

        assert isinstance(response, dict)
        assert response['railcrossing']['instrument'] == 'gated', "gated in response"
        assert set(rail_keys).issubset(response['railcrossing'].keys()), "Keys should be in the response"


@vcr.use_cassette('tests/vcr_cassettes/trigger-railcrossing.yml')
def test_trigger_railcrossing():
        response = McityOSRail.trigger_railcrossing(1)

        assert isinstance(response, dict)
        assert isinstance(response['requestID'], str)
