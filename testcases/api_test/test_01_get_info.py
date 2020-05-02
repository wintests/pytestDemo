import pytest
from operation.user import get_all_user_info, get_one_user_info


def test_get_all_user_info():
    result = get_all_user_info()
    # print(result.__dict__)
    assert result.success is True, result.error


def test_get_get_one_user_info():
    result = get_one_user_info("wintest3")
    # print(result.__dict__)
    assert result.success is True, result.error


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_info.py"])
