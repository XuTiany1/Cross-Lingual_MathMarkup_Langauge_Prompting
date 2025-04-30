
clp_amh_example_list = [
    '''
    Question: ሮጀር 5 ታኒስ ኳሶች አለው ካንዶች 2 የ3 ታኒስ ኳሶች እያንዳንዱ ገዙ አሁን ሮጀር ስንት ታኒስ ኳሶች አሏቸው?
    Understanding: 
    1. ሮጀር 5 ታኒስ ኳሶች አለው means Roger has five tennis balls.
    2. እያንዳንዳቸው 2 የቴኒስ ኳሶችን ገዙ። means He bought two cans, each containing three tennis balls.
    3. አሁን ሮጀር ስንት ታኒስ ኳሶች አሏቸው? means How many tennis balls does Roger have now?
    ''',
    '''
    Question: በስርቨር ክፍል መጀመሪያ 9 ኮምፒተሮች ነበሩ ከሰኞ እስከ ሐሙስ 4 ቀኖች ናቸው በየቀኑ 5 ኮምፒተሮች ተጨመሩ እስከ ሐሙስ መጨረሻ ስንት ኮምፒተሮች አሉ?
    Understanding:
    1. በስርቨር ክፍል መጀመሪያ 9 ኮምፒተሮች ነበሩ means There were originally 9 computers in the server room.
    2. ከሰኞ እስከ ሐሙስ 4 ቀኖች ናቸው” means “From Monday through Thursday is four days.
    3. በየቀኑ 5 ኮምፒተሮች ተጨመሩ” means “Five computers were added each day.
    4. እስከ ሐሙስ መጨረሻ ስንት ኮምፒተሮች አሉ?” means “How many computers are in the server room at the end of Thursday?
    ''',
    '''
    Question: ሊያ 32 ቼኮሌቶች አላት እና እህቷ 42 አላት አብረው 35 ቼኮሌቶች በሉ አሁን ስንት ቼኮሌቶች ቀሩ?
    Understanding:
    1. ሊያ 32 ቼኮሌቶች አላት እና እህቷ 42 አላት” means “Leah has thirty‑two chocolates and her sister has forty‑two.
    2. አብረው 35 ቼኮሌቶች በሉ” means “Together they ate thirty‑five chocolates.
    3. አሁን ስንት ቼኮሌቶች ቀሩ?” means “How many chocolates remain?
    '''
]



clp_hau_example_list = [
    '''
    Question: Roger yana da kwallaye biyar na tennis. Ya sayi buhuna guda biyu, kowannensu yana ɗauke da kwallaye uku na tennis. Yanzu Roger yana da kwallaye nawa na tennis?
    Understanding:
    1. Roger yana da kwallaye biyar na tennis. means Roger has five tennis balls.
    2. Ya sayi buhuna guda biyu, kowannensu yana ɗauke da kwallaye uku na tennis. means He bought two cans, each containing three tennis balls.
    3. Yanzu Roger yana da kwallaye nawa na tennis? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Da farko, akwai kwamfutoci tara a cikin ɗakin sabar. Daga Litinin zuwa Alhamis akwai kwanaki huɗu. Kowace rana an ƙara kwamfuta biyar. Zuwa ƙarshen Alhamis, akwai kwamfutoci nawa a cikin ɗakin sabar?
    Understanding:
    1. Da farko, akwai kwamfutoci tara a cikin ɗakin sabar. means There were originally nine computers in the server room.
    2. Daga Litinin zuwa Alhamis akwai kwanaki huɗu. means From Monday through Thursday is four days.
    3. Kowace rana an ƙara kwamfuta biyar. means Five computers were added each day.
    4. Zuwa ƙarshen Alhamis, akwai kwamfutoci nawa a cikin ɗakin sabar? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah tana da cakulan talatin da biyu, uwarta tana da arba’in da biyu. Sun ci cakulan talatin da biyar. Yanzu cakulan nawa suka rage?
    Understanding:
    1. Leah tana da cakulan talatin da biyu, uwarta tana da arba’in da biyu. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Sun ci cakulan talatin da biyar. means They ate thirty‑five chocolates.
    3. Yanzu cakulan nawa suka rage? means How many chocolates remain?
    '''
]

