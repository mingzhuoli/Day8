import yaml

with open("./w_data0.yml", "r") as f:
    w_data = yaml.load(f)
    print(w_data)
