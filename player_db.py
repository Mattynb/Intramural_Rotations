import random

# pg means can playmake, sg means can shoot/score, sf means can defend guards, pf means can defend bigs, c means can rebound/play inside 
# stats = [points, assists, rebounds]


players = {
    'Jefin' : {'available': True, 'minplayed': 0, 'plays' : [True, True, False, False, False] },
    'Dylan': {'available': True, 'minplayed': 0, 'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] },
    'Tyler' : {'available': True, 'minplayed': 0, 'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] },    
    'Liam' : {'available': True, 'minplayed': 0, 'plays' :  [True, False, True, True, False] },
    'Tenzin ' : {'available': True, 'minplayed': 0, 'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] },
    
    'Justin' : {'available': True, 'minplayed': 0,'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] },
    'Bruce' : {'available': True, 'minplayed': 0, 'plays' : [False, True, False, False, False] },
    'Matheus' : {'available': True, 'minplayed': 0, 'plays' : [False, False, True, True, True] },
    'Yoakin' : {'available': True, 'minplayed': 0, 'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] },
    'Brian': { 'available': True, 'minplayed': 0, 'plays' :  [False, False, False, True, True] },
    
    'Micheal': { 'available': True, 'minplayed': 0, 'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] },
    'Justin Y' : {'available': True, 'minplayed': 0, 'plays' : [bool(random.getrandbits(1)) for x in range(0, 5)] }
}