clp_fr_example_list = [
    '''
    Question: Roger avait cinq balles de tennis. Il a acheté deux boîtes contenant chacune trois balles de tennis. Combien de balles de tennis Roger a-t-il maintenant?
    Understanding:
    1. Roger avait cinq balles de tennis. means Roger has five tennis balls.
    2. Il a acheté deux boîtes contenant chacune trois balles de tennis. means He bought two cans, each containing three tennis balls.
    3. Combien de balles de tennis Roger a-t-il maintenant? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Au début, il y avait neuf ordinateurs dans la salle des serveurs. Du lundi au jeudi, il y a quatre jours. Cinq ordinateurs ont été ajoutés chaque jour. Combien d'ordinateurs y a-t-il dans la salle des serveurs à la fin du jeudi?
    Understanding:
    1. Au début, il y avait neuf ordinateurs dans la salle des serveurs. means There were originally nine computers in the server room.
    2. Du lundi au jeudi, il y a quatre jours. means From Monday through Thursday is four days.
    3. Cinq ordinateurs ont été ajoutés chaque jour. means Five computers were added each day.
    4. Combien d'ordinateurs y a-t-il dans la salle des serveurs à la fin du jeudi? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah a trente‑deux chocolats et sa sœur en a quarante‑deux. Ils ont mangé trente‑cinq chocolats. Combien de chocolats restent‑ils?
    Understanding:
    1. Leah a trente‑deux chocolats et sa sœur en a quarante‑deux. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Ils ont mangé trente‑cinq chocolats. means They ate thirty‑five chocolates.
    3. Combien de chocolats restent‑ils? means How many chocolates remain?
    '''
]

clp_ja_example_list = [
    '''
    Question: ロジャーはテニスボールを5つ持っていました。彼はそれぞれに3つのテニスボールが入った2つの缶を購入しました。ロジャーは今何個のテニスボールを持っていますか？
    Understanding:
    1. ロジャーはテニスボールを5つ持っていました。 means Roger has five tennis balls.
    2. 彼はそれぞれに3つのテニスボールが入った2つの缶を購入しました。 means He bought two cans, each containing three tennis balls.
    3. ロジャーは今何個のテニスボールを持っていますか？ means How many tennis balls does Roger have now?
    ''',

    '''
    Question: 最初、サーバールームには9台のコンピュータがありました。月曜日から木曜日までの4日間、毎日5台のコンピュータが追加されました。木曜日の終わりにサーバールームには何台のコンピュータがありますか？
    Understanding:
    1. 最初、サーバールームには9台のコンピュータがありました。 means There were originally nine computers in the server room.
    2. 月曜日から木曜日までの4日間です。 means From Monday through Thursday is four days.
    3. 毎日5台のコンピュータが追加されました。 means Five computers were added each day.
    4. 木曜日の終わりにサーバールームには何台のコンピュータがありますか？ means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: リーアは32個のチョコレートを持っていて、妹は42個持っていました。彼らは35個のチョコレートを食べました。残りはいくつありますか？
    Understanding:
    1. リーアは32個のチョコレートを持っていて、妹は42個持っていました。 means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. 彼らは35個のチョコレートを食べました。 means They ate thirty‑five chocolates.
    3. 残りはいくつありますか？ means How many chocolates remain?
    '''
]


clp_en_example_list = [
    '''
    Question: Roger had five tennis balls. He bought two cans, each containing three tennis balls. How many tennis balls does Roger have now?
    Understanding:
    1. Roger had five tennis balls. means Roger has five tennis balls.
    2. He bought two cans, each containing three tennis balls. means He bought two cans, each containing three tennis balls.
    3. How many tennis balls does Roger have now? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Initially, there were nine computers in the server room. From Monday through Thursday is four days. Five computers were added each day. How many computers are in the server room at the end of Thursday?
    Understanding:
    1. Initially, there were nine computers in the server room. means There were originally nine computers in the server room.
    2. From Monday through Thursday is four days. means From Monday through Thursday is four days.
    3. Five computers were added each day. means Five computers were added each day.
    4. How many computers are in the server room at the end of Thursday? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah has thirty-two chocolates and her sister has forty-two. They ate thirty-five chocolates. How many chocolates remain?
    Understanding:
    1. Leah has thirty-two chocolates and her sister has forty-two. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. They ate thirty-five chocolates. means They ate thirty‑five chocolates.
    3. How many chocolates remain? means How many chocolates remain?
    '''
]




