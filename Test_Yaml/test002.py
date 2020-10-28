import yaml

# data = {"login_data01": {"name": "lili", "pwd": 456, "se": "男"},
#         "sex": {"se": "男"}}

# datax = {"Search_Data": {
#         "search_test_002": {"except": {"value": "你好"}, "value": "你好"},
#         "search_test_001": {"except": [4, 5, 6], "value": 456}}}

# data = {"login_data01": {"name": "lili", "pwd": 456, "se": "男"},"sex": {"se": "男"}}
data = {"data": {"login_data01": {"name": "lili", "pwd": 456, "se": "男"},"sex": {"se": "男"}}}
datax = {"Search_Data": {"search_test_002": {"except": {"value": "你好"}, "value": "你好"}}}

with open("./w_data2.yml", "w") as f:
    w_data = yaml.dump(datax, f, encoding="utf-8", allow_unicode=True)
