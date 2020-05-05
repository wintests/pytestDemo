import pytest
from testcases.conftest import scenario_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return scenario_data.get(testcase_name)