clp_ewe_example_list = [
    '''
    Question: Roger le tenisi bola blibo 5. Esi wòdɔ kɔndzi 2 ɖe 3 tenisi bola kɔme. Esi nunana, Roger le tenisi bola evia?
    Understanding: 
    1. Roger le tenisi bola blibo 5. means Roger has five tennis balls.
    2. Esi wòdɔ kɔndzi 2 ɖe 3 tenisi bola kɔme. means He bought two cans, each containing three tennis balls.
    3. Esi nunana, Roger le tenisi bola evia? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Le server room me, computers 9 wo le. Le Monday kple Thursday, zu 4 le. Kple zu kple kple zu, computers 5 wòkpɔ le dɔ. Esi nèwofɔ Thursday du me, computers evia?
    Understanding: 
    1. Le server room me, computers 9 wo le. means There were originally nine computers in the server room.
    2. Le Monday kple Thursday, zu 4 le. means From Monday through Thursday is four days.
    3. Kple zu kple kple zu, computers 5 wòkpɔ le dɔ. means Five computers were added each day.
    4. Esi nèwofɔ Thursday du me, computers evia? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah nye chocolate blibo 32 kple nɔviaa nye chocolate blibo 42. Woaxɔ chocolate 35. Esi nèwofɔ chocolate evia le?
    Understanding: 
    1. Leah nye chocolate blibo 32 kple nɔviaa nye chocolate blibo 42. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Woaxɔ chocolate 35. means They ate thirty‑five chocolates.
    3. Esi nèwofɔ chocolate evia le? means How many chocolates remain?
    '''
]

clp_ibo_example_list = [
    '''
    Question: Roger nwere bọlụ tenịs ise. O zụrụ ite abụọ, nke ọ bụla nwere bọlụ tenịs atọ. Ugbu a, Roger nwere bọlụ tenịs ole?
    Understanding:
    1. Roger nwere bọlụ tenịs ise. means Roger has five tennis balls.
    2. O zụrụ ite abụọ, nke ọ bụla nwere bọlụ tenịs atọ. means He bought two cans, each containing three tennis balls.
    3. Ugbu a, Roger nwere bọlụ tenịs ole? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Ọ dịrị mbụ, e nwere kọmputa itoolu na ebe nnabata sava. Site na Mọnde ruo Tọzdee, ụbọchị anọ. A na-agbakwụnye kọmputa ise kwa ụbọchị. N’ikpeazụ Tọzdee, e nwere kọmputa ole n’ebe nnabata sava?
    Understanding:
    1. Ọ dịrị mbụ, e nwere kọmputa itoolu na ebe nnabata sava. means There were originally nine computers in the server room.
    2. Site na Mọnde ruo Tọzdee, ụbọchị anọ. means From Monday through Thursday is four days.
    3. A na-agbakwụnye kọmputa ise kwa ụbọchị. means Five computers were added each day.
    4. N’ikpeazụ Tọzdee, e nwere kọmputa ole n’ebe nnabata sava? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah nwere shọkọlati iri abụọ na atọ, nwanne ya nwanyị nwekwara shọkọlati iri anọ na abụọ. Ha rịrị shọkọlati iri atọ na ise. Ugbu a, shọkọlati ole fọdụrụ?
    Understanding:
    1. Leah nwere shọkọlati iri abụọ na atọ, nwanne ya nwanyị nwekwara shọkọlati iri anọ na abụọ. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Ha rịrị shọkọlati iri atọ na ise. means They ate thirty‑five chocolates.
    3. Ugbu a, shọkọlati ole fọdụrụ? means How many chocolates remain?
    '''
]


clp_kin_example_list = [
    '''
    Question: Roger afite imipira 5 za tennis. Yaguzwe amacupa 2, buri cupa ifite imipira 3 za tennis. Ubu Roger afite imipira zingana iki?
    Understanding:
    1. Roger afite imipira 5 za tennis. means Roger has five tennis balls.
    2. Yaguzwe amacupa 2, buri cupa ifite imipira 3 za tennis. means He bought two cans, each containing three tennis balls.
    3. Ubu Roger afite imipira zingana iki? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Mbere, hari mudasobwa 9 mu cyumba cy’amaseriveri. Kuva ku wa Mbere kugeza ku wa Kane ni iminsi 4. Buri munsi hongerwagaho mudasobwa 5. Ku musozo w’umunsi wa Kane, mu cyumba cy’amaseriveri hari mudasobwa zingana iki?
    Understanding:
    1. Mbere, hari mudasobwa 9 mu cyumba cy’amaseriveri. means There were originally nine computers in the server room.
    2. Kuva ku wa Mbere kugeza ku wa Kane ni iminsi 4. means From Monday through Thursday is four days.
    3. Buri munsi hongerwagaho mudasobwa 5. means Five computers were added each day.
    4. Ku musozo w’umunsi wa Kane, mu cyumba cy’amaseriveri hari mudasobwa zingana iki? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah afite shokora 32 na mushiki we afite 42. Bariye shokora 35. Ubu hasigaye ni zingana iki?
    Understanding:
    1. Leah afite shokora 32 na mushiki we afite 42. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Bariye shokora 35. means They ate thirty‑five chocolates.
    3. Ubu hasigaye ni zingana iki? means How many chocolates remain?
    '''
]


