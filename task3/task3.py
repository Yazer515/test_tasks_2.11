import json

values = []


def inside_json(_json):
    for value in values:
        if _json['id'] == value['id']:
            _json['value'] = value['value']

    # print(_json['title'])
    # if 'value' in _json:
    # print(_json['value'])
    if 'values' in _json:
        #	print(_json['values'])
        # print(type(_json['id']))
        for value in _json['values']:
            #	print(value)
            inside_json(value)
    else:
        return


with open('values.json') as values_file:
    values_json = json.load(values_file)
    # print(values_json)
    for value in values_json['values']:
        values.append(value)

    # print(values)

with open('tests.json') as json_file:
    json_data = json.load(json_file)
    for json_elem in json_data['tests']:
        inside_json(json_elem)
# 		while 1:
#		inside_data = json
#    		print(json['values'])
#    		for inside in json:
#    			print(inside_data['id'])

with open("report.json", "w") as report_file:
    json.dump(json_data, report_file)