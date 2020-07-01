from Base.get_data import GetData

login_list = list()
data = GetData.get_yml_data('login.yml')  # type:dict
for i in data.values(): # type:dict
    login_list.append((i.get('user'), i.get('pwd'), i.get('toast'), i.get('exp')))

print(login_list)
