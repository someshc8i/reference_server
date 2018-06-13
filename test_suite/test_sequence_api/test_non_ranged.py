# import pytest
# from requests import get

#
#
# @pytest.mark.parametrize("id_input, output", [
#     ('some111garbage1111id', 404),
#     ('', 404),
# ])
# def test_invalid_IDs(server, id_input, output):
#     api = '/sequence/'
#     assert get(server + api + id_input).status_code == output
#
#
# @pytest.mark.parametrize("input, output", [
#     (['some111garbage1111id', {"Accept": "text/plain"}], 404),
#     (['some111garbage1111id', {"Accept": "text/embl"}], 404),
# ])
# def test_invalid_id_invalid_header(server, input, output):
#     api = '/sequence/'
#     assert get(server + api + input[0], headers=input[1]).status_code == output