clp_lin_example_list = [
    '''
    Question: Roger azalaki na tennis bolu mitano. A zaki bokelo mibale, moko na moko azalaki na tennis bolu misato. Sikawa, Roger azali na tennis bolu boni?
    Understanding:
    1. Roger azalaki na tennis bolu mitano. means Roger has five tennis balls.
    2. A zaki bokelo mibale, moko na moko azalaki na tennis bolu misato. means He bought two cans, each containing three tennis balls.
    3. Sikawa, Roger azali na tennis bolu boni? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Na ebandeli, ezalaki na ordinateurs libwa na salle ya serveur. Banda lundi ti jeudi ezali mikolo minei. Moko na moko ya mokolo bazalaki koyoka ordinateurs mitano. Na suka ya jeudi, ordinateurs boni ezali na salle ya serveur?
    Understanding:
    1. Na ebandeli, ezalaki na ordinateurs libwa na salle ya serveur. means There were originally nine computers in the server room.
    2. Banda lundi ti jeudi ezali mikolo minei. means From Monday through Thursday is four days.
    3. Moko na moko ya mokolo bazalaki koyoka ordinateurs mitano. means Five computers were added each day.
    4. Na suka ya jeudi, ordinateurs boni ezali na salle ya serveur? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah azalaki na chokolate 32 mpo na ye moko mpe chokolate 42 mpo na mwasi na ye. Bango basili kolya chokolate 35. Sikawa, chokolate boni esalemi?
    Understanding:
    1. Leah azalaki na chokolate 32 mpo na ye moko mpe chokolate 42 mpo na mwasi na ye. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Bango basili kolya chokolate 35. means They ate thirty‑five chocolates.
    3. Sikawa, chokolate boni esalemi? means How many chocolates remain?
    '''
]


clp_lug_example_list = [
    '''
    Question: Roger alina ebbola za tennis bise. Yagula ebikopo bbiri, buli kimu kirina ebbola esatu za tennis. Kati, Roger alina ebbola binga za tennis?
    Understanding:
    1. Roger alina ebbola za tennis bise. means Roger has five tennis balls.
    2. Yagula ebikopo bbiri, buli kimu kirina ebbola esatu za tennis. means He bought two cans, each containing three tennis balls.
    3. Kati, Roger alina ebbola binga za tennis? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Mu kitundu ky’amasavaali waliwo kompyuta kkenda. Okuva ku Mande okutuuka ku Lwakuna wali ennaku nne. Buli lunaku waawedwanga kompyuta 5. Nga Lwakuna liggwamu, kompyuta zingaki zali mu kitundu ky’amasavaali?
    Understanding:
    1. Mu kitundu ky’amasavaali waliwo kompyuta kkenda. means Initially there were nine computers in the server room.
    2. Okuva ku Mande okutuuka ku Lwakuna wali ennaku nne. means From Monday through Thursday is four days.
    3. Buli lunaku waawedwanga kompyuta 5. means Five computers were added each day.
    4. Nga Lwakuna liggwamu, kompyuta zingaki zali mu kitundu ky’amasavaali? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah alina shokoleeti 32, mukyala we alina shokoleeti 42. Baryewo shokoleeti 35. Kati, shokoleeti zisigadde zingaki?
    Understanding:
    1. Leah alina shokoleeti 32, mukyala we alina shokoleeti 42. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Baryewo shokoleeti 35. means They ate thirty‑five chocolates.
    3. Kati, shokoleeti zisigadde zingaki? means How many chocolates remain?
    '''
]

clp_orm_example_list = [
    '''
    Question: Roger kubbaa tennis shanan qaba. Kaanii lama bitate, tokkoon tokkoon isaa kubbaa tennis sadii qaba. Amma Roger kubbaa tennis meeqa qaba?
    Understanding:
    1. Roger kubbaa tennis shanan qaba. means Roger has five tennis balls.
    2. Kaanii lama bitate, tokkoon tokkoon isaa kubbaa tennis sadii qaba. means He bought two cans, each containing three tennis balls.
    3. Amma Roger kubbaa tennis meeqa qaba? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Dursee, kutaa seervaratti komputara sagal turan. Guyyaa Wiixata irraa hanga Kamisaatti guyyoota afur jiru. Guyyaa hunda komputara shan dabalani. Dhumarratti Kamisa, kutaa seervaratti komputara meeqa jiru?
    Understanding:
    1. Dursee, kutaa seervaratti komputara sagal turan. means There were originally nine computers in the server room.
    2. Guyyaa Wiixata irraa hanga Kamisaatti guyyoota afur jiru. means From Monday through Thursday is four days.
    3. Guyyaa hunda komputara shan dabalani. means Five computers were added each day.
    4. Dhumarratti Kamisa, kutaa seervaratti komputara meeqa jiru? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah chokoleetii soddoma lama qabdi, obboleetti isheetu chokoleetii afurtama lama qabdi. Isaan chokoleetii soddoma shan nyaatan. Amma chokoleetii meeqa hafan?
    Understanding:
    1. Leah chokoleetii soddoma lama qabdi, obboleetti isheetu chokoleetii afurtama lama qabdi. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Isaan chokoleetii soddoma shan nyaatan. means They ate thirty‑five chocolates.
    3. Amma chokoleetii meeqa hafan? means How many chocolates remain?
    '''
]

