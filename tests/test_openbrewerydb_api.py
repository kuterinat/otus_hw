import pytest


SUCC_STATUS_CODE = 200
ERR_STATUS_CODE = 404
ERR_MSG = "Couldn't find Brewery"
DEF_PER_PAGE = 20
NUM_ALL = 50
BREWERY_IDS = ['10-56-brewing-company-knox',
               '10-barrel-brewing-co-bend-1',
               '10-barrel-brewing-co-bend-2',
               '10-barrel-brewing-co-bend-pub-bend',
               '10-barrel-brewing-co-boise-boise',
               '10-barrel-brewing-co-denver-denver',
               '10-barrel-brewing-co-portland',
               '10-barrel-brewing-co-san-diego',
               '10-torr-distilling-and-brewing-reno',
               '101-brewery-quilcene',
               '101-north-brewing-company-petaluma',
               '105-west-brewing-co-castle-rock',
               '10k-brewing-anoka',
               '10th-district-brewing-company-abington',
               '11-below-brewing-company-houston',
               '1188-brewing-co-john-day',
               '12-acres-brewing-company-killeshin',
               '12-gates-brewing-company-williamsville',
               '12-west-brewing-company-gilbert',
               '12-west-brewing-company-production-facility-mesa',
               '122-west-brewing-co-bellingham',
               '127-brewing-jackson',
               '12degree-brewing-louisville',
               '12welve-eyes-brewing-saint-paul',
               '13-below-brewery-cincinnati',
               '13-stripes-brewery-taylors',
               '13-virtues-brewing-co-portland',
               '1323-r-and-d-raleigh',
               '14-cannons-brewing-company-westlake-village',
               '14-lakes-brewery-crosslake',
               '14er-brewing-company-denver',
               '14th-star-brewing-saint-albans',
               '16-lots-brewing-mason',
               '16-mile-brewing-co-georgetown',
               '16-stone-brewpub-holland-patent',
               '1623-brewing-co-llc-westminister',
               '1717-brewing-co-des-moines',
               '1718-ocracoke-brewing-ocracoke',
               '1781-brewing-company-spotsylvania',
               '180-and-tapped-coraopolis',
               '1817-brewery-okolona',
               '1840-brewing-company-milwaukee',
               '1850-brewing-company-mariposa',
               '18th-street-brewery-gary',
               '18th-street-brewery-hammond',
               '1905-brewing-company-assumption',
               '1912-brewing-tucson',
               '192-brewing-kenmore',
               '1940s-brewing-company-holbrook',
               '1st-republic-brewing-co-essex-junction']
BREWERY_TYPES = ['contract', 'brewpub', 'large', 'micro', 'closed', 'proprieter', 'nano', 'bar', 'planning', 'regional']
BREWERY_CITIES = {'san_diego': 'San Diego', 'anoka': 'Anoka', 'knoxville': 'Knoxville'}


def test_get_list_breweries_default(brewery_api, all_breweries):
    resp = brewery_api.get('')
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    def_breweries = resp.json()
    assert len(def_breweries) == DEF_PER_PAGE, f"Wrong default number of breweries per page: {len(def_breweries)}"
    assert def_breweries == all_breweries[:DEF_PER_PAGE], "Wrong list of breweries per page"


@pytest.mark.parametrize("per_page", range(1, 51, 7))
def test_get_list_breweries_number_per_page(brewery_api, per_page, all_breweries):

    resp = brewery_api.get('', params={'per_page': per_page})
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    breweries_per_page = resp.json()
    assert len(breweries_per_page) == per_page, f"Wrong number of breweries per page: {len(breweries_per_page)}"
    assert breweries_per_page == all_breweries[:per_page], "Wrong list of breweries per page"


@pytest.mark.parametrize("brewery_id", BREWERY_IDS)
def test_get_brewery_by_id(brewery_api, brewery_id, all_breweries):

    resp = brewery_api.get(brewery_id)
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    brewery = resp.json()
    breweries_with_id = [br for br in all_breweries if br['id'] == brewery_id]
    assert len(breweries_with_id) == 1, f"Wrong number of breweries with id = {brewery_id}: {len(breweries_with_id)}"
    assert brewery == breweries_with_id[0], f"Wrong brewery data: {brewery}"


@pytest.mark.parametrize("brewery_id", [123, 'aassaa', None, True])
def test_get_brewery_incorrect_id(brewery_api, brewery_id, all_breweries):

    resp = brewery_api.get(brewery_id)
    assert resp.status_code == ERR_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    resp_j = resp.json()
    assert resp_j['message'] == ERR_MSG, f"Wrong response message: {resp_j['message']}"


@pytest.mark.parametrize("brewery_type", BREWERY_TYPES)
@pytest.mark.parametrize("brewery_city", BREWERY_CITIES.keys())
def test_get_breweries_by_type(brewery_api, brewery_type, brewery_city):
    resp = brewery_api.get('', params={'by_type': brewery_type, 'by_city': brewery_city})
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    breweries = resp.json()
    for brewery in breweries:
        assert brewery['brewery_type'] == brewery_type, f"Wrong brewery type: {brewery['brewery_type']}"
        assert brewery['city'] == BREWERY_CITIES[brewery_city], f"Wrong brewery city: {brewery['city']}"
