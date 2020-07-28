#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Full power lines

r0_all = '''
If you have the full 123 Power Line in your chart, you are
someone that can organize tasks and remain focused to their
completion. You may not be as particular about tasks which
you regard as less important or boring. Sometimes, people
with this Power Line develop a low opinion of other people who
have less of this quality and many don’t hesitate to express
that negative opinion! This can make their personal and
business interactions less harmonious and productive than
they could be if they showed respect andtolerance for the
people around them.
'''

r1_all = '''If you have the full 456 Power Line, then you have plenty of inner
strength and willpower. You should take full advantage of it but take care that your
focus on achieving your own desires does not make you ignore the needs and
opinions of those who are important to you.
'''
r2_all = '''The full 789 Power Line in your Chart indicates a focus on action. Properly
directed, this can be a great asset for you.
But, the downside is that you may become stressed when unable to be as
active as you want to be. You can become a disturbing influence on other
people around you.
Forced inactivity might worry and frustrate you to the point where you
develop headaches and even more serious medical symptoms.
Focus on the positive aspects – many people would be a little envious of your
abundant energy and enthusiasm.
Don’t let negative thoughts or emotions reduce the benefits you can gain
from channeling your desire for action in ways that enhance your life and
your relationships.
'''
r3_all = '''If you have a filled 147 Power Line in your Chart, you have the capacity to
use your hands to construct things. The way which you use this power will
vary between individuals, from growing plants to building apartments or even
cities. Your power can be of great benefit to you financially but you may be less
successful in building strong and enduring personal relationships.
'''
r4_all = '''The 258 Power Line is one to be prized as it indicates emotional balance and
an enhanced ability for understanding and appreciating spirituality in your
environment and other people. This is helpful if you choose a career where
you need to understand other people’s points of view and needs; negotiators of all types, counselors and
teachers.
'''
r5_all = '''If you have the full 369 Power Line as part of your chart, then you have the
ability to understand complex subjects and apply your knowledge.
Try to keep learning through your life, but I suggest that you focus on
subjects which have some practical value for yourself and the rest of the
world. Some people with this Power Line become less tolerant of other people
without it who struggle to keep up with them.
That’s something to avoid as no amount of learning is worth more than
having some tried and trusted friends and colleagues.
'''
r6_all = '''
Your filled 159 Power Line indicates strong determination to achieve your
goals and desires. This is a desirable power and especially valuable in
our fast-paced worldwhere obstacles, human and otherwise, are everywhere.
You need to develop some patience so that you don’t let out cries of
frustration at any setback, however minor. This wastes energy and creates
a poor impression with other people who see this less than professional
display. Maintain, as far as possible, your composure and your professional
image. Put that pent-up frustration to work devising a way around, through
or over the obstacle. I know you can do it!
'''
r7_all = '''If you have a full 357 Power Line in your chart, you have the ability and
interest to understand and use the deepest mystical or religious concepts and
practices. Other people can do this too but it will take more dedication, time
and effort for them to achieve what is likely to be relatively easy for you.
'''
#empty power lines

r0_all_missing = '''
1, 2 and 3 all Missing
This will not appear in the chart of anyone born in the 20th or 21st Century.
You might want to theorize about what anyone without these three numbers
in their chart might have to try to develop. But, it’s not got any practical
value beyond the exercise you give your brain.
'''
r1_all_missing = '''
4, 5 and 6 all Missing:-
The absence of 4, 5 and 6 indicates that you may try to get by rather than
use your abilities and knowledge to your full capability. In today’s highly
competitive world, this usually means that you don’t achieve your most
important goals and desires and you may develop a sense of bitterness and a
high level of frustration.
This can lead to broken relationships and sickness.
The antidote is to find and use your abilities to the full. Accept and work on
improving your ability in any area which you are not achieving success at the
level you desire. Turn off the television and focus on making your mark in
real life.
'''
r2_all_missing = '''
7, 8 and 9 all Missing
If 7, 8 and 9 are all missing from your chart, you may have difficulty in
sticking with demanding tasks until you get them to a successful conclusion.
This can only be turned around when you realize what you are denying
yourself and those close to you by letting yourself quit before the full value of
your plans and effort are reached.
'''
r3_all_missing = '''
1, 4 and 7 all Missing
When there are no 1, 4 or 7 in your chart, it can indicate that you have
strong views based mostly on what you have thought about and a lack of
practical accomplishment because you find it difficult to stick with many tasks
through to completion.
Many people with this indicator in their chart use the word, “should” a lot but
lack the experience to say “I know this will be the result because I have done
it”. Setting this right involves sticking with the tasks you have until you complete
them to a satisfactory standard.
Start small and use the confidence you develop from these accomplishments
to inspire you to greater success and rewards in bigger and more demanding
projects.
'''
r4_all_missing = '''
2, 5 and 8 all Missing
This will not occur in the chart of anyone born in the 20th or 21st Century.
So, I’ll leave this for you to use as a theoretical exercise: How would this lack
affect an individual?
'''
r5_all_missing = '''
3, 6 and 9 all Missing
When you have none of these three numbers in your chart, numerologists
believe it indicates a potential for poor memory that slowly gets worse.
My experience and reading about this gives me some hope that almost
everyone can improve their memory and many people can maintain that
faculty right through their lives.
Memory, in my non-scientific but practice-based opinion, is like a muscle that
will respond, in most cases, to frequent and regular exercise.
If you don’t give it plenty to remember and also focus on whatever it is that
you need or want to remember while it is in front of you, then it will be
harder to maintain it in peak condition.
'''
r6_all_missing = '''
1, 5 and 9 all Missing
When all these numbers are absent, you will probably be a hesitant person
that puts off as many things as you can.
This leads to disappointment and diminished chances of success in
relationships and business.
The only way to empower yourself to reduce the effects of this is to focus on
your objective and, especially, the improvement in your life which will
happen when you prevail over this tendency.
For some people, the desire to avoid continued disappointment and
recrimination from those around you is a greater spur than the potential
rewards.
'''
r7_all_missing = '''
3, 5 and 7 all Missing
When you do not have these numbers in your chart, you are likely to
question things more than most. You may doubt many commonly accepted
beliefs but are likely to become a strong supporter of those claims which you
find proven to your satisfaction.
You should try to be respectful of the beliefs and statements of other people
even when you strongly disagree with their views.
'''
# missing numbers