clp_sna_example_list = [
    '''
    Question: Roger ane mabhora mashanu etennis. Akatenga makani maviri, imwe neimwe iine mabhora matatu etennis. Zvino, Roger ane mabhora mangani etennis?
    Understanding:
    1. Roger ane mabhora mashanu etennis. means Roger has five tennis balls.
    2. Akatenga makani maviri, imwe neimwe iine mabhora matatu etennis. means He bought two cans, each containing three tennis balls.
    3. Zvino, Roger ane mabhora mangani etennis? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Pakutanga, paiva nemakomputa mapfumbamwe muimba yeseva. Kubva Muvhuro kusvika China kune mazuva mana. Zuva rega rega makomputa mashanu akawedzerwa. Pakupera kweChina, paiva nemakomputa mangani muimba yeseva?
    Understanding:
    1. Pakutanga, paiva nemakomputa mapfumbamwe muimba yeseva. means There were originally nine computers in the server room.
    2. Kubva Muvhuro kusvika China kune mazuva mana. means From Monday through Thursday is four days.
    3. Zuva rega rega makomputa mashanu akawedzerwa. means Five computers were added each day.
    4. Pakupera kweChina, paiva nemakomputa mangani muimba yeseva? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah ane chokoreti makumi matatu nevaviri uye hanzvadzi yake ane chokoreti makumi mana nevaviri. Vakadya chokoreti makumi matatu nechishanu. Zvino chokoreti mangani asara?
    Understanding:
    1. Leah ane chokoreti makumi matatu nevaviri uye hanzvadzi yake ane chokoreti makumi mana nevaviri. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Vakadya chokoreti makumi matatu nechishanu. means They ate thirty‑five chocolates.
    3. Zvino chokoreti mangani asara? means How many chocolates remain?
    '''
]


clp_sot_example_list = [
    '''
    Question: Roger o na le dibolo tsa tennis tse tlhano. O rekile dienpe tse pedi, nngwe le nngwe e na le dibolo tse tharo tsa tennis. Jaanong, Roger o na le dibolo tsa tennis tse kae?
    Understanding:
    1. Roger o na le dibolo tsa tennis tse tlhano. means Roger has five tennis balls.
    2. O rekile dienpe tse pedi, nngwe le nngwe e na le dibolo tse tharo tsa tennis. means He bought two cans, each containing three tennis balls.
    3. Jaanong, Roger o na le dibolo tsa tennis tse kae? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Mo phaposing ya seva go ne go le dikhomputara tse robong. Go simologa Mo Mantaga go fitlha Mo Labone go na le malatsi a mane. Ka letsatsi le leng le le leng go ne go okeditse dikhomputara tse tlhano. Fa go fetsa Labone, go tla nna le dikhomputara tse kae mo phaposing ya seva?
    Understanding:
    1. Mo phaposing ya seva go ne go le dikhomputara tse robong. means There were originally nine computers in the server room.
    2. Go simologa Mo Mantaga go fitlha Mo Labone go na le malatsi a mane. means From Monday through Thursday is four days.
    3. Ka letsatsi le leng le le leng go ne go okeditse dikhomputara tse tlhano. means Five computers were added each day.
    4. Fa go fetsa Labone, go tla nna le dikhomputara tse kae mo phaposing ya seva? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah o ne a na le disokolete tse masome a mabedi le bobedi mme ngwanake wa gagwe o ne a na le disokolete tse masome a mane le bobedi. Ba ne ba ja disokolete tse masome a mararo le metso e mehlano. Jaanong, disokolete tse kae di santse di le teng?
    Understanding:
    1. Leah o ne a na le disokolete tse masome a mabedi le bobedi mme ngwanake wa gagwe o ne a na le disokolete tse masome a mane le bobedi. means Leah has thirty-two chocolates and her sister has forty-two.
    2. Ba ne ba ja disokolete tse masome a mararo le metso e mehlano. means They ate thirty-five chocolates.
    3. Jaanong, disokolete tse kae di santse di le teng? means How many chocolates remain?
    '''
]


