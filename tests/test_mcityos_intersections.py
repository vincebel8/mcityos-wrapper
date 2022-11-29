from mcityoswrapper import McityOSIntersections
from pytest import fixture

@fixture
def intersection_keys():
        return ['id', 'instrument']


@vcr.use_cassette('tests/vcr_cassettes/get-intersections.yml')
def test_get_intersections():
        response = McityOSIntersections.get_intersections()

        assert isinstance(response, dict)
        assert isinstance(response['intersections'], list)


@vcr.use_cassette('tests/vcr_cassettes/get-intersection.yml')
def test_get_intersection(intersection_keys):
        response = McityOSIntersections.get_intersection(1)

        assert isinstance(response, dict)
        assert response['intersection']['instrument'] == 'signal', "signal in response"
        assert set(intersection_keys).issubset(response['intersection'].keys()), "All keys should be in the response"