missing_numbers = {1:"""
Missing 1: This indicates a need to develop a more independent attitude or
you risk being controlled to a great extent by the needs and demands of
other people.
""",
2:"""
Missing 2: You need to adjust your approach to show more appreciation of
other people’s views and desires and a willingness to discuss more than
demand your views always prevail.
""",
3:"""
Missing 3: The absence of any 3’s in your chart indicate that you need to
develop your power to express yourself more clearly.
""",
4:"""
Missing 4: You need to become more organized so that you can progress
your career faster and give yourself more family or social time.
""",
5:"""
Missing 5: With no 5 in your chart, you probably tend to exist in your
comfortable rut rather than look for opportunities to meet new people and
expand your business and social horizons. You must try to sample more of
the vast variety of enjoyable experiences which are within your reach.
""",
6:"""
Missing 6: You need to develop a more responsible attitude to the needs
and views of your family and others that depend on you.
""",
7:"""
Missing 7: You are focused almost exclusively on practical issues, mostly
money and business. Your options would increase and your potential for
greater success in both personal and business areas could increase if you
widened your horizons to include the rest of what our world can offer.
Don’t stop, but slow down and smell the flowers – while you can!
""",
8:"""
Missing 8: You need to increase your motivation to get yourself out of where
you are to where you can easily reach with just a little more drive and
sharper focus. Don’t just look at what you have. Look at what you are
denying yourself andthose who are close to you when you accept low rewards
and a comfortable rut.
""",
9:"""
Missing 9: This indicates that you need to think more about others rather
than focusing entirely on your own desires – you’ve probably already got
your personal needs well taken care of through your obsession with work
above all.
"""
}