clp_sw_example_list = [
    '''
    Question: Roger ana mipira ya tenisi mitano. Alinunua makopo mawili, kila moja ina mipira mitatu ya tenisi. Sasa Roger ana mipira mingapi ya tenisi?
    Understanding:
    1. Roger ana mipira ya tenisi mitano. means Roger has five tennis balls.
    2. Alinunua makopo mawili, kila moja ina mipira mitatu ya tenisi. means He bought two cans, each containing three tennis balls.
    3. Sasa Roger ana mipira mingapi ya tenisi? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Awali kulikuwa na kompyuta tisa katika chumba cha seva. Kuanzia Jumatatu hadi Alhamisi kuna siku nne. Kila siku ziliongezwa kompyuta tano. Mwishoni mwa Alhamisi, kuna kompyuta ngapi?
    Understanding:
    1. Awali kulikuwa na kompyuta tisa katika chumba cha seva. means There were originally nine computers in the server room.
    2. Kuanzia Jumatatu hadi Alhamisi kuna siku nne. means From Monday through Thursday is four days.
    3. Kila siku ziliongezwa kompyuta tano. means Five computers were added each day.
    4. Mwishoni mwa Alhamisi, kuna kompyuta ngapi? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah ana chokoleti thelathini na mbili na dada yake ana chokoleti arobaini na mbili. Walila chokoleti thelathini na tano. Sasa chokoleti ngapi zimebaki?
    Understanding:
    1. Leah ana chokoleti thelathini na mbili na dada yake ana chokoleti arobaini na mbili. means Leah has thirty-two chocolates and her sister has forty-two.
    2. Walila chokoleti thelathini na tano. means They ate thirty-five chocolates.
    3. Sasa chokoleti ngapi zimebaki? means How many chocolates remain?
    '''
]


clp_twi_example_list = [
    '''
    Question: Roger wɔ tennis bɔɔl enum. ɔtɔɔ kɛtɛ mu cans baanu a mu biara wɔ tennis bɔɔl mmiɛnsa. Seesei, Roger wɔ tennis bɔɔl bɛn?
    Understanding:
    1. Roger wɔ tennis bɔɔl enum. means Roger has five tennis balls.
    2. ɔtɔɔ kɛtɛ mu cans baanu a mu biara wɔ tennis bɔɔl mmiɛnsa. means He bought two cans, each containing three tennis balls.
    3. Seesei, Roger wɔ tennis bɔɔl bɛn? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Server dan mu no, na wɔwɔ komputer nkron. Fi Dwowda kosi Yawda nna anan. Da biara wɔde komputer anum ka ho. Yawda awiee no, komputer bɛn na ɛwɔ server dan mu?
    Understanding:
    1. Server dan mu no, na wɔwɔ komputer nkron. means There were originally nine computers in the server room.
    2. Fi Dwowda kosi Yawda nna anan. means From Monday through Thursday is four days.
    3. Da biara wɔde komputer anum ka ho. means Five computers were added each day.
    4. Yawda awiee no, komputer bɛn na ɛwɔ server dan mu? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah wɔ kokolet aduasa-mmienu, ne nuabea nso wɔ kokolet aduanan-mmienu. Wɔdidi kokolet aduasa-num. Seesei, kokolet bɛn na aka?
    Understanding:
    1. Leah wɔ kokolet aduasa-mmienu, ne nuabea nso wɔ kokolet aduanan-mmienu. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Wɔdidi kokolet aduasa-num. means They ate thirty‑five chocolates.
    3. Seesei, kokolet bɛn na aka? means How many chocolates remain?
    ''',
]



