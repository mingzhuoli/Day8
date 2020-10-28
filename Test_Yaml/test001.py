import yaml

with open("./data.yml", "r") as f:
    data = yaml.load(f)
    # print(type(data))
    # print(data)
    # print(data.get("animal"))
    # print(data["animal"])

    # print(type(data.get("YML_Data").get("da2")))
    # print(data.get("YML_Data").get("da2"))
    # print(data)
    # for i in data.get("Test").keys():

    Test_data = data.get("Test")
    for i in Test_data.keys():
        print("test: %s \n test_name: %s \n test_pwd: %s \n" %
              (i, Test_data.get(i).get("name"), Test_data.get(i).get("pwd")))

# test: login_data01
# test_name: lili
# test_pwd: 456