s_num = {
1:["",
"""
One 1: This indicates that you have the potential to express yourself well.
But, most people that have only one 1 in their chart are limited in their ability
to express their emotional desires and inner thoughts. They are also likely to
be intolerant of other people’s different viewpoints to some degree.
""",
"""
Two 1’s: The presence of the second 1 somehow gives more balance to your
ability to express yourself verbally. You will also be better able to seriously
consider and discuss other people’s differing viewpoints than if there was just
a single 1 in your chart.
""",
"""
Three 1’s: Many professional speakers have this in their chart.
If you have this and also have one or more 2’s, 5’s or 8’s, then you are likely
to be a rapid and enthusiastic talker. This can be good if you focus your
chatter on subjects which also interest those around you.
If you do not have any 2’s, 5’s or 8’s in your chart, you are likely to be more
reserved and skeptical.
""",
"""
Four 1’s: Unlike those who are balanced with the presence of just two 1’s on
their chart, the people who have four 1’s are deep thinkers with a lesser
ability to express themselves. They are often misunderstood but accept their
lot and keep smiling. Over time, they become less communicative because of
the difficulties they have encountered which means we all lose out because
their ideas are often worth careful attention.
""",
"""
Five 1’s: If you have more than four ones you are likely to have greater
difficulties with verbal expression. But, you may be able to use your
intellectual capacity and energy to develop non-verbal ways of expressing
your ideas through music or other forms.
"""
],
2:["",
"""
One two on your chart indicates a heightened degree of sensitivity
and strong intuition. But, be careful about taking criticism or disagreement
too much to heart. Remember, friends can disagree but still remain friends.
""",
"""
Two 2’s give you a more balanced level of intuitions and better
capacity to deal with negativity from those around you. You are likely to have
a higher than average rate of success when you pay attention to your first
impressions.
""",
"""
If you have three 2’s in your chart, you may find tsh:e world
around you less appealing than your own thoughts and dreams.
Those qualities may give you some success in theatre or other performing
areas but, be warned, you will have to develop a mental armor to protect
your feelings and your integrity.
""",
"""
With more than three 2’s in your chart, you are liksely to
be impatient and to react strongly without consideration of other’s views or
feelings. This can limit your social and business options unless you work hard on
controlling your impulses and start to consider the effect of your actions and
words on those around you.
"""
],
3:["",
"""
With just one 3 in your chart, I expect you to be a moderately happy
person. Your memory is probably better than average but could be improved
even more with little effort.
""",
"""With two 3’s in your chart, you have the qualities of the person
with just one 3, but may have too much imagination to make the best use of
those qualities. You need to rein in your imagination when it might
interfere with your social or business contacts.
""",
"""If you have three 3’s, you are likely to prefer your own company
and find it hard to create and maintain close relationships.
Only the realization of what benefits you are denying yourself and a
determined effort at making friends can change the outlook for you.
""",
"""People with four 3’s in their chart are likely to be severely
hyperactive. There are relatively few of these people because the occurrence
of four 3’s only happens rarely.
"""
],
4:["",
"""If you have just one 4 in your chart, you keep your imagination
under tight control and focus on the facts and benefits, particularly for
yourself, of any situation.
""",
"""Two 4’s in your chart indicate that you prefer to fosc:us on physical
action, often to the almost total exclusion of the spiritual area.
This can help you achieve your goals but may interfere with your personal
relationships. Some people in this category may find themselves being
manipulated when others take advantage of their desire for close friendship
at almost any price.
""",
"""If you have this many 4’s in your chart, your manual
ability is likely to be far above average and this can help you succeed in your
business ventures. But, you will always be less successful in your personal
relationships if you do not bother to give an appropriate level of attention to them.
"""
],
5:["",
"""You’re lucky if your chart has just one 5. It indicates a person with a
mature understanding of their place in life and a rare ability to encourage
others to their best efforts.
""",
"""You have above average enthusiasm and vigor whsic:h is great when
you don’t overpower everyone around you. Avoid alcohol and stimulants –
you don’t need them!
""",
"""Three or more 5’ Your above average drive and motivation can be great
advantages. But, try to be considerate of others because your tendency to
speak first and loudest can do damage in your business and personal
encounters which may be very hard to recover from.
"""
],
6:["",
"""If you have just one 6 in your chart, your main focus is probably your
home and family. Where you can find time from that focus, you can find
success with almost any kind of artistic endeavor which appeals to you.
""",
"""Your two 6’s indicate a deep, even over-protectives attitude to your
home and family which can interfere with your enjoyment of the environment
you work so hard to create and maintain. Try to rest and pass some
responsibility to other family members. They care for you and appreciate
your efforts. But, your single-minded focus is likely to worry them or
even make them less responsive to you.
""",
"""Three or more 6’ You need to step back a little before your obsessiosn: to
protect and nurture your home and family have a serious negative effect on
your own health.
Give others more responsibility and opportunities to contribute.
That will help to ensure that you all will be able to enjoy the fruits of your
combined efforts in the future.
"""
],
7:["",
"""One 7 indicates a person that has to learn life’s lessons from personal
experience which can be painful and costly.
But, when you have come through that, you have a wisdom based on
experience which will help you prosper and give you many opportunities to
share your knowledge with other people.
""",
"""Two 7’s indicate that you will have even more hards :times to
surmount. Your options are very limited; to wither and fall or use the lessons
to create a better future for yourself and those close to you.
""",
"""Three 7’s may mean that you face huge struggles as you learn
from experience. This can push you down lower than where you started.
You will either give up the struggle and be consumed by your own bitter
regrets of losses that you suffered or you will really learn the lessons and use
them to build a firm foundation for your eventual, almost inevitable success.
"""
],
8:["",
"""One 8 shows that you pay attention to detail and this can be a great
help in achieving whatever goal that you focus on.
It is also a quality which can ensure that you succeed in your own business
or become a valuable, trusted employee. Just make sure that your value to
your employer is reflected in your pay.
Of course, your attention to detail will probably ensure that.
""",
"""Two 8’ Your attention to detail can border on obsession. Try to step back
and focus some of your attention on other people’s needs and views.
Otherwise, you can have the best ideas in the world but have great difficulty
in having them accepted.
""",
"""Three or more 8’ You will be restless, even driven, and this can makse: it
hard to work with others unless you find a way to draw back and be more
cooperative and patient.
"""
],
9:["",
"""
One 9: This indicates you have a degree of inner strength which can be used
to reach your goal, whatever it may be. Of course, the presence
of the single nine cannot guarantee success. You also need to prevent
your goal of material success from taking over other goals
including your desire for a home and family.
""",
"""
Two 9’ These indicate that you have a higher than averagse: intelligence
accompanied by a degree of idealism. You can succeed in service occupations
or directing charitable organizations. But, you will need to learn how to
be less critical of the people you must deal with and motivate those who do
not share your idealism or your other qualities.
""",
"""Three or more 9’ You are endowed with above-average intelligence which
can be a great advantage if you do not become isolated mentally from those
around you who do not have your intellectual abilities.
To prevent burnout or mental instability, you need to consciously retain and
increase the strength of your personal and professional links.
This will also help you when you want to use your humanitarian instincts to
get help for the less fortunate people around the world or just in your
neighborhood.
"""
]
}