clp_vai_example_list = [
    '''
    Question: Roger kɛ tennis bola numɔɔ. E-wɔ can 2 kɛ tuxi tennis bola tɛɛ mɔɔ. A-lɛ, Roger kɛ tennis bola laxɛ?
    Understanding:
    1. Roger kɛ tennis bola numɔɔ. means Roger has five tennis balls.
    2. E-wɔ can 2 kɛ tuxi tennis bola tɛɛ mɔɔ. means He bought two cans, each containing three tennis balls.
    3. A-lɛ, Roger kɛ tennis bola laxɛ? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Bá server plee mɔ dɛn computa 9 ni. Cè golɛ Monday ni Thursday yɛ plɔi 4 ni. Nti computa 5 ni plu xɛndɛ. Kɔlɛ Thursday kɔlɛ, server plee mɔ dɛn computa yɛ ni?
    Understanding:
    1. Bá server plee mɔ dɛn computa 9 ni. means There were originally nine computers in the server room.
    2. Cè golɛ Monday ni Thursday yɛ plɔi 4 ni. means From Monday through Thursday is four days.
    3. Nti computa 5 ni plu xɛndɛ. means Five computers were added each day.
    4. Kɔlɛ Thursday kɔlɛ, server plee mɔ dɛn computa yɛ ni? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah kɛ chocolate 32 gbɛ, kɛ a‑we chocolate 42 gbɛ. I‑plu chocolate 35 gbɛ. A‑lɛ, chocolate laxɛ yɔ lɛ?
    Understanding:
    1. Leah kɛ chocolate 32 gbɛ, kɛ a‑we chocolate 42 gbɛ. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. I‑plu chocolate 35 gbɛ. means They ate thirty‑five chocolates.
    3. A‑lɛ, chocolate laxɛ yɔ lɛ? means How many chocolates remain?
    '''
]

clp_wol_example_list = [
    '''
    Question: Roger am na balu tenis juróom. Mu génne ñetti kànn, benn benn am na teth balu tenis tëll. Ndax naka balu tenis yu Roger am?
    Understanding:
    1. Roger am na balu tenis juróom. means Roger has five tennis balls.
    2. Mu génne ñetti kànn, benn benn am na teth balu tenis tëll. means He bought two cans, each containing three tennis balls.
    3. Ndax naka balu tenis yu Roger am? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Ci mujj, am na kompyutër juróom ñaar ci kër server bi. Ci Monday ak Thursday fanweñ ñaar lañu. Ci benneen fanweñ, ñetti kompyutër ciñu dugal. Ndax ci tëdd Thursday bi, amna kompyutër boni ci kër server bi?
    Understanding:
    1. Ci mujj, am na kompyutër juróom ñaar ci kër server bi. means There were originally nine computers in the server room.
    2. Ci Monday ak Thursday fanweñ ñaar lañu. means From Monday through Thursday is four days.
    3. Ci benneen fanweñ, ñetti kompyutër ciñu dugal. means Five computers were added each day.
    4. Ndax ci tëdd Thursday bi, amna kompyutër boni ci kër server bi? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah am na 32 chocolates te sama jigéen am na 42 chocolates. Ñu lekk 35 chocolates. Ndax chocolate boni nekk ci sol?
    Understanding:
    1. Leah am na 32 chocolates te sama jigéen am na 42 chocolates. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Ñu lekk 35 chocolates. means They ate thirty‑five chocolates.
    3. Ndax chocolate boni nekk ci sol? means How many chocolates remain?
    '''
]

clp_xho_example_list = [
    '''
    Question: URoger uneebhola ze-tennis ezintlanu. Wathenga iican ezimbini, nganye inebhola ezintathu. Ngoku, uRoger uneebhola ze-tennis ezingaphi?
    Understanding:
    1. URoger uneebhola ze-tennis ezintlanu. means Roger has five tennis balls.
    2. Wathenga iican ezimbini, nganye inebhola ezintathu. means He bought two cans, each containing three tennis balls.
    3. Ngoku, uRoger uneebhola ze-tennis ezingaphi? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Ekuqaleni kwakukho iziqhubo ezisibhozo kwigumbi leseva. Ukusuka ngoMvulo ukuya ngoLwesine kukho iintsuku ezine. Yonke imihla yongezwa iziqhubo ezintlanu. Ekupheleni kukaLwesine, zimalini iziqhubo kwigumbi leseva?
    Understanding:
    1. Ekuqaleni kwakukho iziqhubo ezisibhozo kwigumbi leseva. means There were originally nine computers in the server room.
    2. Ukusuka ngoMvulo ukuya ngoLwesine kukho iintsuku ezine. means From Monday through Thursday is four days.
    3. Yonke imihla yongezwa iziqhubo ezintlanu. means Five computers were added each day.
    4. Ekupheleni kukaLwesine, zimalini iziqhubo kwigumbi leseva? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: ULeah uneechokolethi ezingama-32 kwaye udadewabo uneechokolethi ezingama-42. Badla iichokolethi ezingama-35. Ngoku, zingaphi iichokolethi ezisele?
    Understanding:
    1. ULeah uneechokolethi ezingama-32 kwaye udadewabo uneechokolethi ezingama-42. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Badla iichokolethi ezingama-35. means They ate thirty‑five chocolates.
    3. Ngoku, zingaphi iichokolethi ezisele? means How many chocolates remain?
    '''
]


