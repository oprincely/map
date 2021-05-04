#!flask/bin/python
from app.api import bp
from flask import jsonify,request
from app.genum_private import generate_numbers_private

@bp.route('/relation/api/persons', methods=['GET'])
def get_persons():
    
    #Person 1
    FN,MN,LN,btd,btm,bty = 'Ogbenyi','','Martha',30,10,1998
    FN,MN,LN,btd,btm,bty = 'Igwebuike','','Sylvia',27,9,1996
    #Person 2
    FN1,MN1,LN1,btd1,btm1,bty1 = 'Ikpeamaeze','Chizurum','Anthony',15,3,1996
    '''
    #Person 1
    #FN,MN,LN,btd,btm,bty = 'Princely','Emeka','Okwuego',22,2,1982#'Uchechukwu','Emeka','Okwu',22,2,1982
    FN,MN,LN,btd,btm,bty = 'Uchechukwu','Emeka','Okwu',22,2,1982
    #Person 2
    FN1,MN1,LN1,btd1,btm1,bty1 = 'Ngozi','','Nwaosu',3,3,1982
    '''
    
    person1 = generate_numbers_private(FN,MN,LN,btd,btm,bty,year_in_past=2021)[4]

    person2 = generate_numbers_private(FN1,MN1,LN1,btd1,btm1,bty1,year_in_past=2021)[4]
    
    #mixed relationships.
    person1_list = (person1['Heart desire'],person1['Destiny'],person1['Talent'],person1['Maturity'],person1['Image number'])
    person2_list = (person2['Heart desire'],person2['Destiny'],person2['Talent'],person2['Maturity'],person2['Image number'])
    print('person1_list = ',person1_list)
    print('person2_list = ',person2_list)
    #The intersection
    def intersection(lst1, lst2): 
        return list(set(lst1) & set(lst2))
    
    #Analyze
    tool = ["""Rule1. True love is the attraction, brought forth from past lives. (Many numbers in common.)""",
            
            """Rule2. The marriage may be one of experience, with love to be earned through tests and trials,
                then ending in happy companionship and the joy of being together. (One or two numbers in common.)""",
            
            """Other marriages ending in divorce court have seemed to be wrong from the start;
            the reason for the attraction based only on a temporary position as a Pinnacle, Personal Year, or Table 
            of Events, all changing experiences."""]
    
    print(person1)
    print(person2)
    
    common_core_contact = {k: person1[k] for k in person1 if k in person2 and person1[k] == person2[k]}
    print('common_core_contact = ',common_core_contact)
    
    if person1['Heart desire'] ==  person2['Heart desire']:
        deduction = """A strong emotional tie. Love and interest can remain a lifetime through,
                    even though problems and separation come about for other reasons. The tie between two people with
                    the same Heart’s Desire is a spiritual one."""
    elif person1 == intersection:
        affinitive = """Second—compare each major position in the same way. Do they have the same numbers on all positions?
                        This is most unusual. This attraction would be similar to being affinities.
                        But far too often there is little real accomplishment when two people are so much alike."""
    elif person1['Destiny'] ==  person2['Destiny']:
        same_destiny = """the marriage may be comparatively happy, as they live on the same level of activity.
                        They may have grown up together in the same environment, or met through association on the same 
                        level of living. Many marriages, comparatively happy, come about in this way because of common
                        interests from birth; but there should be other points of attraction in common to bring
                        the lasting fire of romance."""
    elif person1['Talent'] ==  person2['Talent']:
        same_talent = """this may bring two people together in love and marriage through association at 
                        work or social interests connected with the work. This marriage can be generally
                        happy because of a mutual interest. This is usually built on the commonly accepted
                        traditions and standards of home and marriage. Now and then, this tie is strange 
                        and intense, with many problems of temperament brought over
                        from past incarnations. This attraction can lead to marriage but not to smooth waters."""
    elif person1['Maturity'] ==  person2['Maturity']:
        same_goal = """The tie between two people with the same Ultimate Goal is a pleasing one, but does not
                    always lead to marriage until later in life, unless there are other points of attraction in common."""
    elif person1['Image number'] ==  person2['Image number']:
        same_person = """Two people may be attracted to each other by the Personality.
                        This is not enough for a happy marriage."""
    #mixed relationships.
    mixed_relationships = intersection(person1_list, person2_list)
    print('mixed_relationships = ',mixed_relationships)
    #for k,v in person1.items():
    def get_key(my_dict, val):
        for key, value in my_dict.items():
            if val == value:
                return key
        return "key doesn't exist"
    
    for i in mixed_relationships:
        if get_key(common_core_contact, i) == "key doesn't exist":
            print(f'{FN} {get_key(person1, i)} is the {FN1} {get_key(person2, i)}')
    
    return 'DONE'#jsonify({'person1': person1,'person2': person2})
