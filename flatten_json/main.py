def _flatten_json_(y):
        out = {}
        def flatten(x, name=''):
            if type(x) is dict:
                if len(x):
                    for a in x:
                        flatten(x[a], name + a + '.')
                elif x == {}:
                    out[name[:-1]] = x
            elif type(x) is list:
                i = 0
                if len(x):
                    out[name[:-1]] = x
                elif(x==[]):
                    out[name[:-1]] = x
            else:
                out[name[:-1]] = x

        flatten(y)
        return out

def _unflatten_json_(dic):
        try:
            resultDict = dict()
            for key, value in dic.items():
                parts = key.split(".")
                d = resultDict
                for part in parts[:-1]:
                    if part not in d:
                        d[part] = dict()
                    d = d[part]
                d[parts[-1]] = value
            return json.dumps(resultDict)
        except Exception as e:
            logging.getLogger('EventLog').log(logging.INFO, "unflatten json error: %s" % (str(e.message)),
                                              extra=EventType.INDIVIDUAL_ASSET._dict)
        return dict()
dict_string = {'type': '1', 'data': {'key1': 'k', 'key2': 'k2'}}
flatten = _flatten_json_(dict_string)
unflatten = _unflatten_json_(flatten)
print "dict_string", dict_string,"","_flatten_json_",flatten," \n ","unflatten: ",unflatten
