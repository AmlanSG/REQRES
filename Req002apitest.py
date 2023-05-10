import jsonpath_ng
import requests
import json

from jsonpath_ng import jsonpath, parse


def ver_dict(res):
    print("Dictionary Object", res)

    res_str = json.dumps(res)
    print(type(res))
    json_data = json.loads(res_str)

    jsonpath_expr_str = "$.data.id"

    # Parse the JSONPath expression string and compile it into an expression object
    jsonpath_expr = jsonpath_ng.parse(jsonpath_expr_str)

    # Search the JSON document using the compiled JSONPath expression
    matches = jsonpath_expr.find(json_data)

    print(matches)
    for match in matches:
        assert isinstance(match.value, int)
        print("ID is :", match.value)


def ver_list(res):
    print("List Object", res)


# For Get
for i in range(1, 5):
    api_url = "https://reqres.in/api/users/" + str(i)
    response = requests.get(api_url)
    print(response)
    res_bod = response.json()
    if "dict" in str(type(res_bod)):
        ver_dict(res_bod)
    elif "list" in str(type(res_bod)):
        ver_list(res_bod)
    else:
        print("NOT A Valid Format")
