#!/usr/bin/python3
# -*- coding: utf-8 -*-

describe = {
#Sun and Moon
"sun_to_natmoon":"""Male and Female; illuminated achievements, needs, and
sensitivities; highlighted relationships, seeing the light.""",
"moon_to_natsun":"""Sensitivity to need-fulfillment; seeing the light; female influence.""",
"merc_sun/moon":"""Thoughts about male-female principles, including marriage; relationships in general; plans for fulfillment.""",
"ven_sun/moon":"""Friendship; love awareness; harmony.""",
"mars_sun/moon":"""Energy helping or upsetting relationship; serval awareness in
partnership; drive for fulfillment.""",
"jup_sun/moon":"""Happy relationship; enthusiasm for life; success.""",
"sat_sun/moon":"""Difficult concerns in relationship; addressing problems; possible
inhibition or separation; weakened system.""",
"ura_sun/moon":"""Intensification of independence within relationship; sudden
developments; possible breakup.""",
"nep_sun/moon":"""Misunderstandings in relationship; deception; discontent.""",
"plu_sun/moon":"""Potential new perspective in relationship; critical time of
development; separation to start anew.""",
"nod_sun/moon":"""Making contact; new associations.""",
"asc_sun/moon":"""Openness to others; feeling secure.""",
"mc_sun/moon":"""Ego fulfillment in relationship; marriage.""",
####################################################
#Sun and Mercury
"sun_to_natmerc":"""Illumination of intelligence; thoughts; common sense.""",
"merc_to_natsun":"""Thinking about ego potentials; new ideas.""",
"moon_sun/merc":"""Awareness of needs; emotional thoughts.""",
"ven_sun/merc":"""Idealization of thoughts about relationships and love; thoughts
about sexual matters; writing about love.""",
"mars_sun/merc":"""Excitement; nervous drive; energies to tackle a project; possible
quarrelsomeness.""",
"jup_sun/merc":"""Optimism; broadening one's horizon; successful travel, speechmaking,
publishing; uplifting thoughts about religion.""",
"sat_sun/merc":"""Seriousness in mental outlook; possible depression; sadness
about potential separation; a new maturity.""",
"ura_sun/merc":"""High excitability in the nervous system and thinking process;
sudden eruptions of temperament; quick trips; new
circumstances.""",
"nep_sun/merc":"""Fantasy; imagination; spiritual wondering; possible deception
by others; something undermining the perceived reality.""",
"plu_sun/merc":"""The dramatic push to new perspectives; big plans,""",
"nod_sun/merc":"""New social contacts; sales presentations; meetings.""",
"asc_sun/merc":"""Exchanging ideas; sharing with others; pleasant mental state.""",
"mc_sun/merc":"""Ego awareness; helping one's plans work and standing up to the
test; successful communications.""",
################################################################
#Sun and Venus
"sun_to_natven":"""Romance; love relationship; illumination of one's sense of beauty; aesthetics; marriage; birth.""",
"ven_to_natsun":"""Idealization of outlook; feeling love; the artistic touch.""",
"moon_sun/ven":"""Strong feelings of love in relationship; feeling good about life.""",
"merc_sun/ven":"""Thinking about love, usually in an idealized way; dialogues
about feelings; a beautiful trip.""",
"mars_sun/ven":"""Desire for love; sexual feelings; the application of creativity.""",
"jup_sun/ven":"""Happiness; success; idealized relationship; a grand vacation.""",
"sat_sun/ven":"""Strain within love relationship; hard work to make feelings
right again, to make ends meet; fears of separation.""",
"ura_sun/ven":"""Intensified sexuality; "love-crazy"; sudden romantic meetings.""", 
"nep_sun/ven":"""Dreaminess about love potential; overindulgences of all kinds for ego gratification or defense; self-deception.""",
"plu_sun/ven":"""Extreme intensification of emotions; a waste of feelings and
possible squandering of relationship values; the feeling of fate
within relationship perspectives.""",
"nod_sun/ven":"""Meetings under lovely circumstances; artistic people and
events; making new friends.""",
"asc_sun/ven":"""Being at one's best; attractiveness to others.""",
"mc_sun/ven":"""The love-union; marriage; feeling of fulfillment.""",

##################################################################

#Sun and Mars 
"sun_to_natmars":"""nergy applied directly, naturally, vigorously.""",
"mars_to_natsun":"""Temperament; feeling attacked; possible accident; intensified
sex drive; surgery.""",
"moon_sun/mars":"""Awareness of relationship dynamics in balance with individual
needs; the feminine influence; thoughts for marriage.""",
"merc_sun/mars":"""Alertness; ready for action; fast-talk; busy travel.""",
"ven_sun/mars":"""The feelings of love; sex; conception; birthing.""",
"jup_sun/mars":"""Optimism; expansive energy application; success.""",
"sat_sun/mars":"""Difficulties in energy application; obstacles against work
advancement; inhibitions; worries and indecision.""",
"ura_sun/mars":"""High excitability; intense reflex-actions; impulse; sudden events
and forceful adjustment ofnew circumstances; militarism;
over-exertion causing breakdown of efficiency.""",
"nep_sun/mars":"""Possible loss ofvitality; difficulty concentrating; feeling "off the
track.""",
"plu_sun/mars":"""Force; ruthless application of energy; defensiveness to an
extreme; warring relationships; severe health strain possible.""",
"nod_sun/mars":"""Meeting new associates in work situation; teamwork; dating.""",
"asc_sun/mars":"""Feeling robust; being seen as hearty and confident.""",
"mc_sun/mars":"""Success; loving ones work; efficiency; ready to fight for ones principles.""",

########################################################################

#Sun and Jupiter
"sun_to_natjup":"""Recognition; success; feeling great.""",
"jup_to_natsun":"""Being rewarded; success; a great vacation.""",
"moon_sun/jup":"""The feeling of needs fulfilled; good health; fine relationship.""",
"merc_sun/jup":"""Efficient and successful thinking; good news; writing,publishing, contracting, traveling; healthy mental outlook.""",
"ven_sun/jup":"""Happy relationship; expansive romance; recognition; honors.""",
"mars_sun/jup":"""Successful application ofwill-power; zeal; enthusiasm that catches on.""",
"sat_sun/jup":"""collision" between what one wants and what is demanded;
a quandary of law and order; a curtailment; negativism; loss.""",
"ura_sun/jup":"""Sudden success; great expectations; expansive outlook; the sense
of good luck.""",
"nep_sun/jup":"""Increased sensitivity; the sense of things spiritual; loss of
concentrated orientation.""",
"plu_sun/jup":"""Successful efforts; great good luck; fulfillment in a big way;
an estate; an inheritance.""",
"nod_sun/jup":"""Meeting happy/wealthy/successftil people; new plans with
others that feel "bound to succeed.""",
"asc_sun/jup":"""Great enthusiasm; infectious happiness; successful teamwork.""",
"mc_sun/jup":"""Good luck, success, and fulfillment; ego recognition; time of
great good fortune.""",

################################################################

#Sun and Saturn 428
"sun_to_natsat":"""Illumination of ambition; testing if one is on the right track;
awareness of responsibility; importance of the father.""",
"sat_to_natsun":"""The sense of difficulty, overwork, depletion, confinement,
discipline; the fear of loss; "aloneness"; possibly grief.""",
"moon_sun/sat":"""A sense ofloneliness; separation from females; personal needs
under wraps; feeling inferior; hurt.""",
"merc_sun/sat":"""Serious thinking; grave decisions; possible depression; striving
for a new way of seeing things.""",
"ven_sun/sat":"""Feelings of an inhibited love-life; suppressed feelings in
relationship; feeling victimized.""",
"mars_sun/sat":"""Running "hot and cold"; energies feel confined; the sense of
futility.""",
"jup_sun/sat":"""break-up of a relationship or value system for eventual
recovery and gain; the cloud with a silver lining.""",
"ura_sun/sat":"""The clash between new ways of doing things and long-established
ways; crises within relationship; the fight for individuality.""",
"nep_sun/sat":"""Sadness; loss of hope; delusions within relationship leading to
the feeling of aloneness.""",
"plu_sun/sat":"""The threat of loss in relationship or health; a pressure to change
one's entire value system.""",
"nod_sun/sat":"""Difficult meetings with others.""",
"asc_sun/sat":"""Being misunderstood; possible threat to health.""",
"mc_sun/sat":"""Lacking the feeling ofsuccess; feeling devalued; working hard
to win; the "lone wolf.""",

##########################################################################

#Sun and Uranus 429
"sun_to_natura":"""Independent, even revolutionary spirit; being oneself and
getting away with it.""",
"ura_to_natsun":"""Intensified feeling of ego aggrandizement; excited state in
relationship; possible break up.""",
"moon_sun/ura":"""Emotional excitability; the intense woman; demand for need
fulfillment.""",
"merc_sun/ura":"""Quickness of mind; the spark of understanding; the harsh word;
seeing things too analytically for comfort.""",
"ven_sun/ura":"""Sudden love feelings; instant attraction; sexiness.""",
"mars_sun/ura":"""Rash action; possible injury; combativeness; temperament;
sudden breakdown of relationship; "hitting a brick wall.""",
"jup_sun/ura":"""Rewards for innovation; ego recognition; surprise and success.""",
"sat_sun/ura":"""A struggle for individual freedom; the fight against the routine,
old, or traditional way of doing things; separation.""",
"nep_sun/ura":"""Possible loss of the sense ofindividuality; self-deluding schemes
for ego recognition; threat to relationship and personal health.""",
"plu_sun/ura":"""The demand for new perspectives; a new individual reality;
reforms; a strong drive for power; twists of fate.""",
"nod_sun/ura":"""Meeting unusual or intense people; quick new associations.""",
"asc_sun/ura":"""pearing at one's best; high excitability; sudden events.""",
"mc_sun/ura":"""Major events in support of big plans; hopeful triumph for the
ego.""",

################################################################################

#Sun and Neptune 430
"sun_to_natnep":"""Illumination of sensitivity, imagination, aesthetics; possible
befuddlement, remoteness, impracticality.""",
"nep_to_natsun":"""The sense of ego loss; hypersensitivity; potential spiritual
rationalization, inspiration; deception; illegality.""",
"moon_sun/nep":"""Moodiness; high impressionability; very special inner
experiences not easily understood; gynecological concerns.""",
"merc_sun/nep":"""Mental sensitivity; self-deception; worrisome; fear from a lack
of resourcefulness.""",
"ven_sun/nep":"""Reveling in love impractically; emotional disappointments.""",
"mars_sun/nep":"""Magnetism; sexual discovery; nefarious scheming to exalt
the ego.""",
"jup_sun/nep":"""Success through inspiration or imagination; possible
overindulgence.""",
"sat_sun/nep":"""Emotional struggle or pain; concerns about the blood; bereavement
about separation.""",
"ura_sun/nep":"""Sudden impressionability or even psychic awareness; nervous
reactions for unclear reasons; relationship disputes.""",
"plu_sun/nep":"""Extreme sensitivity; use of the spiritual, psychic, or illusory as
a force for persuasion; fateful deception.""",
"nod_sun/nep":"""Deception in relationships; support of the needy.""",
"asc_sun/nep":"""A sensitive show to others, true or fabricated; difficulties being
accepted.""",
"mc_sun/nep":"""Loss of ego strength or aesthetics taking over ego presentation;
depression; emotional stress in the profession; artistic strength.""",

##################################################################################

#Sun and Pluto 431
"sun_to_natplu":"""Illumination of power needs; the need to control; new
perspectives confirmed in life.""",
"plu_to_natsun":"""Powerful force creates major change in the life; identity change;
sudden prominence; exhibitionism.""",
"moon_sun/plu":"""Attempts to project power and persuasion; feelings possibly
trampled in relationship.""",
"merc_sun/plu":"""Extraordinary mental projection; "lording it over" someone;
great salesmanship.""",
"ven_sun/plu":"""Emotional upset; creative force; strength in the arts.""",
"mars_sun/plu":"""Enormous drive; strenuous self-application; carving new
perspectives in one's life; strong sexual interest.""",
"jup_sun/plu":"""Expansion of power base; success; international opportunities.""",
"sat_sun/plu":"""Potential loss in relationship through power struggle;
ruthlessness; separation.""",
"ura_sun/plu":"""New individual perspectives; sudden change; rebellion; reform.""",
"nep_sun/plu":"""Self-sacrifice in relationship or to a cause; high impressionability;
vocation problems.""",
"nod_sun/plu":"""Very special new attachments; meeting the powerful.""",
"asc_sun/plu":"""Enormous power projection; being forced to fight.""",
"mc_sun/plu":"""Striving for power and control; vocational upset and change
to adopt new perspectives; power games with important
consequences.""",

###############################################################################

#Sun and Lunar Node 432
"sun_to_natnod":"""Experiences shared with others become important; the
public..""",
"nod_to_natsun":"""New contacts come into the life..""",
"moon_sun/nod":"""Feelings shared with others; the relationship dynamics ofwife
and husband are highlighted..""",
"merc_sun/nod":"""Communications with others; business contacts; news;
commentary..""",
"ven_sun/nod":"""Lovely associations; the arts; beginning of a romantic
relationship..""",
"mars_sun/nod":"""Vigorous drives with others to gain personal importance..""",
"jup_sun/nod":"""Public recognition; associations with the wealthy or
international; positive legal involvements; good fortune..""",
"sat_sun/nod":"""Reserve in relationships; maturation; patience with others..""",
"ura_sun/nod":"""Attraction to unusual individuals; upsets through intensity; the
drive for popularity..""",
"nep_sun/nod":"""Feeling that relationships are threatening or bothersome; feeling
let down by others..""",
"plu_sun/nod":"""Being persuasive; ordering and controlling others; exerting
influence; public prominence..""",
"asc_sun/nod":"""Making personal contacts..""",
"mc_sun/nod":"""Becoming prominent through associations.""",

#####################################################################################

#Sun and Ascendant 433
"sun_to_natasc":"""Recognition; being seen for who one is.""",
"asc_to_natsun":"""Testing the identity; personality clarification through the reactions
of others.""",
"moon_sun/asc":"""Feelings and needs in relationships become very important,
especially for females or with females.""",
"merc_sun/asc":"""Thinking about who one really is in relation to others;
existential awareness and sensitivity.""",
"ven_sun/asc":"""Affections; love of others; peace.""",
"mars_sun/asc":"""Making things happen; strong self-projections; disputes and
possibly anger; the sense ofself-promotion.""",
"jup_sun/asc":"""Philanthropic or social welfare outlook; successful relationship.""",
"sat_sun/asc":"""Inhibition or discretion; reserve or depression; separation.""",
"ura_sun/asc":"""Intensification of self-image; pushy behavior; upsets.""",
"nep_sun/asc":"""High sensitivity about others' opinions; being duped; being
disregarded.""",
"plu_sun/asc":"""The power play through personal persuasion; fated events.""",
"nod_sun/asc":""" Personal acquaintances; business contacts.""",
"mc_sun/asc":"""Personal recognition, especially through the profession; the
influence of the parents.""",

#####################################################################################

#Sun and Midheaven 434
"sun_to_natmc":"""Ego recognition; potential glory; usually successful; fulfillment.""",
"mc_to_natsun":"""Professional fulfillment; getting what one deserves.""",
"moon_sun/mc":"""Finding one's position in life, usually through the profession.""",
"merc_sun/mc":"""Thinking about one's position in life.""",
"ven_sun/mc":"""Feelings about love, the arts, aesthetics; sociability.""",
"mars_sun/mc":"""Strong power maneuvering in the profession; promotion and
success.""",
"jup_sun/mc":"""optimism; publicity; fulfillment.""",
"sat_sun/mc":"""Maturation through sobering experiences; refinement of ambition; learning from apparent mistakes.""",
"ura_sun/mc":"""Sudden changes; shifts of position.""",
"nep_sun/mc":"""Something threatens ego definition; confusion; insecurity.""",
"plu_sun/mc":"""Very strong drive for fulfillment of objectives; changes in life
perspective; upset in relationships.""",
"nod_sun/mc":"""Forming relationships.""",
"asc_sun/mc":"""Personal relations.""",

####################################################################################

#Moon and Mercury 435
"moon_to_natmerc":"""Thinking with the feelings; emotional perception.""",
"merc_to_natmoon":"""Mental stimulation about personal needs and how to fulfill
them; improved communication; the advice of a woman.""",
"sun_moon/merc":"""Realism; practical planning.""",
"ven_moon/merc":"""Lovely thoughts; the sense of beauty; art appreciation.""",
"mars_moon/merc":"""Critical, perhaps nervous thought processes; clarification
of objectives.""",
"jup_moon/merc":"""Rational thought; good judgment; sound planning; interests in
travel, communication sciences, educational institutions.""",
"sat_moon/merc":"""Solving problems to grow in wisdom; thoughts about patience;
possible depression if the tide has turned.""",
"ura_moon/merc":"""Sudden, innovative thoughts and plans; irritability about
progress; getting on with things hastily.""",
"nep_moon/merc":"""An active imagination; reverie; hypersentience; falsehood.""",
"plu_moon/merc":"""New perspectives; persuasion or being persuaded; the force of
thought.""",
"nod_moon/merc":"""Sharing thoughts with others; making contacts.""",
"asc_moon/merc":"""Letting people know how one thinks; sharing opinions.""",
"mc_moon/merc":"""Making decisions, usually about one's profession or social
position.""",

####################################################################################

#Moon and Venus 436
"moon_to_natven":"""Love and sensitivity.""",
"ven_to_natmoon":"""Grace; good social reception; cooperation.""",
"sun_moon/ven":"""The love in a marriage; art appreciation.""",
"merc_moon/ven":"""Thinking about love.""",
"mars_moon/ven":"""Potential overindulgence; living passionately.""",
"jup_moon/ven":"""Good luck; lots of good feelings; feeling loved.""",
"sat_moon/ven":"""Sternness within feelings; tightness entering romance.""",
"ura_moon/ven":"""Sudden romantic feelings and attachments; intensification of
sexuality.""",
"nep_moon/ven":"""Dreaminess; fantasies about love, the erotic; possible
misdirection of love; being duped.""",
"plu_moon/ven":"""Powerful awakening of the emotions, more sexual than
temperamental; procreation; complications and a waste
of emotions.""",
"nod_moon/ven":""" Lovely association; rewarding social contacts; maternal feelings.""",
"asc_moon/ven":"""Affectionate behavior toward others; being well-received.""",
"mc_moon/ven":"""Success; feeling valuable.""",

#################################################################################

#Moon and Mars 437
"moon_to_natmars":"""Emotional excitement; emotional conviction.""",
"mars_to_natmoon":"""Strong drive to fulfill needs, to "let it fly"; disruption;
hyperactivity.""",
"sun_moon/mars":"""The working bond within a marriage; prosperity through
relationship.""",
"merc_moon/mars":"""Nervousness; being irritable; worrisome preoccupations.""",
"ven_moon/mars":"""Sexual desires; creativity; promoting things artistic.""",
"jup_moon/mars":"""Principles; justified actions.""",
"sat_moon/mars":"""Caught in the middle of the road; frustration.""",
"ura_moon/mars":"""Intensified temperament; eruption; anger; arguments leading
to emotional wear and tear.""",
"nep_moon/mars":"""Emotional magic; possible duplicity; weaving a spell for personal
gain.""",
"plu_moon/mars":"""Powerful opinionation; demanding nature.""",
"nod_moon/mars":""" Energetic activity with others; good teamwork.""",
"asc_moon/mars":"""Personal enterprise; leadership.""",
"mc_moon/mars":"""Marriage thoughts; self-promotion; getting things off the
ground.""",

#############################################################################

#Moon and Jupiter 438
"moon_to_natjup":"""Feeling happy; being successful; contentment; religiousness or
the judiciary becoming important.""",
"jup_to_natmoon":"""Opportunity; reward; publicity; success.""",
"sun_moon/jup":"""Optimism; a fine relationship.""",
"merc_moon/jup":"""Making expansive plans; learning; traveling.""",
"ven_moon/jup":"""Lovingness; artistry; relating rewardingly through the emotions.""",
"mars_moon/jup":"""Enthusiasm; get-up-and-go; making success happen.""",
"sat_moon/jup":"""Interference possible through outside restrictions; separation
from an important female or becoming distant from important
emotions.""",
"ura_moon/jup":"""Confidence; expectation of reward.""",
"nep_moon/jup":"""Losing focus of objectives; success feels like it is leaving one's
grasp.""",
"plu_moon/jup":"""Major plans for major triumph; the big picture and the power
to make it appear.""",
"nod_moon/jup":"""Sociability; successful contacts.""",
"asc_moon/jup":"""Expansive nature; being happy and well-accepted.""",
"mc_moon/jup":"""Popularity; confidence; possible religious significances; good
fortune, especially through a female.""",

#################################################################################

#Moon and Saturn 439
"moon_to_natsat":"""Awareness of ambition, strategy, direction,Self-control; loneliness.""",
"sat_to_natmoon":"""Sobering times; feelings of enforced controls; possible separation
in relationship.""",
"sun_moon/sat":"""Prudence; maturity; the wise thought; sadness and perhaps
depression, especially among women.""",
"merc_moon/sat":"""Emotional changes; restrictions in expression; the grace "to start
over again.""",
"ven_moon/sat":"""The sense of real problems; difficulty getting off the ground
except by very careful, strategically planned exertion of energy.""",
"mars_moon/sat":"""The sense of law and order prevails; the sense of duty; feeling
confident about structure; appreciating why certain controls are necessary.""",
"jup_moon/sat":"""Reaching for emotional freedom; exploding out of frustration.""",
"ura_moon/sat":"""Feelings of inferiority; melancholy.""",
"nep_moon/sat":"""The threat of loss; feeling isolated; needs repressed.""",
"plu_moon/sat":""" Making contacts is difficult; loneliness.""",
"nod_moon/sat":"""A reserved self-presentation.""",
"asc_moon/sat":"""Making things happen carefully; structuring ambition.""",
"mc_moon/sat":"""Emotional individuation, emotional tensions, Intensification of self; impulsivity to fulfill needs.""",

#####################################################################################

#Moon and Uranus 440
"moon_to_natura":"""The sense of free-will; sudden attachments; anxiety about
accomplishment.""",
"ura_to_natmoon":"""Excited mental activity; expecting a surprise; innovative ideas;
short trips.""",
"sun_moon/ura":"""Excitability of emotions; sudden sexual activities; artistic
creativity.""",
"merc_moon/ura":"""Lack of self-control; self-aggrandizement.""",
"ven_moon/sat":"""Large plans to put the self forward; sudden success.""",
"mars_moon/ura":"""Striving for independence in order to solve things; the struggle""",
"jup_moon/ura":"""between the traditional and the avant-garde; changes in
emotional expression.""",
"nep_moon/ura":"""Nervousness about a sense of futility; things are unclear and
insecure for no apparent reason.""",
"plu_moon/ura":""" Bombast; the fanatical push for fulfillment ofneeds;
sensationalism.""",
"nod_moon/ura":"""Restlessness in contact with others.""",
"asc_moon/ura":"""Excitability; consideration of geographic relocation.""",
"mc_moon/ura":"""Much excitement about ambition, potential gains; sudden
changes of plans.""",

####################################################################################

#Moon and Neptune 441
"moon_to_natnep":"""The awakening of aesthetics, special sensitivities, or the spirit.""",
"nep_to_natmoon":"""Subconscious awareness emerges, refinement or bewilderment.""",
"sun_moon/nep":"""A delicate relationship; the man trying to support the woman;
illuminated aesthetics; the importance of the spirit.""",
"merc_moon/nep":"""Fantasy; imagination; remembrance of things past; saying one thing and meaning another; vagueness.""",
"ven_moon/nep":"""Highly romanticized feelings oflove; art appreciation; being
deceived through the emotions.""",
"mars_moon/nep":"""Personal magic; hypersensitivity; weakened system.""",
"jup_moon/nep":"""Grand imaginings and plans; artistic interests and success.""",
"sat_moon/nep":"""sense of suffering under the yoke; hard work to restructure ambition; shaking off indolence.""",
"plu_moon/nep":"""Temperamental impulse; emotional unpredictability. Emotional
shock, upheaval, change.""",
"nod_moon/nep":"""The projection of passivity or confusion.""",
"asc_moon/nep":"""The feeling of having lost ego definition.""",
"mc_moon/nep":"""Artistic talent possible; artsy temperament; imagination can pay
off significantly; emotional concerns from the early home life
come to consciousness.""",

###################################################################################

#Moon and Pluto 442
"moon_to_natplu":"""Zeal; intensity ofself-application.""",
"plu_to_natmoon":"""Extreme emotional intensity; upheavals; exaggerated new plans.""",
"sun_moon/plu":"""Tight team effort in relationship; special far-reaching plans;
emotional excitement.""",
"merc_moon/plu":"""Strategizing, planning, conceptualization; the power of
persuasion.""",
"ven_moon/plu":"""Intensification of feelings; romance; anything amorous and
need-fulfilling.""",
"mars_moon/plu":"""Often an intense emotional crisis; great tension; too much
energy not knowing where to go; frustration and anger.""",
"jup_moon/plu":"""Big plans; luck and success; rich emotionalism.""",
"sat_moon/plu":"""Inclination to feelings of loss; depression; constraint; the
pressure to regroup forces and plan anew.""",
"ura_moon/plu":"""Possible nervous crisis; intensity that can get out of hand;
tremendous projection of self is possible; identification with
the world; sudden upsets.""",
"nep_moon/plu":"""The supernatural is added to the emotional life; the feeling of
fate; the fear ofthe unknown; feeling weakened somehow.""",
"nod_moon/plu":""" Emotionalism disrupts teamwork and getting along with others.""",
"asc_moon/plu":"""Tremendous self-projection in reaction to the environment;
temperamental upset.""",
"mc_moon/plu":"""Ego consciousness prevails; one-sided emotional intensity.""",

####################################################################

#Moon and Lunar Node 443
"moon_to_natnod":"""Association with others, usually emotionally based.""",
"nod_to_natmoon":"""Contacts with others brings assistance and comfort.""",
"sun_moon/nod":"""Harmony in relationships.""",
"merc_moon/nod":"""Thinking about interpersonal reactions; getting along with others; building cooperation.""",
"ven_moon/nod":"""Affectionate attachments with others; contacts with artistic people or cultural events.""",
"mars_moon/nod":"""Energetic associations and teamwork.""",
"jup_moon/nod":"""Confidence; good luck through interaction with others.""",
"sat_moon/nod":"""Working hard with others; sometimes having then to go it alone.""",
"ura_moon/nod":"""Meeting exceptional people or experiencing unusual events with
or through others; sudden new attachments.""",
"nep_moon/nod":"""The potential undermining of relationships or contacts with
others; sentimentality.""",
"plu_moon/nod":"""Powerful forces affect interpersonal relationships; the sense
of fated attraction.""",
"asc_moon/nod":"""The importance of interpersonal relationships is brought
forward.""",
"mc_moon/nod":"""Ego-involvement intensified in emotional relationship.""",

#####################################################################################

#Moon and Ascendant 444
"moon_to_natasc":"""AS Focus on personal needs and relationships to fulfill them.""",
"asc_to_natmoon":"""Focus on personal needs and relationships to fulfill them.""",
"sun_moon/asc":"""Evaluation of interpersonal relationships for one's own benefit;
interaction of marriage partners from one's personal perspective.""",
"merc_moon/asc":"""Thinking about how to put one's best foot forward; creating
confidence.""",
"ven_moon/asc":"""Adaptability to preserve the love in a relationship; social events
that put one forward.""",
"mars_moon/asc":"""Energetic self-projection; temperamental change at the slightest
sense of frustration.""",
"jup_moon/asc":"""Expansive confidence; gregariousness; largesse; publicity.""",
"sat_moon/nep":"""The process of maturation; heavy moods of deliberation;
severity; depression; feelings of constraint.""",
"ura_moon/asc":"""Excited self-projection; sudden relationships.""",
"nep_moon/asc":"""Self-delusion is possible; feeling "wiped out"; loneliness;
deception by a female.""",
"plu_moon/asc":"""Over-dramatization or obsessive importance of relationship;
dramatic personal projection to others.""",
"nod_moon/asc":"""Desire for contacts; importance ofwomen as associates.""",
"mc_moon/asc":"""Learning about one's position in the world; revival of concerns
from the early home life.""",

###############################################################################

#Moon and Midheaven 445
"moon_to_natnep":"""One's strongest needs are out in the open.""",
"nep_to_natmoon":"""Ego-consciousness alerts all one's senses.""",
"sun_moon/mc":"""Positive attitude toward life; the spirit of enterprise.""",
"merc_moon/mc":"""Thinking about one's position in life.""",
"ven_moon/mc":"""Graceful social positioning; success with the emotions;
significant relationships are possible.""",
"mars_moon/mc":"""Strong work orientation; promotion; strength on the job; the
introduction of a man to a woman.""",
"jup_moon/mc":"""High enthusiasms; probably professional success; an awakening
of religion or the study of philosophy becomes important.""",
"sat_moon/mc":"""Sobering experiences affect the emotional life; greater efficiency;
depressing longing.""",
"ura_moon/mc":"""High degree of emotional excitement; nervousness in reaction
to changes; the sense ofvocational instability or the threat of
pending upset; anxiety.""",
"nep_moon/mc":"""Sensing a loss of ego-identification; feeling devalued; perhaps
the awakening of aesthetics or things spiritual.""",
"plu_moon/mc":"""Tremendous thrust forward, usually accompanied by intense
emotion; the biggest picture; rejuvenation.""",
"nod_moon/mc":"""Professional contacts.""",
"asc_moon/mc":"""Awareness of one's emotional orientation; self-evaluation.""",

#################################################################################

#Mercury and Venus 446
"merc_to_natven":"""Idealization; thoughts of love.""",
"ven_to_natmerc":"""Romanticizing; thoughts of love.""",
"sun_merc/ven":"""Awareness of things beautiful; the arts; sunny disposition.""",
"moon_merc/ven":"""The emotions gain creative expression.""",
"mars_merc/ven":"""Alerting the passions; making strong, emotional statements; creativity.""",
"jup_merc/ven":"""Expansive idealization; perhaps religiousness; aesthetics; publishing; artistic achievement.""",
"sat_merc/ven":"""Serious attitude toward life; maturation; trimming down ideals
to be more practical; adjusting to realism.""",
"ura_merc/ven":"""Intensification of innovation; the spontaneous idea of feelings
becoming dominant; extraordinary communication.""",
"nep_merc/ven":"""Fantasy; seeing through a special dimension; spiritual
thoughts; deluding oneself about reality.""",
"plu_merc/ven":"""Highly focused aesthetics, argumentative position, or
expectations; the sense of mission; the successful "hard sell.""",
"nod_merc/ven":"""Sociability; relationship to the arts.""",
"asc_merc/ven":"""Pleasantness; being well-mannered; appreciated by others.""",
"mc_merc/ven":"""Possibly a profession in the arts; the profit from things creative;
acknowledging things beautiful or ideal.""",

#################################################################

#Mercury and Mars 447
"merc_to_natmars":"""Nervous drive.""",
"mars_to_natmerc":"""Energized thinking; making plans.""",
"sun_merc/mars":"""Putting one's foot down; making a point strongly; standing up
for one's position; enjoying a good argument; quick decisions.""",
"moon_merc/mars":"""Emotions are added to the issue at hand; arguments get an extra
level of meaning; one needs to be heard.""",
"ven_merc/mars":"""Arguments about love; excited plans about romance;
creative inspiration; insight.""",
"jup_merc/mars":"""Constructive thinking; sound judgment; knowing how to "sell"
an idea with enthusiasm.""",
"sat_merc/mars":"""Concentration; focused thought; efficiency and practicality;
knowing how to close the sale; knowing how to wound.""",
"ura_merc/mars":"""Tremendous excitability; thinking and planning on the run;
potentially rash judgment; losing self-control.""",
"nep_merc/mars":"""Vagaries; deception; not telling all; avoiding key points; intrigue;
fantasy channeled into creativity.""",
"plu_merc/mars":"""Criticism with a passion; knowing just what's wrong with the
world; involved in big arguments.""",
"nod_merc/mars":"""Discussions with others; easily argumentative.""",
"asc_merc/mars":"""Being seen as a talker; known to be impulsive.""",
"mc_merc/mars":"""Bravura; the champion salesperson; ready to win the fight.""",

##############################################################

#Mercury and Jupiter 448
"merc_to_natjup":"""Good common sense; writing, publishing; traveling.""",
"jup_to_natmerc":"""Intellect; thoughts about the spirit; legal issues; travel.""",
"sun_merc/jup":"""Success with the intellect; creative ideas are born; solutions are
illuminated.""",
"moon_merc/jup":"""Emotions inspire impressive ideas and welcomed solutions.""",
"ven_merc/jup":"""Idealized thinking; appreciation of one's world; thoughts and
plans for romance; a lovely vacation.""",
"mars_merc/jup":"""Energetic opinionation is well-accepted; making one's point
effectively.""",
"sat_merc/jup":"""Sober decisions; rational thought; withdrawing from disputes to avoid a fight; the lonely stand.""",
"ura_merc/jup":"""Excited presentation of ideas; curiosity about new things; sudden
inspiration; effective advertising.""",
"nep_merc/jup":"""Inspiration; beguiling fantasy; magnetism; losing the focus of an issue; lack of realism.""",
"plu_merc/jup":"""The powerful salesperson; the big proposal; dramatic persuasion.""",
"nod_merc/jup":"""Sociability; the exchange of thoughts with others; meetings.""",
"asc_merc/jup":"""Acceptance of one's well-organized thinking; successful teamwork.""",
"mc_merc/jup":"""Optimistic hope; looking for the best side of things to come
about; successful planning.""",

#######################################################################

#Mercury and Saturn 449
"merc_to_natsat":"""Hard work; analysis.""",
"sat_to_natmerc":"""Wisdom through duress; maturation through depression; the
sense of heavy responsibility.""",
"sun_merc/sat":"""Making a go of it; getting down to work; discipline paying off;
knowing what's got to be done.""",
"moon_merc/sat":"""Emotional quandary; emotional indecision because of fear of
losing; frustration; taxing learning process.""",
"ven_merc/sat":"""Frustration in romance; fickleness; needing reassurance.""",
"mars_merc/sat":"""Risking everything to make one's point; turning drive into
tyranny; arguments; no compromise.""",
"jup_merc/sat":"""Logic; reasoning; success through concentration and industry.""",
"ura_merc/sat":"""Great tension between the old way of thinking about things
and a new way; anxiety about change of the status quo; quick
decisions.""",
"nep_merc/sat":"""Depression; a sad spirit looking for a ray of hope.""",
"plu_merc/sat":"""Contemplating loss; fearing wipe-out; abandonment; feeling
resourceless.""",
"nod_merc/sat":"""Making contact with hard-working people who can be helpful.""",
"asc_merc/sat":"""Tendency to be aloof; backing off from responsibilities.""",
"mc_merc/sat":"""The heavy thinker; mind over matter; winning through
planning.""",

########################################################################

#Mercury and Uranus 450
"merc_to_natura":"""Impulsive action; provocative ideas; inspiration.""",
"ura_to_natmerc":"""Intensification of the nervous system; acuteness of thought;
sharpness; speed, sudden travel plans.""",
"sun_merc/ura":"""Ready-to-go; temperament is well-received; "up to speed"; able
to create the surprising move.""",
"moon_merc/ura":"""Emotional excitability; quick mood changes; valid instincts
about the situation.""",
"ven_merc/ura":"""A sense of artistry; the tendency to love spontaneously.""",
"mars_merc/ura":"""Nervous drive finds the mark and usually can pay off; the
instincts of a fighter hitting home; courage.""",
"jup_merc/ura":"""Impressive presentation of ideas; successful solutions spring
to mind.""",
"sat_merc/ura":"""Nervous antipathy toward any state of tension or frustration;
tendency to intolerance; trying always for quick extrication.""",
"nep_merc/ura":"""The higher levels of the mind; inspiration; psychic feelings
brought into focus; magical persuasiveness; deductive analysis.""",
"plu_merc/ura":"""Tremendous power for work, action, leadership; getting the
biggest job done in a commanding way.""",
"nod_merc/ura":"""Creative interchange with others; quick conferences.""",
"asc_merc/ura":"""Accident-prone through fast action or recklessness.""",
"mc_merc/ura":"""The inventor; success with all-around resourcefulness.""",

##########################################################################

#Mercury and Neptune 451
"merc_to_natnep":"""Thinking about what to feel; alert imagination; special
awarenesses.""",
"nep_to_natmerc":"""Feeling what to think; fantasy; special awarenesses.""",
"sun_merc/nep":"""Creativity; successful imaginative conceptualization; possibly
allowing oneself to be deceived.""",
"moon_merc/nep":"""Emotional sensitivity; possible paranormal awarenesses; personal
impressions dominate the thinking process.""",
"ven_merc/nep":"""Sensual thoughts; rapture; expecting a great deal ofpersonal
attention; demanding in love; impractical expectations; artistic
expression.""",
"mars_merc/nep":"""Putting imagination to work; inspired planning pays off.""",
"jup_merc/nep":"""Expansive fantasy; the large picture becomes personalized;
dramatic hopefulness; inspiration in the arts.""",
"sat_merc/nep":"""A gloomy reaction to real or imagined circumstances; looking
at the down side of things, which may not be valid.""",
"ura_merc/nep":"""Sudden new ideas; inspiration; going "far out"; individual
participation in the arts.""",
"plu_merc/nep":"""Instincts supporting the power drive.""",
"nod_merc/nep":"""Creative contact with others.""",
"asc_merc/nep":"""Potential overreaction to others; being exploited.""",
"mc_merc/nep":"""Spiritual awareness; living among the clouds with or without
practical orientation.""",

#########################################################################

#Mercury and Pluto 452
"merc_to_natplu":"""The ability to persuade; communicating new perspectives.""",
"plu_to_natmerc":"""The ability to persuade; demanding new perspectives.""",
"sun_merc/plu":"""The need for recognition; championing an idea or attitude that
prevails; communication skill.""",
"moon_merc/plu":"""Emotional communication power.""",
"ven_merc/plu":"""Artistic communication power; advertising; promotions of any
kind; "up front" sexual expression.""",
"mars_merc/plu":"""The ability to grasp a situation quickly, right or wrong, and take
action confidently and persuasively; attacking the issue without
reservation.""",
"jup_merc/plu":"""Teaching lessons; gaining a good reputation; publicity;
persuasion brings success.""",
"sat_merc/plu":"""Insistence of a point ofview; unrelenting demands; driven by
fear of failure; needing control.""",
"ura_merc/plu":"""The bright idea saves the day; extreme self-confidence; ready
to chart new territory.""",
"nep_merc/plu":"""Overdoing issues drains energy and wears out one's welcome.""",
"nod_merc/plu":"""Being recognized by others for persuasion and communication
skills.""",
"asc_merc/plu":"""Exercising influence.""",
"mc_merc/plu":"""Resourcefulness; great perception of any situation; leadership.""",

#########################################################################

#Mercury and Lunar Node 453
"merc_to_natnod":"""Exchanging ideas with others.""",
"nod_to_natmerc":"""Meeting others to exchange ideas.""",
"sun_merc/nod":"""Putting together a philosophy of life.""",
"moon_merc/nod":""" Sharing emotional thoughts with others.""",
"ven_merc/nod":"""Socialization; sharing affection with others; kindness.""",
"mars_merc/nod":"""Making things happen in group sharing.""",
"jup_merc/nod":"""Teaching; communication; philosophizing; partnership.""",
"sat_merc/nod":"""Reticence about sharing one's point ofview with others; perhaps
too much self-control or modesty.""",
"ura_merc/nod":"""Stimulating ideas shared; sudden business contacts; selfaggrandizement
that disturbs relationships.""",
"nep_merc/nod":"""Confusion about how to fit into the group.""",
"plu_merc/nod":"""The thrust of intelligence; lording it over others.""",
"asc_merc/nod":"""Making contacts is easy and pays off.""",
"mc_merc/nod":"""Placed in the forefront in social and business circles.""",

######################################################################

#Mercury and Ascendant 454
"merc_to_natasc":"""Social attitude becomes important""",
"asc_to_natmerc":"""What one thinks is "on the line"; open to evaluation.""",
"sun_merc/asc":"""Putting together a philosophy of life.""",
"moon_merc/asc":"""Projection of emotions to others.""",
"ven_merc/asc":"""Projection of feelings about love, intimacy, and the arts.""",
"mars_merc/asc":"""Negotiating with others; deciding on the best course of action
in collaboration with advisors.""",
"jup_merc/asc":"""Teaching; successful meetings; sharing ideas easily.""",
"sat_merc/asc":"""Adopting a strategic reserve in expression; withdrawing from a
social circle; protecting one's position.""",
"ura_merc/asc":"""Impetuous opinionation can irk others; being critical.""",
"nep_merc/asc":"""Not knowing quite what to think about something or someone;
openness to deception.""",
"plu_merc/asc":"""Becoming prominent and influential; putting one's personal
stamp on something.""",
"nod_merc/asc":"""Easy interchange with others.""",
"mc_merc/asc":"""Baring one's soul; taking one's stand; communicating without
fear.""",

###################################################################

#Mercury and Midheaven 455
"merc_to_natmc":"""Following one's way of thinking to the hilt; changes as a result.""",
"mc_to_natmerc":"""Having one's point ofview clarified or recognized.""",
"sun_merc/mc":"""Feeling confident about one's life philosophy; further change.""",
"moon_merc/mc":"""Feelings get expressed through a sense of Tightness and usually
are effective.""",
"ven_merc/mc":"""Thinking about love and relationships and feeling "right.""",
"mars_merc/mc":"""Making a decision about where one stands, usually with regard
to the profession or one's social position.""",
"jup_merc/mc":"""arge thoughts are easy to come by and are easily communicated
for success; almost a "can't lose" position; teaching, publishing;
, traveling for gain; philosophizing.""",
"sat_merc/mc":"""One's point ofview comes under scrutiny by authority figures.""",
"ura_merc/mc":"""Formulating new objectives; making a sensation; throwing
caution to the winds because of great confidence; nerve.""",
"nep_merc/mc":""" Self-absorbed thinking may lose the track on the public course.""",
"plu_merc/mc":""" major turning point is possible; the power picture is clear;
persuasion dominates.""",
"nod_merc/mc":"""pen interaction with others; telling the truth.""",
"asc_merc/mc":"""elf-absorption; losing contact with others; change brewing.""",

######################################################################

#Venus and Mars 456
"ven_to_natmars":"""Feelings for love; romance; sexual relationship; creativity in
the arts.""",
"mars_to_natven":"""Passion; impulsive sexual drive; excitement.""",
"sun_ven/mars":""" Potential marriage; physical attraction; opportunity in the arts;
conception.""",
"moon_ven/mars":""" Emotional impulses; maternal feelings; fulfillment through the
arts.""",
"merc_ven/mars":""" Physicality, love, and togetherness influencing the mental
outlook; writing about love.""",
"jup_ven/mars":""" Success in the arts and/or in plans to make relationships, attract
love, marry, have children.""",
"sat_ven/mars":""" The sense of being controlled in love matters, of losing freedom;
inhibitions; possible relationship with someone of conspicuous
age difference; renunciation.""",
"ura_ven/mars":""" Intense passion; high nervous involvement with things sexual;
sexual experimentation; dangerous liaison.""",
"nep_ven/mars":""" Reveling in desire; spiritual bonds; rationalization of passionate
attractions; self-sacrifice to another; being taken advantage of.""",
"plu_ven/mars":""" Powerful sexual drive; the conquest.""",
"nod_ven/mars":""" Attractiveness among others.""",
"asc_ven/mars":""" Showing love easily, with few conditions.""",
"mc_ven/mars":""" Intense relationship; desire for marriage or the actual event;
giving birth.""",

#################################################################

#Venus and Jupiter 457
"ven_to_natjup":"""Happiness in love; success; humanism; birthing.""",
"jup_to_natven":"""Success in love; artistic success; philanthropy; birthing.""",
"sun_ven/jup":""" Being popular, successful, particularly well-appreciated;
advancement in life; goodwill.""",
"moon_ven/jup":""" Charm; good nature; pleasant circumstances.""",
"merc_ven/jup":""" Happy thoughts; good humor; writing beautifully;
communicating with grace.""",
"mars_ven/jup":"""Preoccupation with opportunity; trying to make things happen
successfully; stirred up feelings; a good time.""",
 "sat_ven/jup":""" Realism is introduced to expansive hopes; possible coming down
to earth with a thud; caution; loss of faith.""",
 "ura_ven/jup":""" Sudden turn of events to joy and success; exhilaration.""",
 "nep_ven/jup":"""A loss of focus in love relationship; a change of direction for
no clear reason; being taken advantage of, deceived.""",
"plu_ven/jup":"""Publicity; popularity; the world view; unbounded enthusiasm.""",
"nod_ven/jup":"""Unselfishness; sharing.""",
"asc_ven/jup":"""A bright disposition; good cheer.""",
"mc_ven/jup":"""Wonderment at the feelings of love and/or success.""",

########################################################################

#Venus and Saturn 458
"ven_to_natsat":"""Grace given to ambition; the arts introduced to the life; the hurt
of love lost.""",
"sat_to_natven":"""Suppression oflove feelings; relationship with someone of
conspicuous age difference; learning trust in romance; trying
to understand peacefulness and calm.""",
"sun_ven/sat":"""Possible trouble in relationship; a difference in objectives; lack
ofsatisfaction; conservatism.""",
"moon_ven/sat":"""Emotional hurt, probably from loneliness or feeling
unimportant.""",
"merc_ven/sat":"""hinking about ways to feel fulfilled, to improve relationship,
to feel wanted; preoccupation; searching for the ideal.""",
"mars_ven/sat":"""Driving a wedge into relationship harmony; wanting more than
is there; fearing competition; disputes; possible separation.""",
"jup_ven/sat":"""Learning respect for the status quo; keeping to oneself.""",
"ura_ven/sat":"""Tension in relationship; jealousies; split-off affairs; boredom with
the past; arguments; possible separation.""",
"nep_ven/sat":"""Pretense in relationships; thinking the grass is greener
elsewhere; dreaminess deceives; possible separation.""",
"plu_ven/sat":"""Unusually strong tensions toward separation; wasting emotions.""",
"nod_ven/sat":"""Contacts with similar souls on the downside of life; needing sympathy.""",
"asc_ven/sat":"""Hiding one's light; withdrawing; fear ofnot being accepted.""",
"mc_ven/sat":"""Feeling unimportant; never successful enough.""",

#######################################################################

#Venus and Uranus 459
"ven_to_natura":"""Grace added to individuality; being appreciated, desired.""",
"ura_to_natven":"""Intensification of love desires and emotional excitement.""",
"sun_ven/ura":"""Love adventures; ready-to-go; proud of excitability.""",
"moon_ven/ura":"""Sudden excitement in fulfillment of one's needs in love, in sex,
in the arts; new ideas for a new future.""",
"merc_ven/ura":"""Sudden ideas about seeking out love adventure, sex; ready ideas
to solve problems innovatively, aesthetically.""",
"mars_ven/ura":"""Strong excitability in love; creative activity.""",
"jup_ven/ura":"""Expansive artistic ideas; appreciation of the arts; an adventurous
vacation.""",
"sat_ven/ura":"""Strategic controls are applied to the passionate nature; coming
down to earth.""",
"nep_ven/ura":"""Seduction; off-the-norm in sexual experience and fantasy;
relationship problems that are not easily defined and threaten
togetherness.""",
"plu_ven/ura":"""Fated attraction; enormous thrust of love needs and activity;
potential notoriety; possible exhibitionism.""",
"nod_ven/ura":"""Intense feelings seek out the same in others.""",
"asc_ven/ura":"""A projection of sexiness; artistic temperament.""",
"mc_ven/ura":"""Getting involved with someone quickly; an affair breaking open
to public view; success in artistic endeavors.""",

################################################################################

#Venus and Neptune 460
"ven_to_natnep":"""Love in a swoon; erotic imaginings; artistic ideas.""",
"nep_to_natven":"""Potential delusion in love; feeling unrequited; creative outlets.""",
"sun_ven/nep":"""Falling in love with love; secretiveness.""",
"moon_ven/nep":"""A dreamy emotional projection; impracticality.""",
"merc_ven/nep":"""Sympathy for others; artistic creativity; idealization.""",
"mars_ven/ura":"""Sexual drive has difficulty being fulfilled; there is magnetic
attractiveness but trouble settling down; easy self-delusion.""",
"jup_ven/nep":"""Romantic reverie; luxury consciousness; keeping up a good
front.""",
"sat_ven/nep":"""Fear oflosing the dream; a new look at realism is needed.""",
"ura_ven/nep":"""Intensified fantasy setting up impractical expectations; going too
far; susceptibility to exploitation through ego aggrandizement.""",
"plu_ven/nep":"""Extremely emotional; sexual needs pack a primal punch.""",
"nod_ven/nep":"""Relationships become unclear in their value structure.""",
"asc_ven/nep":"""Possibly a libertine image; reveling in love ideals.""",
"mc_ven/nep":"""Losing oneself in illusion; profiting through artistic endeavors,
creativity.""",

#############################################################################

#Venus and Pluto 461
"ven_to_natplu":"""Grace is brought to power; improved acceptance for the
indomitable.""",
"plu_to_natven":"""Intensification oflove desires; affairs; compulsiveness;
wasting emotions.""",
"sun_ven/plu":"""Creative thrusts in love, in the arts, and in general lifestyle are
illuminated conspicuously but nonthreateningly.""",
"moon_ven/plu":"""Enormous feeling of emotions from the depths of being.""",
"merc_ven/plu":"""Thinking about sexual relationships; artistic creativity.""",
"mars_ven/plu":"""The sex drive dominates expression; temperamental
emotionalism.""",
"jup_ven/plu":"""Creativity; publicity; sex adventures on vacation; problems in the
courts, possibly involving revenge.""",
"sat_ven/plu":"""The fear of losing love; the sense of tragedy.""",
"ura_ven/plu":"""Immediate love impulse; experiences off-the-beaten-track.""",
"nep_ven/plu":"""A love narcosis; possible instability in relationships.""",
"nod_ven/plu":"""Meeting people seems to present a gamble instead of security.""",
"asc_ven/plu":"""Fascinating personality attracts others.""",
"mc_ven/plu":"""Artistic success; love affairs brought out into the open; fated
union.""",

###########################################################################

#Venus and Lunar Node 462
"ven_to_natnod":"""Nice meeting with someone; romantic contact.""",
"nod_to_natven":"""Contact with someone or an event in the arts; cultural
get-togethers; romance; emotional meetings.""",
"sun_ven/nod":"""Politeness; sociability; geniality; others coming to one's
assistance.""",
"moon_ven/nod":"""Showing one's feelings.""",
"merc_ven/nod":"""Communication about romance or artistic matters to others.""",
"mars_ven/nod":"""Making sexy contact with someone; making an important
romantic date.""",
"jup_ven/nod":"""Enjoying someone's company enormously; entertainment.""",
"sat_ven/nod":"""Being brought up short in a situation that was potentially
emotionally rewarding; shyness; withdrawal.""",
"ura_ven/nod":"""Intense, sudden attraction to someone; quick liaison; making
friends with someone out of the ordinary.""",
"nep_ven/nod":"""Idealizing someone; making promises that are hard to keep;
indulgent with love.""",
"plu_ven/nod":"""Romantic contact that may be extremely strong and lasting.""",
"asc_ven/nod":"""Affectionate nature; cordiality; popularity.""",
"mc_ven/nod":"""Being known for one's art or appreciation of things cultural;
significant romantic fulfillment.""",

##########################################################################

#Venus and Ascendant 463
"ven_to_natasc":"""Niceness; being appreciated.""",
"asc_to_natven":"""Niceness; being appreciated.""",
"sun_ven/asc":"""A sense of all that is lovely; showing oneself at one's best in
terms of appearance.""",
"moon_ven/asc":"""The show of emotions; affections shown to others.""",
"merc_ven/asc":"""Sociability; entertaining nature; telling stories.""",
"mars_ven/asc":"""Using one's charm or sexiness to make something happen.""",
"jup_ven/asc":"""Enthusiasm galore; a show of luxury.""",
"sat_ven/asc":"""Tightening up the budget; pulling back the affections; being
known as frugal, tight.""",
"ura_ven/asc":"""Intense flair; attractiveness to others; one's sense of individual
style.""",
"nep_ven/asc":"""Fooling oneself about personal popularity or attractiveness;
sadness about romantic loss.""",
"plu_ven/asc":"""Extreme show of self-awareness, probably in terms ofstyle, flair,
beauty, or arts appreciation; clothing; gender pride.""",
"nod_ven/asc":"""Being sweet, interested in others.""",
"mc_ven/asc":"""A sense of beauty; a recognized "romantic.""",

##############################################################################

#Venus and Midheaven 464
"ven_to_natmc":"""Falling in love; reinforcing a deep relationship; peace, kind
support of others.""",
"mc_to_natven":"""Falling in love; reinforcing a deep relationship; forwarding
a career in the arts or other metier; getting a raise.""",
"sun_ven/mc":"""Being very strongly aware of oneself; confident sense of
attractiveness; success.""",
"moon_ven/mc":"""Feelings about romance; relating to others deeply; being valued
for one's work; recognition for a job well done.""",
"merc_ven/mc":"""Artistic ideas; beautiful communications for profit; working as
a writer or some other kind of artist.""",
"mars_ven/mc":"""Impulsive expression of creativity; showing joie de vivre.""",
"jup_ven/mc":"""Philanthropy; giving love; enthusiasm; happiness; success.""",
"sat_ven/mc":"""Ambition focused in the arts; controlling the love urge; loss
of relationship; being frugal; facing a cutback of some kind
professionally.""",
"ura_ven/mc":"""Excitability in love; new ideas on the job, perhaps "zany";
openness about relationships.""",
"nep_ven/mc":"""Imagination; artistic achievement; losing touch with the most
satisfactory ways of relating and loving.""",
"plu_ven/mc":"""Tremendous focus on an artistic career; cultural exposure;
publicity; emotional expression; love relationship.""",
"nod_ven/mc":"""Seen as an affectionate person.""",
"asc_ven/mc":"""Being at harmony.""",

###################################################################################
#Mars and Jupiter 465
"mars_to_natjup":"""A fortunate course of action; clearing the air; successful
creative activity.""",
"jup_to_natmars":"""Tremendous energy; enterprise; making things happen in a big
way; "making waves" effectively.""",
"sun_mars/jup":"""Success; organizational talent; leadership.""",
"moon_mars/jup":"""Opinionation; emotional, "gut" feelings guide action; pride.""",
"merc_mars/jup":"""Planning capability; publishing; showing the fruits ofone's
labors and creativity.""",
"ven_mars/jup":"""Success; romantic expression; creative activity.""",
"sat_mars/jup":"""Struggling with impulse; having to toe the line; pulling in one's
sails.""",
"ura_mars/jup":"""Explosive expression; breaking loose; domination.""",
"nep_mars/jup":"""Imagining success; letting reality get away; being near a mistaken
course of action.""",
"plu_mars/jup":"""Extreme creative self-application; enterprise; demanding success
from the environment; the really big picture.""",
"nod_mars/jup":"""Cooperation with others; getting their support.""",
"asc_mars/jup":"""Being respected as a doer; getting things done.""",
"mc_mars/jup":"""The excitement of being "on top"; opportunity for success.""",

####################################################################################

#Mars and Saturn 466
"mars_to_natsat":"""The clash of hot and cold, action and control; stalemate""",
"sat_to_natmars":"""Putting a damper on things;ups and downs; indecision; failing.""",
"sun_mars/sat":"""Possible threat to the body or health; breaking down under
stress and strain; the sense of loss; eking it out.""",
"moon_mars/sat":"""Moodiness; possible depression; feelings about losing
something.""",
"merc_mars/sat":"""Thoughts don't know where to go; any alternative seems
inappropriate; indecision; separating from issues.""",
"ven_mars/sat":"""Emotions are cooled; frustration; feeling loveless or unloved,
unsupported; passionately trying to make something work.""",
"jup_mars/sat":"""Tremendous concentration; fast production of fine work;
wisdom; weighing all matters and making a pronouncement.""",
"ura_mars/sat":"""Intense drive; breaking loose; gaining independence through
struggle; sudden accident.""",
"nep_mars/sat":"""Confusion; feeling threatened; self-torment about identity.""",
"plu_mars/sat":"""The need to take control; forcing an issue; strong anger.""",
"nod_mars/sat":"""Unsatisfactory liaisons.""",
"asc_mars/sat":"""truggling for every step of advance; possible health threat.""",
"mc_mars/sat":"""Overcoming obstacles stoicly; silent pride.""",

##############################################################################

#Mars and Uranus 467
"mars_to_natura":"""Intense self-awareness; tremendous urge to action; test of
nerves.""",
"ura_to_natmars":"""Sudden application of great energy; dominant will.""",
"sun_mars/ura":"""Making something happen; sudden new circumstances; strong
sense of self-confidence; feeling invulnerable.""",
"moon_mars/ura":""" Intensification of the emotions; the strong need for love; a desire
for recognition.""",
"merc_mars/ura":"""Nervousness; planning independent action; strategy.""",
"ven_mars/ura":"""Passionate excitability; increased romantic activity.""",
"jup_mars/ura":"""Planning one's future, one's new position in life; looking to
rewards; planning the course of action.""",
"sat_mars/ura":"""A clash between controls and the freest spirit; potential battles
and separations; controls can not be tolerated.""",
"nep_mars/ura":"""Inspiration for vigorous selfhood; a dream leading the action;
something coming out of "nowhere"; a loss of the usual orientation.""",
"plu_mars/ura":"""Force; a "Higher Power"; intervention of the big shock.""",
"nod_mars/ura":"""Hyperexcitability with others.""",
"asc_mars/ura":"""Accident-prone temperament and personality.""",
"mc_mars/ura":"""Putting a gun to someone's head"; getting one's way; the sense
of "either/or"; taking drastic measures.""",

##############################################################################

#Mars and Neptune 468
"mars_to_natnep":"""Inspiration; imagination made applicable; personal magnetism.""",
"nep_to_natmars":"""Change of course of action due to dissatisfaction; going to
where the grass seems greener; losing focus.""",
"sun_mars/nep":"""New plans are illuminated; situational changes.""",
"moon_mars/nep":"""Emotional sensitivity; indecision; feeling off course.""",
"merc_mars/nep":"""Imagination may lose anchor; difficulty coping.""",
"ven_mars/nep":"""Erotic musings; differently directed sensuality.""",
"jup_mars/nep":"""Enjoying the cloud's silver lining; a break in the knick of time.""",
"sat_mars/nep":"""Being taken advantage of; reticence; the sense of futility;
persevering in spite of fear.""",
"ura_mars/nep":"""Energetically following one's personal dream; reaching for
'pie-in-the-sky.'""",
"plu_mars/nep":"""Apparently irresponsible attitude; selfish pursuit of one's
objectives; devil-may-care attitude.""",
"nod_mars/nep":"""Sense of suspicion in associations.""",
"asc_mars/nep":"""Giving off a magnetic or off-the-norm emanation; being
different.""",
"mc_mars/nep":"""Apparent loss of ego-consciousness; one's own world prevails;
losing contact defensively; rebuilding the inner spirit.""",

#####################################################################

#Mars and Pluto 469
"mars_to_natplu":"""Extreme force; persuasion; control; brutality; excessive effort.""",
"plu_to_natmars":"""Extreme force; persuasion; control; brutality; excessive effort.""",
"sun_mars/plu":"""Hard work; passionate attack to achieve an objective; accident
potential; intervention ofsome undeniable force or authority;
upset ofplans that is unredeemable.""",
"moon_mars/plu":"""Daring; taking a chance; playing the powerful hunch; self-belief;
publicity.""",
"merc_mars/plu":"""Seeing is achieving; tenacious pursuit ofplans; publicity; effective
salesmanship.""",
"ven_mars/plu":"""Passionate disposition; sexual adventure or even danger; an
affair.""",
"jup_mars/plu":"""Unusual success; the big plan comes into focus; the energy and
resources are available to make things happen; publicity.""",
"sat_mars/plu":"""Hard, hard work; extraordinary discipline is needed and usually
prevails.""",
"ura_mars/plu":"""Tremendous energy; dangerous sense of attack; a chip on one's
shoulder; fight first, talk later.""",
"nep_mars/plu":"""Cunning strategies; subterfuge; plotting rebellion.""",
"nod_mars/plu":"""Working with others to change the world.""",
"asc_mars/plu":"""Showing the hero image; the fighter who dares the impossible;
aggression.""",
"mc_mars/plu":"""Confidence; ambition; dealing with might on either side of any
issue; major job maneuver.""",

################################################################################

#Mars and Lunar 470
"mars_to_natnod":"""Getting along with others; combined efforts pay off.""",
"nod_to_natmars":"""meeting others to get the work done.""",
"sun_mars/nod":"""Good cooperation dynamics; good blending of energies with
others.""",
"moon_mars/nod":"""Emotional attitude toward others shows and leads activity.""",
"merc_mars/nod":"""Plans to collaborate, cooperate, share; promotion through
partnerships; community-minded; salesmanship; publicity.""",
"ven_mars/nod":"""Getting together affectionately, passionately.""",
"jup_mars/nod":"""Successful teamwork; lots of enthusiasm; taking a trip with
someone; planning togetherness for the long term.""",
"sat_mars/nod":"""Something or someone always stepping on one's shadow;
difficulty making the sale; withdrawing because of poor
reception; one's ardor is squashed; looking for more amenable
associations.""",
"ura_mars/nod":"""Organizing others; getting people stirred up; sharing
excitement; sudden events that affect lots ofpeople.""",
"nep_mars/nod":"""Self-absorption within a group; charismatic or off-putting.""",
"plu_mars/nod":"""Others must "get on the train" or get left behind!""",
"asc_mars/nod":"""Easy camaraderie.""",
"mc_mars/nod":"""Excellent teamwork; partnership values important.""",

#############################################################################

#Mars and Ascendant 471
"mars_to_natasc":"""AS The fighting spirit.""",
"asc_to_natmars":"""Robustness.""",
"sun_mars/asc":"""Getting involved with arguments or operating in an inhospitable
milieu; having to adjust things forcefully.""",
"moon_mars/asc":"""Emotional temperament easily shown to others.""",
"merc_mars/asc":"""A sharp tongue; verbal disputes; angry letters; telling someone
off; intolerance.""",
"ven_mars/asc":"""Passion; love and sex are first concerns in relationships; the arts
become important for personal expression.""",
"jup_mars/asc":"""Enthusiasm and leadership; harmonious public outreach.""",
"sat_mars/asc":"""Anxiety comes from feeling controlled somehow; frustration
and rebellion; others don't cooperate as they should.""",
"ura_mars/asc":"""Testiness; argumentation; temper; picking a fight; inclination
to intimidate others; ego aggrandizement.""",
"nep_mars/asc":"""Magnetism, charisma; out of the mainstream; others may not
understand; withdrawal as an option.""",
"plu_mars/asc":"""Premature action; intensity; "bitchiness"; easily provoked to
anger.""",
"nod_mars/asc":"""Excellent teamwork.""",
"mc_mars/asc":"""Work fulfillment with others.""",

#Mars and Midheaven 472
"mars_to_natmc":"""Ego awareness; action; fire; change of status.""",
"mc_to_natmars":"""Recognition; responsibility grows; change ofstatus.""",
"sun_mars/mc":"""The drive to be important; self-promotion.""",
"moon_mars/mc":"""Emotional excitability; impulsiveness; publicity; an emotional
appeal; changing status through emotional 'feel.'""",
"merc_mars/mc":"""Acting with vigor according to plan; important news or
strategically helpful information.""",
"ven_mars/mc":"""Social desires; sexual desires; romance on the job; selfpromotion.""",
"jup_mars/mc":"""Great success; promotion in professional status; energy and
opportunity.""",
"sat_mars/mc":"""The demand is to bring energies, plans, and enthusiasms into
line; elimination of the overdone or exaggerated.""",
"ura_mars/mc":"""The big push; the quick advance; winning right away; rashness;
argumentative; inflamed.""",
"nep_mars/mc":"""Creativity may be off the mark; discipline is needed to use one's
talents in the best way; diffusion needs focus.""",
"plu_mars/mc":"""Zeal, energy, promotion, publicity, power; the big picture.""",
"nod_mars/mc":"""Leadership qualities; success potential.""",
"asc_mars/mc":"""Confidence; projection of sureness and pizazz.""",

##############################################################################

#Jupiter and Saturn 473
"jup_to_natsat":"""Law and order; ambition given the go-ahead signal; patience
pays off; feeling tighter than right; dogmatic.""",
"sat_to_natjup":"""Control tempers zeal; opportunities are carefully evaluated;
success takes on long-term security; one has "made it happen";
strategy.""",
"sun_jup/sat":"""Taking destiny into one's own hands; major changes according
to plan; or, if nothing has been prepared, becoming gripped by
the status quo and having to make the best of things.""",
"moon_jup/sat":"""Emotional conviction; hypersensitive about one's ego position.""",
"merc_jup/sat":"""Studying one's philosophy of life; a long trip; speaking with
great maturity; studying hard; asking the right questions.""",
"ven_jup/sat":"""Maturation of romantic needs and projections; feeling a little
older than one's age; a touch of reserve.""",
"mars_jup/sat":"""Ambition emerges out of discontent; feeling unrewarded and
making a change; not wanting to toe the line.""",
"ura_jup/sat":"""Terribly upset with the status of things; forceful change of
direction, which can upset many dimensions of life.""",
"nep_jup/sat":"""Bewilderment; not knowing which "master" to follow;
loneliness.""",
"plu_jup/sat":"""Tremendous perseverance; dramatic thrust of self; control of
the situation; fearless; major change ofsituation.""",
"nod_jup/sat":"""Working well with others; being just with others.""",
"asc_jup/sat":"""Keeping properly in one's place; the tactician.""",
"mc_jup/sat":"""The philosopher; thinking with grandeur.""",

#############################################################################

#Jupiter and Uranus 474
"jup_to_natura":"""The big break; success or going one's independent way to
greener pastures.""",
"ura_to_natjup":"""The big break; boundless optimism.""",
"sun_jup/ura":"""Great success; the illumination of one's best position in any
situation, in life in general; individuality in full bloom.""",
"moon_jup/ura":"""Opportunity for major change; looking ahead to success.""",
"merc_jup/ura":"""Planning on success; confidence; a series of fortunate breaks.""",
"ven_jup/ura":"""Happy feelings about love, artistic things; fascination with being
a man or a woman; narcissism.""",
"mars_jup/ura":"""Drive and determination toward success; a love of individual
freedom; speculation; changing fortunes.""",
"sat_jup/ura":"""The introduction of patience and practicality to boundless selfprojection;
temperance over excess.""",
"nep_jup/ura":"""Inspiration; gain from the unexpected; strange conditions seem
to heighten individual awareness; a silver lining.""",
"plu_jup/ura":"""Tremendous drive to success; publicity; gains.""",
"nod_jup/ura":"""Individuality attracts enthusiasm and new friends.""",
"asc_jup/ura":"""Optimism and personal self-confidence; knowing the best will
happen; success; fortunate twists in the way things transpire.""",
"mc_jup/ura":"""Comfortably becoming known for who one is.""",

#################################################################################

#Jupiter and Neptune 475
"jup_to_natnep":"""Idealism; grand spirit; feeling quietly special; looking ahead
to nice times; self-indulgences; rumor and scandal.""",
"nep_to_natjup":"""Emphasis on things spiritual, philosophical, religious,
extrasensory; benevolence; self-indulgences; tricky legalisms.""",
"sun_jup/nep":"""Potentially misguided states; feeling the spirit; trying to capture
the essence of things; following a dream.""",
"moon_jup/nep":"""Dreaminess; an emotional swoon; going with the wind.""",
"merc_jup/nep":"""Active imagination; learning to communicate fancifully;
visualization; changing character; inspiration.""",
"ven_jup/nep":"""Eroticism; optimism in love.""",
"mars_jup/nep":"""Strong idealism; the need for practical focus.""",
"sat_jup/nep":"""Breakdown ofidealization; pessimism; possible self-delusion.""",
"ura_jup/nep":"""Charisma; intuitionally innovative; liking the shades.""",
"plu_jup/nep":"""Unreasonable plans; self-projection out of hand; major
adjustment oflife circumstances.""",
"nod_jup/nep":"""Dealing with others naively or simplistically.""",
"asc_jup/nep":"""Appearing to live in a world lighted by personal imagination
and an emotionally rationalized agenda.""",
"mc_jup/nep":"""A visionary; the potential for all kinds of self-indulgence.""",

#Jupiter and Pluto 476
"jup_to_natplu":"""Establishing new perspectives; feeling personal power and
resourcefulness; building the big picture; keeping in control of
things.""",
"plu_to_natjup":"""Tremendous optimism; a thrust for power; leadership.""",
"sun_jup/plu":"""Successful use of strong personality power; doing well with all
resources; keeping things in one's own grip.""",
"moon_jup/plu":"""Emotional conviction guides a new start; establishing one's new
position with a gut feeling.""",
"merc_jup/plu":"""Persuasion; influence; promotion of a cause.""",
"ven_jup/plu":"""Creativity; flair.""",
"mars_jup/plu":"""Leadership; publicity; organizing talent; applying controls to
suit one's particular purposes.""",
"sat_jup/plu":"""Adjusting the big picture to meet more with convention;
strategy becomes necessary.""",
"ura_jup/plu":"""Intense application of resources to establish a new perspective;
overturning the tables; getting back onto the track or finding
a better one.""",
"nep_jup/plu":"""Inclination to be deceptive; adjusting the data; omitting key
facts; working a situation into one's own format.""",
"nod_jup/plu":"""Working together with others for success.""",
"asc_jup/plu":"""Being known as an organizer and special achiever.""",
"mc_jup/plu":"""Hard-working attainment of power position.""",

#####################################################################################

#Jupiter and Lunar Node 477
"jup_to_natnod":"""Good relationships, profitable associations; 'connections.'""",
"nod_to_natjup":"""Meeting others; making profitable liaisons; "connections.""",
"sun_jup/nod":"""Feeling good about one's self in relation to others; building
confidence to support action.""",
"moon_jup/nod":"""An emotional and enthusiastic projection to others pays off.""",
"merc_jup/nod":"""Thinking about others' welfare; sharing success; appreciating
the complementation ofpartnership.""",
"ven_jup/nod":"""Pleasantness with others; a graceful image; caring.""",
"mars_jup/nod":"""Successful teamwork.""",
"sat_jup/nod":"""Working with others by the rules; getting things perfectly clear;
holding back in strategic reserve; slowing things down for safety;
maybe "missing the boat" through caution.""",
"ura_jup/nod":"""Entertaining image; inventive; enthusiastic; new associations.""",
"nep_jup/nod":"""Lack of clarity about the objectives of being or working
together; sharing the spirit with others but not much else,
especially in the way of grounding.""",
"plu_jup/nod":"""Strong personal projection of sociability; "collecting" wellknown
people.""",
"asc_jup/nod":"""Pleasantness with others.""",
"mc_jup/nod":"""Recognition for one's humanity and agreeableness.""",

##########################################################################

#Jupiter and Ascendant  478
"jup_to_natasc":"""Enthusiasm; harmony.""",
"asc_to_natjup":"""Enthusiasm; harmony.""",
"sun_jup/asc":"""Pleasantness with others; enthusiasm brought to the fore.""",
"moon_jup/asc":"""Largesse, kindness; a happy time.""",
"merc_jup/asc":"""Delight in social contact.""",
"ven_jup/asc":"""Affectionate relationship with others.""",
"mars_jup/asc":"""Easy, enthusiastic cooperation with others.""",
"sat_jup/asc":"""Appreciating the rules; maturity; comfortable with convention.""",
"ura_jup/asc":"""Optimism; enthusiasm; fortunate adjustment to one's status
saves the day.""",
"nep_jup/asc":"""Living with hope and speculation; dreaming; projecting the
niceness of things; not admitting the adverse.""",
"plu_jup/asc":"""Strong image; influential; leadership.""",
"node_jup/asc":"""Needing to be with other people for their support and
appreciation ofwho one is.""",
"mc_jup/asc":"""Being in the right place at the right time; successful positioning.""",

########################################################################

#Jupiter and Midheaven  479
"jup_to_natmc":"""Success, recognition, good fortune; sense ofpurpose.""",
"mc_to_natjup":"""Success; professional gains; internationalism; legalism.""",
"sun_jup/mc":"""Illumination of one's purpose in life; new opportunities;
recognition and success.""",
"moon_jup/mc":"""Fulfillment of personal needs to a high degree; recognition; a
deserved sense of importance.""",
"merc_jup/mc":"""Publishing; lots of ideas; voluble communication; plans that
prove successful.""",
"ven_jup/mc":"""Success; reward; artistic appreciation and achievement;
happiness; love relationship; engagement; marriage; birth.""",
"mars_jup/mc":"""Creating opportunities; making success happen; being inspired.""",
"sat_jup/mc":"""Cautious pursuit of opportunity; respect for the rules; longlasting
endeavors pay off with long-lasting rewards.""",
"ura_jup/mc":"""Great good luck with new enterprise; good fortune appears
suddenly.""",
"nep_jup/mc":"""Projecting the best of all worlds; needing anchor to avoid
disappointments; befuddlement; lack of realism.""",
"plu_jup/mc":"""Great gains; potential for extraordinary achievement and
recognition; publicity.""",
"node_jup/mc":"""Enthusiastic contacts with others.""",
"asc_jup/mc":"""Pleasant contact with others who support one's personal success.""",

################################################################################

#Saturn and Uranus 480
"sat_to_natura":"""Tension between the avant-garde and the conventional; the new
and the old; feeling controls; need to fight for gains.""",
"ura_to_natsat":"""Pep-up for ambition; exciting the status quo into new
development; a jolt to consider freedom; separation.""",
"sun_sat/ura":"""Tendency to rebel; egocentric drive against controls; separations
in order to find one's way.""",
"moon_sat/ura":"""Emotional courage emerges under duress; changes for freedom.""",
"mec_sat/ura":"""Demands on nervous energy; decisions to be made about doing
things a new way; necessary stages of rethinking.""",
"ven_sat/ura":"""Tensions in romantic life; hot and cold; off again, on again;
feeling personally limited.""",
"mars_sat/ura":"""Tremendous upheaval possible in rebellion, through calamity,
overexertion, or anxiety about how things will get on; challenges
leading to a fight.""",
"jup_sat/ura":"""Resolution of tensions comes rewardingly from without.""",
"nep_sat/ura":"""Breakdown under emotional pressure; new vision fighting to
be understood; sadness; feeling lost.""",
"plu_sat/ura":"""Tremendous fear ofloss; upheaval to protect assets; rebellion.""",
"nod_sat/ura":"""Too much combative energy to fit teamwork requirements easily.""",
"asc_sat/ura":"""The loner's position is established; indecision.""",
"mc_sat/ura":"""Break away from the old; recognition of one's thrust for
individuality or loss of self to the grip of controls.""",

#################################################################################

#Saturn and Neptune 481
"sat_to_natnep":"""under stress; denial.""",
"nep_to_natsat":"""Losing focus of ambition; depression; sense of being wronged.""",
"sun_sat/nep":"""Painstaking attention to hard work to fulfill plans; feeling alone
in the effort.""",
"moon_sat/nep":"""Emotional drain; feeling inhibited.""",
"merc_sat/nep":"""Pessimism; depression; slowness of mind; strangely nervous.""",
"ven_sat/nep":"""Deluded love feelings; inhibitions; diminished emotional
expression, sexual activity; unrequited love; longing for
attention; lack of popularity; appreciated more by senior people.""",
"mars_sat/nep":"""Diminution of energy; preoccupations that can't be explained;
lack of zest.""",
"jup_sat/nep":"""Very upset with the ways of the world; losing the will to fight.""",
"ura_sat/nep":"""Irritability; frustration.""",
"plu_sat/nep":"""Strong depression; feeling downtrodden; tremendous awareness
ofpotential for loss; fear.""",
"nod_sat/nep":"""Not getting along easily with others; withdrawal.""",
"asc_sat/nep":"""Being a loner; feeling confined; sense of being 'out of the
group.'""",
"mc_sat/nep":"""Peculiar loss of ambition; moodiness; giving up or capitulating
to demands of the environment totally.""",

#########################################################################

#Saturn and Pluto
"sat_to_natplu":"""The threat of loss in any area of life; potential self-destruction;
hard, hard work.""",
"plu_to_natsat":"""The threat of loss in any area of life; potential self-destruction;
hard, hard work.""",
"sun_sat/plu":"""Threat of loss; hard work; enforced change; separation; potential
ill health.""",
"moon_sat/plu":"""Emotional coldness; renunciation; giving up giving.""",
"merc_sat/plu":"""Depression; morbid thoughts; deep study; stark realism.""",
"ven_sat/plu":"""Troubled by the loss of love.""",
"mars_sat/plu":"""Fighting battles to keep life going; enormous undercurrent of
frustration; a gun with a cork in its barrel.""",
"jup_sat/plu":"""Trouble with authority; adoption of the austere; staying out
of trouble; trying to save what's left.""",
"ura_sat/plu":"""Brutal efforts to start a new order; an attack, regardless of
potential losses.""",
"nep_sat/plu":"""Being doubted; not being seen for who one is; unstable life
situation because of the inexplicable, because offear.""",
"nod_sat/plu":"""Suffering shared with others.""",
"asc_sat/plu":"""Sadness; mourning.""",
"mc_sat/plu":"""Hard, hard work to rise again from difficulty; major separation
as a last resort.""",

######################################################################################

#Saturn and Lunar Node 483
"sat_to_natlunarnod":"""Serious attitude in relation to others; aloneness.""",
"lunarnod_to_natsat":"""b Meetings of a serious nature; a lonely position.""",
"sun_sat/lunarnod":"""Setting oneself apart from others for defense or for prestige;
appearing self-contained.""",
"moon_sat/lunarnod":"""Appealing to senior persons; showing precocious maturity;
qualifying for responsibility.""",
"merc_sat/lunarnod":"""Thoughts that appeal to others because they are sound,
conservative, and respectful; strategy; news ofsadness.""",
"ven_sat/lunarnod":"""Difficulty expressing emotions to others; inhibitions; depression
in relationship.""",
"mars_sat/lunarnod":"""Difficult surrounding situations; looking for personal freedom;
confused motivation.""",
"jup_sat/lunarnod":"""The generation gap; rebellion; freeing oneself from stress.""",
"ura_sat/lunarnod":"""Upsetting the established way of doing things; going against
group expectations; separatist activities.""",
"nep_sat/lunarnod":"""Confusion in one's environment; confusing others about one's
personal stand; deception; fraud; lies.""",
"plu_sat/lunarnod":"""Sacrifice; loss through others; giving up the struggle.""",
"asc_sat/lunarnod":"""Pulling back; appearing alone; going away.""",
"mc_sat/lunarnod":"""Standing alone in life; mourning for others; little joy from
accomplishments.""",

###############################################################################


#Saturn and Ascendant 484
"sat_to_natasc":"""Controlled or inhibited personality; possible illness.""",
"asc_to_natsat":"""One's position of maturity, wisdom, control, and patience is
shown openly.""",
"sun_sat/asc":"""Taking responsibility squarely into one's life plan; strategizing
personal freedom; making something happen through hard
work; overtaxing body-health system.""",
"moon_sat/asc":"""Depression due to the environment; difficulty being accepted.""",
"merc_sat/asc":"""Others influencing how one thinks; wanting to be alone, to get
away from it all.""",
"ven_sat/asc":"""Inhibition of expression to others; sour disposition.""",
"mars_sat/asc":"""Getting mad at the status quo; trying to put things right;
struggling with inhibitions and control.""",
"jup_sat/asc":"""Being seen as "above it all"; c'est la vie! or one works very hard
to reestablish a new order that is reliable and predictable.""",
"ura_sat/asc":"""Upsets and disputes over change; demanding personal freedom.""",
"nep_sat/asc":"""Depressing and introverted life situations; arguments about
strange dimensions or obscure things; overmaking a point.""",
"plu_sat/asc":"""Violent upset; deep anguish; being put down by others.""",
"nod_sat/asc":"""Unpleasant circumstances with others.""",
"mc_sat/asc":"""Feeling like the victim; trying to justify one's position.""",

###############################################################################


#Saturn and Midheaven 485
"sat_to_natmc":"""Major change in the family or in the profession; possible death
concerns within the extended family circle; the father figure; an
extremely important time of life development.""",
"mc_to_natsat":"""Focus upon ambition; professional change; significant family
development; a major move.""",
"sun_sat/mc":"""Need to fight hard and having the capacity to do so.""",
"moon_sat/mc":"""Renunciation of one thing and the adoption of another to fulfill
needs better; an attack on private emotions.""",
"merc_sat/mc":"""Melancholy; separation thoughts; bad news; professional
decisions that are hard to make.""",
"ven_sat/mc":"""Improvement in job situation; dryness in relationships.""",
"mars_sat/mc":"""A battle in the job situation; tendency to give in, pull back, lose
ground; controls adopted.""",
"jup_sat/mc":"""Doing things right, the way they are expected to be done;
keeping things as they are; or changing things to how they
should be done for maximum security.""",
"ura_sat/mc":"""The great effort; intensity; a new way of doing things; sudden
crisis on the job or in the family; surprise.""",
"nep_sat/mc":"""A lack of clarity; one's position is vague; feeling fears.""",
"plu_sat/mc":"""Great demands; fear of loss; the grand struggle.""",
"nod_sat/mc":"""Potential on the job or in the family; major stroke of fate may
affect all development.""",
"asc_sat/mc":"""Working with others in compassion and serious understanding.""",

####################################################################################

#Uranus and Neptune 486
"ura_to_natnep":"""Exploring individuation through imagination; through
speculation; through creativity; possible use of underhanded
means (artfully rationalized) to do the job.""",
"nep_to_natura":"""Loss of ego focus is possible if socio-professional position
is unstable; spiritual world is awakened; amorphous states;
irritability.""",
"sun_ura/nep":"""Great creativity; ultrasensitive; impressionable; vaunted selfregard.""",
"moon_ura/nep":"""Emotional conviction, realistic or fanciful; the sense of being on
the right track to do one's best.""",
"merc_ura/nep":"""Aware of the metaphysical; the mind plays tricks; high curiosity;
perhaps needing a reorientation to common sense.""",
"ven_ura/nep":"""High sensitivity; fantasy life; reveling in love.""",
"mars_ura/nep":"""Applied creativity could be very strong; impatience; a nervous
feeling of foreboding.""",
"jup_ura/nep":"""Good luck coming out of nowhere; rejuvenation of the spirit.""",
"sat_ura/nep":"""A clash among ambitions and projections; need for recognition;
changes of direction; staying put causes depression and loss of
self-confidence.""",
"plu_ura/nep":"""The big picture commands a certain course of action, which
must be followed; very little option to do otherwise.""",
"nod_ura/nep":"""Meeting with people who care about one's future.""",
"asc_ura/nep":"""Wearing anxieties on one's sleeve; needing sympathy.""",
"mc_ura/nep":"""Supernatural concerns come into play; guidance is sought from
other realms or never-before-tapped sources.""",

######################################################################################

#Uranus and Pluto 487
"ura_to_natplu":"""Overturning the status quo; creating a whole new perspective for
ego recognition.""",
"plu_to_natura":"""Tremendous intensification of ego awareness; attainment of
great goals through great effort; upsets and tension enroute.""",
"sun_ura/plu":"""The urge for independence and freedom; great tension;
revolution.""",
"moon_ura/plu":"""Change through force; indomitable, emotional conviction.""",
"merc_ura/plu":"""Intense thought activity; new ideas, new plans, all for a new
personal perspective; forcing individuality into focus.""",
"ven_ura/plu":"""Creativity; a conquest for love or in the arts.""",
"mars_ura/plu":"""Enormous energy; fanaticism is possible; coercion.""",
"jup_ura/plu":"""Enormous success potential.""",
"sat_ura/plu":"""Egotism; tendency toward autocratic leadership; "my way is the
best way"; pressure from others; toppled from position.""",
"nep_ura/plu":"""Deep study of specialized subject; sympathetic understanding of
others; peculiar nervous state when excited.""",
"nod_ura/plu":"""Untiring colleague; teamwork paying off, but one's own ego is
put first in line.""",
"asc_ura/plu":"""Force active in one's environment.""",
"mc_ura/plu":"""Grand awareness ofwhat's going on; the opportunity to rise to
leadership.""",

###################################################################################

#Uranus and Lunar Node 488
"ura_to_natnod":"""Meetings with unusual people pay off; sudden relationships.""",
"nod _to_natura":"""Shared experiences are particularly rewarding.""",
"sun_ura/nod":"""High tension; a group taking action.""",
"moon_ura/nod":"""Excitability; a team taking a stand.""",
"merc_ura/nod":"""Excited thoughts shared with others; impetuousness.""",
"ven_ura/nod":"""Sudden attachments, romantic or just like-minded: the
camaraderie is what is important.""",
"mars_ura/nod":"""Tremendous energy and tension; having an axe to grind and
gaining support.""",
"jup_ura/nod":"""The big opportunity comes to those demanding it.""",
"sat_ura/nod":"""Difficulties encountered together with others; the acceptance of
controls by 'group vote.'""",
"nep_ura/nod":"""Meeting with people off the beaten path.""",
"plu_ura/nod":"""The strong need to be influential, persuasive; rocking the boat,
and people approving the motion.""",
"asc_ura/nod":"""Sudden new acquaintances.""",
"mc_ura/nod":"""Teamwork paying off; professional recognition.""",

#########################################################################

#Uranus and Ascendant 489
"ura_to_natasc":"""AS Major new start; high probability of geographic relocation.""",
"asc_to_natura":"""Showcase opportunity for individuality; "show off time.""",
"sun_ura/asc":"""Show of restlessness; anxiety about putting one's best foot
forward; hoping for success.""",
"moon_ura/asc":"""Emotionalism spills into view; needs sympathy, support, and
approval.""",
"merc_ura/asc":"""Nervous planning; fault finding; sharp witted; caustic.""",
"ven_ura/asc":"""Being sexy; showing oneself in exciting fashion; emphasizing
individual "new looks" of any kind.""",
"mars_ura/asc":"""Making things happen raucously; devil-may-care attitude.""",
"jup_ura/asc":"""Working feverishly to earn recognition.""",
"sat_ura/asc":"""The clash of controls and the avant-garde; indecision; airing
dilemmas.""",
"nep_ura/asc":"""Strange experiences may be revealed; emotions are shared;
a feeling of martyrdom can be exploited.""",
"plu_ura/asc":"""Force; commanding success.""",
"nod_ura/asc":"""Getting like-minded people on board.""",
"mc_ura/asc":"""Major change potential in job status, with the parents, or
through the spouse's job position or family.""",

#####################################################################################

#Uranus and Midheaven 490
"ura_to_natmc":"""An extraordinary time of life; probable reorganization of family
life in the early home; dramatic adjustment ofjob status as an
adult; change of profession possible; sudden change of direction
in practically every department oflife; individuality reigns;
geographic relocation.""",
"mc_to_natura":"""Brings the power of selfhood forward; assertion is recognized;
strong developmental tensions for job and social position.""",
"sun_ura/mc":"""Strong illumination of individuality; getting what one deserves;
unrest; eagerness for achievement; nervous drive.""",
"moon_ura/mc":"""Prominent shift of direction for emotional fulfillment;
excitement about making a new bid for life advancement.""",
"merc_ura/mc":"""Nervous excitability in expectation of change; new ideas.""",
"ven_ura/mc":"""Possible promiscuity; feelings are exposed; creativity; eagerness
to please.""",
"mars_ura/mc":"""Temperamental drive for ego recognition; argumentative and
challenging; rash action; upping the tempo.""",
"jup_ura/mc":"""Optimistic outlook for success; recognition; publicity.""",
"sat_ura/mc":"""Possible rebuff in one's bid for recognition; having to temper
idiosyncratic behavior; pull back for gain.""",
"nep_ura/mc":"""Creativity; expecting recognition; withdrawal if frustrated.""",
"plu_ura/mc":"""Extraordinary power-drive to win success and command
attention; overexertion threatens the nervous system.""",
"nod_ura/mc":"""Climbing over others to fulfill one's own needs for recognition.""",
"asc_ura/mc":"""Sudden adjustments to much of the life; change that has
far-reaching significance; "this is it" for years to come.""",

####################################################################

#Neptune and Pluto 491
"nep_to_natplu":"""The supernatural; other realms seem to be involved with life
occurrences; unusual problems; peculiar experiences; possible
concerns about death matters; creative enterprise.""",
"plu_to_natnep":"""Enormous intensification of sensory sensitivity; possible loss of
the frame of reality; subterfuge; possible introduction of drugs
or alcohol dysftmctionally.""",
"sun_nep/plu":"""Creative enterprise; possible drain on the system through
overindulgences; rationalization reigns over realism.""",
"moon_nep/plu":"""Extreme creativity possible; high sensitivity; big mood sweeps
and fluctuations; anxiety about being appreciated.""",
"merc_nep/plu":"""Preoccupation with out-of-the-world thoughts and experiences;
communications are other than they appear; deception as a
strategy; nervous irritability; loss of centering.""",
"ven_nep/plu":"""Creativity; respect for mysticism; intense love fantasy; sensuality;
overindulgence with anything pleasant.""",
"mars_nep/plu":"""Great personal magnetism to set things right or rejection of
actions because of misunderstanding.""",
"jup_nep/plu":"""In love with love, with life; feeling at one with the way things
should be; a 'Thank God' position; possibly religiousness.""",
"sat_nep/plu":"""Grief, weakness, torment.""",
"nep_nep/plu":"""Disruption to gain recognition; adventurous ego thrust; courage;
making waves to get to shore; possibly aberrant behavior.""",
"nod_nep/plu":"""Sharing otherworldliness and curiosity with others; group study
projects.""",
"asc_nep/plu":"""The mystical air flavors personal image.""",
"mc_nep/plu":"""Profit through the occult or the spiritual; recognition of
idiosyncrasies.""",

##################################################################################

#Neptune and Lunar Node 492
"nep_to_natnod":"""Possible breakdown of relationships; sense of being out of the
group, or bound together through spiritual sharing.""",
"nod_to_natnep":"""Meeting with others interested in paranormal dimensions.""",
"sun_nep/nod":"""Seeking to establish contacts with others through artistic or
spiritual exchange; or else feeling misunderstood.""",
"moon_nep/nod":"""High sensitivity; feeling ostracized; being misunderstood.""",
"merc_nep/nod":"""Imagination shared with others; expecting too much from
others; being let down by occurrences; undependability.""",
"ven_nep/nod":"""Vagueness about emotional values; suspicions; promiscuity.""",
"mars_nep/nod":"""Charisma; resourceful adaptation to others.""",
"jup_nep/nod":"""Spiritual bonds with others; religiousness tightens relationships.""",
"ura_nep/nod":"""Emotional hurt through deception, unfaithfulness, duplicity.""",
"sat_nep/nod":"""Self-willed motives disrupt group ideas.""",
"plu_nep/nod":"""Difficulty blending personal perspective with others' views.""",
"asc_nep/nod":"""Appearing strange to others; being duped.""",
"mc_nep/nod":"""Taking a position off the mainstream of life.""",

#############################################################################

#Neptune and Ascendant 493
"nep_to_natasc":"""High sensitivity, impressionability; spiritual projection; loss of
ego.""",
"asc_to_natnep":"""Gaining acceptance for one's specialness.""",
"sun_nep/asc":"""Projection of aesthetics, creativity; the arts as a profession;
sensitivities are used for gain, or there is discomfort and
frustration.""",
"moon_nep/asc":"""Great sensitivity; open to hurt; easily deceived.""",
"merc_nep/asc":"""Great imagination; special perceptions; aware ofspecial levels
of interaction with others; open to deception.""",
"ven_nep/asc":"""Sensual image; longing to understand love and share it.""",
"mars_nep/asc":"""Charisma possible; fighting for one's vision; disputes about
ethereal premises.""",
"jup_nep/asc":"""Good fortune is assumed; one's peaceful nature.""",
"ura_nep/asc":"""Loss of get-up-and-go energy; pull back; feeling out of the
group; slow progress through the martyring of earlier ideas.""",
"sat_nep/asc":"""Hoping for luck; someday one's ship comes in.""",
"plu_nep/asc":"""Feelings of an oppressive environment; difficulty tuning in.""",
"nod_nep/asc":"""Hurt through others; deception, rumor.""",
"mc_nep/asc":"""Recognition for aesthetics or alone in one's specially sensitive
realm.""",

##############################################################################

#Neptune and Midheaven 494
"nep_to_natmc":"""Very important time of life: there can be the sense of ego disappearance;
the identity somehow gets lost in situations through
disregard or through drugs or alcohol in emotional defensiveness;
possible success through the arts, imagination, aesthetics;
peculiar states in the early home life; job vagaries for the adult.""",
"mc_to_natnep":"""Accentuation of creativity on the job; disruption in the home
life; being pushed around; feeling lost; "losing it.""",
"sun_nep/mc":"""Illumination of aesthetics and creativity on the job or in the
social life; possible discontent with life position and the creativity
to begin change; reaching for the vision.""",
"moon_nep/mc":"""High sensitivity; artistic expression dominates; being lost in one's
own world.""",
"merc_nep/mc":"""Imagination; losing orientation to the mainstream; rumor;
creative communication.""",
"ven_nep/mc":"""Idealized love out in the open; holding high the image ofwhat
love should be.""",
"mars_nep/mc":"""Charisma for professional gain through the arts; personal artistic
flair; sensual image; playing a role.""",
"jup_nep/mc":"""Dreaming, hoping, feeling sure somehow that all will be well.""",
"sat_nep/mc":"""The feeling of being wiped out; needing to correct past mistakes
with honest, open, clear statements and plans.""",
"ura_nep/mc":"""Intense impatience; self-righteousness; creativity.""",
"plu_nep/mc":"""The supernatural as a professional focus; strange happenings on
the job or in the home.""",
"nod_nep/mc":"""Difficult relationships; peculiarities.""",
"asc_nep/mc":"""The tendency to live in one's own foggy realm; defenses against
insecurity.""",

############################################################################

#Pluto and Lunar Node 495
"plu_to_natnod":"""Identification with a large group; making very important
contacts; a life-significant relationship.""",
"nod_to_natplu":"""New associations of significance and importance.""",
"sun_plu/nod":"""The urge to impose one's will on others.""",
"moon_plu/nod":"""Reaching for the big picture; making the big scene emotionally;
ambition is magnified, or there is too much fear for any action.""",
"merc_plu/nod":"""Thinking big; hearing the grass grow; intellectual dominance.""",
"ven_plu/nod":"""Important love contact; possible tragic melodrama.""",
"mars_plu/nod":"""Exhibition ofpersonal power; tyranny.""",
"jup_plu/nod":"""Forcing oneself into a power position; self-promotion; attaining
success through others.""",
"ura_plu/nod":"""Potential loss through others; the end of relationships.""",
"sat_plu/nod":"""Intense need for recognition; publicity; crush the opposition.""",
"nep_plu/nod":"""The power of the half-truth; deception as a tool; win at any cost.""",
"asc_plu/nod":"""The need for influence.""",
"mc_plu/nod":"""Associations with others are the sine qua non of success.""",

#######################################################################

#Pluto and Ascendant 496
"plu_to_natasc":"""Extremely important time oflife: dramatic changes of
perspective are possible; identity transformation; geographic
relocation; taking command of things; a life milestone.""",
"asc_to_natplu":"""The use of personal power and persuasion.""",
"sun_plu/asc":"""Seeing a whole new avenue for development and success; "full
steam ahead.""",
"moon_plu/asc":"""Strong reaction to stimuli; emotional eruption.""",
"merc_plu/asc":"""Domination of others mentally; the thrust ofintellect.""",
"ven_plu/asc":"""Emotionalism used to excite others; love relationship;
propaganda.""",
"mars_plu/asc":"""Ruthless energy deployment; courage; upset and change;
accident-prone.""",
"jup_plu/asc":"""Drive to major success; receiving a bounty.""",
"ura_plu/asc":"""High potential for great difficulty and loss; oppressive dealings
with others.""",
"sat_plu/asc":"""Unusual events fan the fires further; success at all costs.""",
"nep_plu/asc":"""Something paranormal influences situations, fight against rumor;
vision to fulfill; embarrassment to transcend.""",
"nod_plu/asc":"""Identification of the ego with a larger group.""",
"mc_plu/asc":"""Power and authority and success; ego ascendancy.""",

############################################################################

#Pluto and Midheaven 497
"plu_to_natmc":"""Extremely important time of life; dramatic changes of
perspective are practically assured; identity transformation
is possible; job adjustment is major; professional developments
are life significant; parental adjustments in the early home are
personally significant; separations; a life-milestone.""",
"mc_to_natplu":"""Recognition and the ultimate power position are probable;
past mistakes can be opened to view and threaten ruin; change
of status.""",
"sun_plu/asc":"""The potential for major life change is illuminated; wanting to spread one's wings and fly;
getting on with excitement.""",
"moon_plu/mc":"""Emotional power; leadership through such power; highly
influential.""",
"merc_plu/mc":"""Thinking big; recognition of intelligence; planning.""",
"ven_plu/asc":"""Attractiveness; emotional charisma; appearing sexy.""",
"mars_plu/mc":"""Striving for power; drive to dominate; explosively argumentative.""",
"jup_plu/mc":"""Unusual scope of reward; assumption ofsuccess; righteousness.""",
"ura_plu/mc":"""The conspicuous threat of loss; potential scandal; major business
reversal; hard, hard work; circumstances of death; bereavement.""",
"sat_plu/mc":"""Impatience; nervousness; sudden changes; publicity; rewards.""",
"nep_plu/mc":"""Potential scandal; otherworldliness; peculiarities;
disappointments; away from the middle of the road; power
run amuck.""",
"nod_plu/mc":"""Leadership of a group of people.""",
"asc_plu/mc":"""Importance and fame; being out in front of everyone.""",

#####################################################################################

#Lunar Node and Ascendant 498
"nod_to_natasc":"""Personal relationships.""",
"asc_to_natnod":"""Personal relationships.""",
"sun_nod/asc":"""Helpful social contacts; gregariousness; an entertaining
personality.""",
"moon_nod/asc":"""Emotional bonds with others; sympathy; caring for others.""",
"merc_nod/asc":"""Entertainment; gossip; exchanging ideas; getting input from
others; news; traveling to meetings.""",
"ven_nod/asc":"""Pleasantness; affectionate associations.""",
"mars_nod/asc":"""Working for the common good; the 'doer.'""",
"jup_nod/asc":"""Sociability; humanitarianism; congeniality.""",
"ura_nod/asc":"""Prevailing with realism and wisdom; conservatism.""",
"sat_nod/asc":"""All for the avant-garde; unusual associations; upbeat ways of
doing things with other people.""",
"nep_nod/asc":"""Making relationships with others through sensitivities and even
interests in the paranormal; impressionability.""",
"plu_nod/asc":"""Power plays with others for personal advancement.""",
"mc_nod/asc":"""Sense of community.""",

######################################################################################

#Lunar Node and Midheaven 499
"nod_to_natmc":"""Being recognized; meeting or marriage.""",
"mc_to_natnod":"""Being recognized; meeting or marriage.""",
"sun_nod/mc":"""The importance of contacts and friends for success; easy social
ascendancy.""",
"moon_nod/mc":"""The challenge and fulfillment ofsharing emotions with others.""",
"merc_nod/mc":"""The exchange of ideas for personal gain.""",
"ven_nod/mc":"""Sociability; congeniality; talking about feelings to someone.""",
"mars_nod/mc":"""Getting things done together; partnership work.""",
"jup_nod/mc":"""Social life and entertainment; church groups; togetherness.""",
"ura_nod/mc":"""Being comfortable in the loner's position; being the serious person in the group; respect;
conservatism.""",
"sat_nod/mc":"""The sudden experience; possible rashness; being seen as "zany";
solving problems innovatively with others.""",
"nep_nod/mc":"""The tendency to impracticality in dealing with others.""",
"plu_nod/mc":"""Leadership; success.""",
"asc_nod/mc":"""Harmony.""",

#####################################################################################

#Ascendant and Midheaven 500
"asc _to_natmc":"""Identity awareness.""",
"mc _to_natasc":"""Identity awareness.""",
"sun_asc/mc":"""The quest to be one's own person; to do well by one's selfimage; to clarify the persona.""",
"moon_asc/mc":"""Showing others how one feels about things.""",
"merc_asc/mc":"""Thinking about one's place in the world.""",
"ven_asc/mc":"""The sense of beauty; harmony; comfort.""",
"mars_asc/mc":"""Individual talents put into action.""",
"jup_asc/mc":"""Glad to be alive; optimism; pleased with things; justification.""",
"ura_asc/mc":"""Austerity is important as part of maturity and reliability; conservatism is comfortable.""",
"sat_asc/mc":"""Excitability; emotional; quickly responsive; adventurous.""",
"nep_asc/mc":"""Idealization; spirituality; quiet.""",
"plu_asc/mc":"""Power performances become well known.""",
"nod_asc/mc":"""Pleasantness; contacts come easily.""",
}

