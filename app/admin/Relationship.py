from app.genum_private import generate_numbers_private
from app.Love import (same_heart_desire,go_getters,carry_outers,easy_takers,lover_affairs,extroverts,introverts)

def relationships(FN,MN,LN,btd,btm,bty,FN1,MN1,LN1,btd1,btm1,bty1,year_in_past):
    person1 = generate_numbers_private(FN,MN,LN,btd,btm,bty,year_in_past)[4]
    person2 = generate_numbers_private(FN1,MN1,LN1,btd1,btm1,bty1,year_in_past)[4]
    
    #mixed relationships.
    person1_list = (person1['Heart desire'],person1['Destiny'],person1['Talent'],person1['Goal'],
                    person1['Personality'],person1['physical'],person1['mental'],person1['emotion'],
                    person1['intuitive'],person1['security'],person1['point of intense'])
    #'n1':one,'n2':two,'n3':thr,'n4':fou,'n5':fiv,'n6':six,'n7':sev,'n8':eig,'n9':nin,'security':ps
    person2_list = (person2['Heart desire'],person2['Destiny'],person2['Talent'],person2['Goal'],
                    person2['Personality'],person2['physical'],person2['mental'],person2['emotion'],
                    person2['intuitive'],person2['security'],person2['point of intense'])

    #print('person1_list = ',person1_list)
    #print('person2_list = ',person2_list)

    #The intersection
    def intersection(lst1, lst2): 
        return list(set(lst1) & set(lst2))

    #Analyze
    #same_heart_desire,go_getters,carry-outers,easy-takers,lover_affairs,extroverts,introverts
    def where_is_the_heart(*list_to_compare,heart_desire,person):
        conclude = [person]
        for i in list_to_compare:
            if heart_desire in i:
                conclude.append(i[-1])
        return conclude

    rule1 = """Rule1. True love is the attraction, brought forth from past lives. (Many numbers in common.)"""
            
    rule2 = """Rule2. The marriage may be one of experience, with love to be earned through tests and trials,
                then ending in happy companionship and the joy of being together. (One or two numbers in common.)"""
            
    rule3 = """Rule3. Other marriages ending in divorce court have seemed to be wrong from the start;
            the reason for the attraction based only on a temporary position as a Pinnacle, Personal Year, or Table 
            of Events, all changing experiences."""

    common_core_contact = {k: person1[k] for k in person1 if k in person2 and person1[k] == person2[k]}

    #where_is_the_heart(*list_to_compare,heart_desire)
    w_i_t_h1 = where_is_the_heart(introverts[0],extroverts[0],go_getters[0],carry_outers[0],easy_takers[0],
                                 heart_desire=person1['Heart desire'],person=FN)
    w_i_t_h2 = where_is_the_heart(introverts[0],extroverts[0],go_getters[0],carry_outers[0],easy_takers[0],
                                 heart_desire=person2['Heart desire'],person=FN1)

    if person1['Heart desire'] ==  person2['Heart desire']:
        deduction = """Same Heart: A strong emotional tie. Love and interest can remain a lifetime through,
                    even though problems and separation come about for other reasons. The tie between two people with
                    the same Heart’s Desire is a spiritual one."""
    else:
        deduction = 'No same Heart Desire'
        
    if person1 == 'common_core_contact':
        affinitive = """Second—compare each major position in the same way. Do they have the same numbers on all positions?
                        This is most unusual. This attraction would be similar to being affinities.
                        But far too often there is little real accomplishment when two people are so much alike."""
    else:
        affinitive = 'No same affinitive'
        
    if person1['Destiny'] ==  person2['Destiny']:
        same_destiny = """Same Destiny: the marriage may be comparatively happy, as they live on the same level of activity.
                        They may have grown up together in the same environment, or met through association on the same 
                        level of living. Many marriages, comparatively happy, come about in this way because of common
                        interests from birth; but there should be other points of attraction in common to bring
                        the lasting fire of romance."""
    else:
        same_destiny = 'No same Destiny'

    if person1['Talent'] ==  person2['Talent']:
        same_talent = """Same Talent: this may bring two people together in love and marriage through association at 
                        work or social interests connected with the work. This marriage can be generally
                        happy because of a mutual interest. This is usually built on the commonly accepted
                        traditions and standards of home and marriage. Now and then, this tie is strange 
                        and intense, with many problems of temperament brought over
                        from past incarnations. This attraction can lead to marriage but not to smooth waters."""
    else:
        same_talent = 'No same Talent'
    if person1['Goal'] ==  person2['Goal']:
        same_goal = """Same Goal: The tie between two people with the same Ultimate Goal is a pleasing one, but does not
                    always lead to marriage until later in life, unless there are other points of attraction in common."""
    else:
        same_goal = 'No same Goal'
        
    if person1['Personality'] ==  person2['Personality']:
        same_person = """Same Persons: Two people may be attracted to each other by the Personality.
                        This is not enough for a happy marriage."""
    else:
        same_person = 'No same Persons'
    #mixed relationships.
    mix = intersection(person1_list, person2_list)
    #print('mixed_relationships = ',mixed_relationships)

    mixed = []
    def get_key(my_dict, val):
        for key, value in my_dict.items():
            if val == value:
                return key
        return "key doesn't exist"

    for i in mix:
        if get_key(common_core_contact, i) == "key doesn't exist":
            mixed.append(f'{FN} {get_key(person1, i)} is the {FN1} {get_key(person2, i)}')
            #print(mixed)

    return rule1,rule2,rule3,person1,person2,w_i_t_h1,w_i_t_h2,deduction,affinitive,same_destiny,same_talent,\
           same_goal,same_person,common_core_contact,mix,mixed
    #data = [tool,common_core_contact,deduction,same_destiny]
