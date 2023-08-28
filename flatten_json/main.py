def _flatten_json_(self, y):
        out = {}
        def flatten(x, name=''):
            if type(x) is dict:
                #print "xb:", x ," size :", len(x)
                if len(x):
                    for a in x:
                        #print "x[a]:", x[a], " name ", name, " a ", a
                        flatten(x[a], name + a + '.')
                    #print "xs:", x
                elif x == {}:
                    #print "xs_0:", x, "name: ",name
                    out[name[:-1]] = x
            elif type(x) is list:
                #print "lb:", x
                i = 0
                #print "lb:", x, " size :", len(x)
                if len(x):
                    #print "ls_N0:", x, "name: ", name
                    #for a in x:
                    #    flatten(a, name + str(i) + '.')
                    #    i += 1
                    out[name[:-1]] = x
                elif(x==[]):
                    #print "ls_0:", x, "name: ", name
                    out[name[:-1]] = x
            else:
                #print "e:", x
                out[name[:-1]] = x

        flatten(y)
        return out

    def _unflatten_json_(self, dic):
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
