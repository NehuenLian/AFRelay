from src.shared.utils.response_management import build_error_response


def test_build_error_response():

    error_response = build_error_response("FakeMethod", "Error type fault", "detail")
    
    assert error_response["status"] == "error"

    assert error_response["error"]["method"] == "FakeMethod"
    assert error_response["error"]["error_type"] == "Error type fault"
    assert error_response["error"]["details"] == "detail"