def fun():
    capital = {'odisha': 'Bhubaneswar','Telangana':'Hyderabad', 'Tamil Nadu':'Chennai'}
    print(capital['odisha'])
    print(capital)
    k = capital.keys()
    print(k)
    v = capital.values()
    print(v)
    l = capital.items()
    print(l)
    for key in capital.keys():
        print(key, capital[key])
    for key, val in capital.items():
        print(key, val)
    capital['Bihar'] = 'Patna'
    print(capital)
    capital.update({'Punjab':'Chandigarh'})
    print(capital)
    #print(capital.has_key('Rajasthan'))
    #print(capital['Rajasthan']) #generates error if not found
    print(capital.get("Rajasthan"))
#nested dictionary
    d1 = {'reshma':{'age':74,'course':'c language'}, 'sunikhya':{'age':9,'course':'python'}}
    print(d1['reshma']['age'])
#dictionary of lists
    d2 = {'fruits':['mango','apple','orange'],'flowers':['jasmine','lily','tulip']}
    print(d2['fruits'])
    print(d2['fruits'][2])
    #d3 = {['USA','JAPAN','CHINA']:'COUNTRIES', ['EUROPE','AFRICA','ASIA']:'CONTINENTS'}
    #print(d3)
    d3 = {('USA','JAPAN','CHINA'):'COUNTRIES', ('EUROPE','AFRICA','ASIA'):'CONTINENTS'}
    print(d3)
    print(d3['USA','JAPAN','CHINA'])
fun()