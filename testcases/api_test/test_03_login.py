import pytest
from operation.user import login_user

@pytest.mark.parametrize("")
def test_login_user():
    result = login_user("wintest", "123456")
    # print(result.__dict__)
    assert result.success is True, result.error


if __name__ == '__main__':
    pytest.main(["-q", "-v", "test_03_login.py"])