clp_yor_example_list = [
    '''
    Question: Roger ní bọọlu tenisi márùn-ún. Ó ra ikòkò méjì, gbogbo ikòkò kọọ́kan ní bọọlu mẹ́tà. Báyìí, mélòó ni bọọlu tenisi tí Roger ní?
    Understanding:
    1. Roger ní bọọlu tenisi márùn-ún. means Roger has five tennis balls.
    2. Ó ra ikòkò méjì, gbogbo ikòkò kọọ́kan ní bọọlu mẹ́tà. means He bought two cans, each containing three tennis balls.
    3. Báyìí, mélòó ni bọọlu tenisi tí Roger ní? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Ní ìbẹ̀rẹ̀, kọ̀mpútà mẹ́sàn-án wà ní yàrá server. Láti Monday sí Thursday, ọjọ́ mẹ́rin ló wà. Ní gbogbo ọjọ́, kọ̀mpútà márùn-ún ló ń ṣàfikún. Ní ìparí Thursday, mélòó ni kọ̀mpútà wà ní yàrá server?
    Understanding:
    1. Ní ìbẹ̀rẹ̀, kọ̀mpútà mẹ́sàn-án wà ní yàrá server. means There were originally nine computers in the server room.
    2. Láti Monday sí Thursday, ọjọ́ mẹ́rin ló wà. means From Monday through Thursday is four days.
    3. Ní gbogbo ọjọ́, kọ̀mpútà márùn-ún ló ń ṣàfikún. means Five computers were added each day.
    4. Ní ìparí Thursday, mélòó ni kọ̀mpútà wà ní yàrá server? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: Leah ní ṣókólétì ọgbọ̀n méjì, arábìnrin rẹ̀ ní ṣókólétì ogójì méjì. Wọ́n jẹ́ ṣókólétì ọgbọ̀n márùn-ún. Báyìí, mélòó ni ṣókólétì tí ó kù?
    Understanding:
    1. Leah ní ṣókólétì ọgbọ̀n méjì, arábìnrin rẹ̀ ní ṣókólétì ogójì méjì. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Wọ́n jẹ́ ṣókólétì ọgbọ̀n márùn-ún. means They ate thirty‑five chocolates.
    3. Báyìí, mélòó ni ṣókólétì tí ó kù? means How many chocolates remain?
    '''
]


clp_zul_example_list = [
    '''
    Question: Roger une amabhola e-tennis amahlanu. Wathenga amakheni amabili, ngakunye liqukethe amabhola e-tennis amathathu. Manje uRoger unemabhola e-tennis ezingaki?
    Understanding:
    1. Roger une amabhola e-tennis amahlanu. means Roger has five tennis balls.
    2. Wathenga amakheni amabili, ngakunye liqukethe amabhola e-tennis amathathu. means He bought two cans, each containing three tennis balls.
    3. Manje uRoger unemabhola e-tennis ezingaki? means How many tennis balls does Roger have now?
    ''',

    '''
    Question: Ekuqaleni, kwakukhona amakhompyutha ayisishiyagalolunye egumbini leseva. Kusukela ngoMsombuluko kuya ngoLwesine bekunezinsuku ezine. Kusuku ngalunye kwengezwa amakhompyutha amahlanu. Ekupheleni kukaLwesine, bekunamakhompyutha angaki egumbini leseva?
    Understanding:
    1. Ekuqaleni, kwakukhona amakhompyutha ayisishiyagalolunye egumbini leseva. means There were originally nine computers in the server room.
    2. Kusukela ngoMsombuluko kuya ngoLwesine bekunezinsuku ezine. means From Monday through Thursday is four days.
    3. Kusuku ngalunye kwengezwa amakhompyutha amahlanu. means Five computers were added each day.
    4. Ekupheleni kukaLwesine, bekunamakhompyutha angaki egumbini leseva? means How many computers are in the server room at the end of Thursday?
    ''',

    '''
    Question: ULeah une ushokoledi ezingama-32 kanti udadewabo wakhe une ushokoledi ezingama-42. Badle ushokoledi ezingama-35. Manje ushokoledi esele zingaki?
    Understanding:
    1. ULeah une ushokoledi ezingama-32 kanti udadewabo wakhe une ushokoledi ezingama-42. means Leah has thirty‑two chocolates and her sister has forty‑two.
    2. Badle ushokoledi ezingama-35. means They ate thirty‑five chocolates.
    3. Manje ushokoledi esele zingaki? means How many chocolates remain?
    '''
]











