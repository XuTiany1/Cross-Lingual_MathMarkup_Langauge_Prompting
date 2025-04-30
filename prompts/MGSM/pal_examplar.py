###############
# EN examplar
##############


es_example_list = [
    ''' 
        #Roger empezó con 5 pelotas de tenis. 
        tennis_balls = 5 
        #2 latas de 3 pelotas de tenis cada una son 
        bought_balls = 2 * 3 tennis balls 
        #La respuesta es 
        answer = tennis_balls + bought_balls 
        return answer
        #La respuesta es 11''',
    ''' 
        #Inicialmente, había 9 computadoras en la sala de servidores. 
        initial_computers = 9 
        #De lunes a jueves hay 4 días. 
        days = 4 
        #Se añadieron 5 computadoras cada día 
        added_computers_per_day = 5 
        #El número total de computadoras añadidas es 
        days * added_computers_per_day = 4 * 5 = 20 
        #El número total de computadoras en la sala de servidores es 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #La respuesta es 29.''',
    ''' 
        #Inicialmente, hay 3 coches. 
        initial_cars = 3 
        #Llegan 2 coches más. 
        arriving_cars = 2 
        #El número total de coches en el estacionamiento es 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #La respuesta es 5.''',
    ''' 
        #Shawn tiene 5 juguetes. 
        initial_toys = 5 
        #Recibió 2 juguetes de su mamá 
        initial_toys + 2 = 5 + 2 = 7 juguetes. 
        #Recibió 2 juguetes más de su papá, ahora tiene 
        answer = 7 + 2 = 9 juguetes en total. 
        return answer
        #La respuesta es 9.''',
    ''' 
        #Michael empezó con 58 pelotas de golf
        initial_balls = 58
        #El martes perdió 23 pelotas de golf.
        lost_on_tuesday = 23
        #El miércoles perdió 2 pelotas de golf más.
        lost_on_wednesday = 2
        #Por lo tanto, al final del miércoles, tiene 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #La respuesta es 33.''',
    ''' 
        #El monto inicial de dinero de Olivia era initial_money.
        initial_money = 23 
        #Compró cinco bagels por $3 cada uno 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Después de comprar los bagels, Olivia tiene 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #La respuesta es 8.''',
    ''' 
        #Leah tenía 32 y el número de chocolates de su hermana era 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Si comieron 35 chocolates 
        eaten_chocolates = 35 
        #El número restante de chocolates es 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #La respuesta es 39.'''
]


vai_example_list = [
    ''' 
        #ꖄꔠr sꕚrꔎd ꔨth 5 ꔎnꕇs ꕑlls꘎ 
        tennis_balls = 5 
        #2 cꕉns ꕱf 3 ꔎnꕇs ꕑlls ꔀꕉch ꔤs 
        bought_balls = 2 * 3 tennis balls 
        #Tꔂ ꕉnsꔃr ꔤs 
        answer = tennis_balls + bought_balls 
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 11''',
    ''' 
        #ꔤꕇꔳꕉlly꘍ tꔂꔓ ꔃꔓ 9 cꕱmꖛꔎrs ꔤn tꔂ ꔖrꔍr ꖄꕱm꘎ 
        initial_computers = 9 
        #Fꖄm ꖒnꕜy ꕿ Tꖗrsꕜy꘍ tꔂꔓ ꕉꔓ 4 ꕜys꘎ 
        days = 4 
        #5 cꕱmꖛꔎrs ꔃꔓ ꕉdꔐd ꔀꕉch ꕜy 
        added_computers_per_day = 5 
        #Tꔂ ꕿꕚl ꖸmꔆr ꕱf cꕱmꖛꔎrs ꕉdꔐd ꔤs 
        days * added_computers_per_day = 4 * 5 = 20 
        #ꕿꕚl ꖸmꔆr ꕱf cꕱmꖛꔎrs ꔤn tꔂ ꔖrꔍr ꖄꕱm ꔤs 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 29꘎''',
    ''' 
        #ꔤꕇꔳꕉlly꘍ tꔂꔓ ꕉꔓ 3 cꕉrs꘎
        initial_cars = 3 
        #2 ꖒꔓ cꕉrs ꕉrꔸꔍ꘎ 
        arriving_cars = 2 
        #ꕿꕚl ꖸmꔆr ꕱf cꕉrs ꔤn tꔂ ꕐrꕃng ꖃt ꔤs 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 5꘎''',
    ''' 
        #Sꕌwn ꕌs 5 ꕿys꘎ 
        initial_toys = 5 
        #ꔂ ꖑt 2 ꕿys fꖄm ꔦs ꖒm 
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #ꔂ ꖑt 2 ꖒꔓ ꕿys fꖄm ꔦs ꕜd꘍ ꖇ ꖓw ꔂ ꕌs 
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 9꘎''',
    ''' 
        #ꕆꕦꔀl sꕚrꔎd ꔨth 58 ꖑlf ꕑlls
        initial_balls = 58
        #ꕱn ꖤꔀsꕜy꘍ ꔂ ꖃst 23 ꖑlf ꕑlls꘎
        lost_on_tuesday = 23
        #ꕱn ꔃdꔢsꕜy꘍ ꔂ ꖃst 2 ꖒꔓ ꖑlf ꕑlls꘎
        lost_on_wednesday = 2
        #Tꔂꔓꕽꔓ꘍ ꕉt tꔂ ꔀnd ꕱf ꔃdꔢsꕜy꘍ ꔂ ꕌs 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 33꘎''',
    ''' 
        #ꕱꔷꔲꕉ's ꔤꕇꔳꕉl ꕉꖒꖕnt ꕱf ꖒꔢy ꕉs ꔤꕇꔳꕉl_ꖒꔢy꘎
        initial_money = 23 
        #Sꔂ ꕷꖕght ꔱꔍ ꕑꔠls ꕽr $3 ꔀꕉch 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #ꕉfꔎr ꖜꕂng tꔂ ꕑꔠls꘍ ꕱꔷꔲꕉ ꕌs 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 8꘎''',
    ''' 
        #ꔒꕉh ꕌd ꕉs 32 ꕉnd tꔂ ꖸmꔆr ꕱf ꖋcꕱꕞꔎs ꔂr ꔻsꔎr ꕌd ꕉs 42꘎ 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #ꔤf tꔂy ꕉꔎ 35 ꖋcꕱꕞꔎs 
        eaten_chocolates = 35 
        #Tꔂ ꔓꕮꔤꕇng ꖸmꔆr ꕱf ꖋcꕱꕞꔎs ꔤs 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Tꔂ ꕉnsꔃr ꔤs 39꘎'''              
]

en_example_list = [
    ''' 
        #Roger started with 5 tennis balls. 
        tennis_balls = 5 
        #2 cans of 3 tennis balls each is 
        bought_balls = 2 * 3 tennis balls 
        #The answer is 
        answer = tennis_balls + bought_balls 
        return answer
        #The answer is 11''',
    ''' 
        #Initially, there were 9 computers in the server room. 
        initial_computers = 9 
        #From Monday to Thursday, there are 4 days. 
        days = 4 
        #5 computers were added each day 
        added_computers_per_day = 5 
        #The total number of computers added is 
        days * added_computers_per_day = 4 * 5 = 20 
        #total number of computers in the server room is 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #The answer is 29.''',
    ''' 
        #Initially, there are 3 cars.
        initial_cars = 3 
        #2 more cars arrive. 
        arriving_cars = 2 
        #total number of cars in the parking lot is 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #The answer is 5.''',
    ''' 
        #Shawn has 5 toys. 
        initial_toys = 5 
        #He got 2 toys from his mom 
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #He got 2 more toys from his dad, so now he has 
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #The answer is 9.''',
    ''' 
        #Michael started with 58 golf balls
        initial_balls = 58
        #On Tuesday, he lost 23 golf balls.
        lost_on_tuesday = 23
        #On Wednesday, he lost 2 more golf balls.
        lost_on_wednesday = 2
        #Therefore, at the end of Wednesday, he has 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #The answer is 33.''',
    ''' 
        #Olivia's initial amount of money as initial_money.
        initial_money = 23 
        #She bought five bagels for $3 each 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #After buying the bagels, Olivia has 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #The answer is 8.''',
    ''' 
        #Leah had as 32 and the number of chocolates her sister had as 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #If they ate 35 chocolates 
        eaten_chocolates = 35 
        #The remaining number of chocolates is 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #The answer is 39.'''              
]

fr_example_list = [
    ''' 
        #Roger a commencé avec 5 balles de tennis.
        tennis_balls = 5 
        #2 boîtes de 3 balles de tennis chacune donnent 
        bought_balls = 2 * 3
        #La réponse est 
        answer = tennis_balls + bought_balls 
        return answer
        #La réponse est 11''',
    ''' 
        #Initialement, il y avait 9 ordinateurs dans la salle des serveurs.
        initial_computers = 9 
        #Du lundi au jeudi, il y a 4 jours.
        days = 4 
        #5 ordinateurs ont été ajoutés chaque jour 
        added_computers_per_day = 5 
        #Le nombre total d'ordinateurs ajoutés est 
        days * added_computers_per_day = 4 * 5 = 20 
        #Le nombre total d'ordinateurs dans la salle des serveurs est 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #La réponse est 29.''',
    ''' 
        #Initialement, il y a 3 voitures.
        initial_cars = 3 
        #2 voitures supplémentaires arrivent.
        arriving_cars = 2 
        #Le nombre total de voitures dans le parking est 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #La réponse est 5.''',
    ''' 
        #Shawn a 5 jouets.
        initial_toys = 5 
        #Il a reçu 2 jouets de sa mère 
        initial_toys + 2 = 5 + 2 = 7 jouets. 
        #Il a reçu 2 jouets de plus de son père, donc il a maintenant 
        answer = 7 + 2 = 9 jouets au total. 
        return answer
        #La réponse est 9.''',
    ''' 
        #Michael a commencé avec 58 balles de golf.
        initial_balls = 58
        #Mardi, il a perdu 23 balles de golf.
        lost_on_tuesday = 23
        #Mercredi, il a perdu 2 balles de golf supplémentaires.
        lost_on_wednesday = 2
        #Donc, à la fin de mercredi, il a 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #La réponse est 33.''',
    ''' 
        #Le montant initial d'argent d'Olivia était initial_money.
        initial_money = 23 
        #Elle a acheté cinq bagels à 3 $ chacun 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Après avoir acheté les bagels, Olivia a 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #La réponse est 8.''',
    ''' 
        #Leah avait 32 et le nombre de chocolats que sa sœur possédait était 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #S'ils ont mangé 35 chocolats 
        eaten_chocolates = 35 
        #Le nombre restant de chocolats est 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #La réponse est 39.'''
]


zh_example_list = [
    ''' 
        # 罗杰开始时有5个网球
        tennis_balls = 5 
        # 2罐每罐3个网球
        bought_balls = 2 * 3 tennis balls 
        # 答案是
        answer = tennis_balls + bought_balls 
        return answer
        # 答案是11''',
    ''' 
        # 起初，服务器室里有9台电脑
        initial_computers = 9 
        # 从星期一到星期四共有4天
        days = 4 
        # 每天增加5台电脑
        added_computers_per_day = 5 
        # 增加的电脑总数是
        days * added_computers_per_day = 4 * 5 = 20 
        # 服务器室的电脑总数是
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # 答案是29''',
    ''' 
        # 起初有3辆车
        initial_cars = 3 
        # 又来了2辆车
        arriving_cars = 2 
        # 停车场的车辆总数是
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # 答案是5''',
    ''' 
        # 肖恩有5个玩具
        initial_toys = 5 
        # 他从妈妈那里得到2个玩具
        initial_toys + 2 = 5 + 2 = 7 toys. 
        # 他从爸爸那里又得到了2个玩具，现在他总共有
        answer = 7 + 2 = 9 toys in total. 
        return answer
        # 答案是9''',
    ''' 
        # 迈克尔起初有58个高尔夫球
        initial_balls = 58
        # 星期二他丢了23个高尔夫球
        lost_on_tuesday = 23
        # 星期三他又丢了2个高尔夫球
        lost_on_wednesday = 2
        # 因此，在星期三结束时，他有
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # 答案是33''',
    ''' 
        # 奥利维亚的初始金额为初始金额
        initial_money = 23 
        # 她花了$3买了5个百吉饼
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # 买完百吉饼后，奥利维亚还剩
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # 答案是8''',
    ''' 
        # 莱娅有32个巧克力，她的妹妹有42个
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # 如果他们吃了35个巧克力
        eaten_chocolates = 35 
        # 剩下的巧克力数量是
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # 答案是39'''
]


de_example_list = [
    ''' 
        # Roger begann mit 5 Tennisbällen. 
        tennis_balls = 5 
        # 2 Dosen mit jeweils 3 Tennisbällen sind 
        bought_balls = 2 * 3 Tennisbälle 
        # Die Antwort ist 
        answer = tennis_balls + bought_balls 
        return answer
        # Die Antwort ist 11''',
    ''' 
        # Anfangs gab es 9 Computer im Serverraum. 
        initial_computers = 9 
        # Von Montag bis Donnerstag gibt es 4 Tage. 
        days = 4 
        # Es wurden täglich 5 Computer hinzugefügt 
        added_computers_per_day = 5 
        # Die Gesamtzahl der hinzugefügten Computer beträgt 
        days * added_computers_per_day = 4 * 5 = 20 
        # Die Gesamtzahl der Computer im Serverraum beträgt 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # Die Antwort ist 29.''',
    ''' 
        # Anfangs gab es 3 Autos. 
        initial_cars = 3 
        # Es kamen 2 weitere Autos an. 
        arriving_cars = 2 
        # Die Gesamtzahl der Autos auf dem Parkplatz beträgt 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # Die Antwort ist 5.''',
    ''' 
        # Shawn hat 5 Spielzeuge. 
        initial_toys = 5 
        # Er bekam 2 Spielzeuge von seiner Mutter 
        initial_toys + 2 = 5 + 2 = 7 Spielzeuge. 
        # Er bekam 2 weitere Spielzeuge von seinem Vater, jetzt hat er insgesamt 
        answer = 7 + 2 = 9 Spielzeuge. 
        return answer
        # Die Antwort ist 9.''',
    ''' 
        # Michael begann mit 58 Golfbällen
        initial_balls = 58
        # Am Dienstag verlor er 23 Golfbälle.
        lost_on_tuesday = 23
        # Am Mittwoch verlor er 2 weitere Golfbälle.
        lost_on_wednesday = 2
        # Also hat er am Ende des Mittwochs 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # Die Antwort ist 33.''',
    ''' 
        # Olivia's Anfangsbetrag an Geld als initial_money.
        initial_money = 23 
        # Sie kaufte fünf Bagels für je $3 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # Nach dem Kauf der Bagels hat Olivia 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # Die Antwort ist 8.''',
    ''' 
        # Leah hatte 32 und die Anzahl der Schokoladen, die ihre Schwester hatte, war 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # Wenn sie 35 Schokoladen gegessen haben 
        eaten_chocolates = 35 
        # Die verbleibende Anzahl von Schokoladen ist 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # Die Antwort ist 39.'''
]

ja_example_list = [
    ''' 
        # ロジャーは5個のテニスボールから始めました。 
        tennis_balls = 5 
        # 3個ずつの2缶は 
        bought_balls = 2 * 3 テニスボール 
        # 答えは 
        answer = tennis_balls + bought_balls 
        return answer
        # 答えは11''',
    ''' 
        # 最初は、サーバールームに9台のコンピュータがありました。 
        initial_computers = 9 
        # 月曜日から木曜日まで、4日間です。 
        days = 4 
        # 1日に5台のコンピュータが追加されました 
        added_computers_per_day = 5 
        # 追加されたコンピュータの合計数は 
        days * added_computers_per_day = 4 * 5 = 20 
        # サーバールームのコンピュータの合計は 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # 答えは29.''',
    ''' 
        # 最初は車が3台ありました。 
        initial_cars = 3 
        # 2台の車が追加されました。 
        arriving_cars = 2 
        # 駐車場の車の合計は 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # 答えは5.''',
    ''' 
        # ショーンは5つのおもちゃを持っています。 
        initial_toys = 5 
        # 彼は母親からおもちゃを2つもらいました 
        initial_toys + 2 = 5 + 2 = 7 おもちゃ。 
        # 彼はさらに2つのおもちゃを父親からもらい、合計で 
        answer = 7 + 2 = 9 個のおもちゃを持っています。 
        return answer
        # 答えは9.''',
    ''' 
        # マイケルは58個のゴルフボールで始めました
        initial_balls = 58
        # 火曜日に23個のゴルフボールを失いました。
        lost_on_tuesday = 23
        # 水曜日にさらに2個のゴルフボールを失いました。
        lost_on_wednesday = 2
        # したがって、水曜日の終わりには、彼は 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # 答えは33.''',
    ''' 
        # オリビアの初期金額はinitial_moneyです。
        initial_money = 23 
        # 彼女は1つあたり$3のベーグルを5つ買いました 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # ベーグルを購入した後、オリビアは 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # 答えは8.''',
    ''' 
        # リアは32個、彼女の妹は42個のチョコレートを持っていました。 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # 彼らが35個のチョコレートを食べた場合 
        eaten_chocolates = 35 
        # 残りのチョコレートの数は 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # 答えは39'''
]


bn_example_list = [
    ''' 
        #রজার সাথে ৫টি টেনিস বল ছিল। 
        tennis_balls = 5 
        # ২টি ক্যান প্রতি ক্যানে ৩টি টেনিস বল আছে 
        bought_balls = 2 * 3 tennis balls 
        # উত্তর হল 
        answer = tennis_balls + bought_balls 
        return answer
        # উত্তর হল ১১''',
    ''' 
        #প্রাথমিকভাবে, সার্ভার রুমে ৯টি কম্পিউটার ছিল। 
        initial_computers = 9 
        # সোমবার থেকে বৃহস্পতিবার পর্যন্ত, ৪টি দিন আছে। 
        days = 4 
        # প্রতি দিন ৫টি কম্পিউটার যোগ করা হয়েছে 
        added_computers_per_day = 5 
        # যোগ করা কম্পিউটারের মোট সংখ্যা 
        days * added_computers_per_day = 4 * 5 = 20 
        # সার্ভার রুমে মোট কম্পিউটারের সংখ্যা 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # উত্তর হল ২৯.''',
    ''' 
        #প্রাথমিকভাবে, ৩টি গাড়ি ছিল। 
        initial_cars = 3 
        # ২টি আরও গাড়ি আসছে। 
        arriving_cars = 2 
        # পার্কিংয়ে গাড়ির মোট সংখ্যা 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # উত্তর হল ৫.''',
    ''' 
        #শওনের কাছে ৫টি খেলনা আছে। 
        initial_toys = 5 
        # তিনি তার মা থেকে ২টি খেলনা পেয়েছিলেন 
        initial_toys + 2 = 5 + 2 = 7 টি খেলনা। 
        # তিনি তার বাবা থেকে আরও ২টি খেলনা পেয়েছিলেন, এখন তার মোটে 
        answer = 7 + 2 = 9 টি খেলনা আছে। 
        return answer
        # উত্তর হল ৯.''',
    ''' 
        #মাইকেল ৫৮টি গল্ফ বল দিয়ে শুরু করেছিলেন
        initial_balls = 58
        # মঙ্গলবার তিনি ২৩টি গল্ফ বল হারিয়েছিলেন।
        lost_on_tuesday = 23
        # বুধবার তিনি আরো ২টি গল্ফ বল হারিয়েছিলেন।
        lost_on_wednesday = 2
        # তাই, মঙ্গলবারের শেষে, তার কাছে আছে 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # উত্তর হল ৩৩.''',
    ''' 
        #অলিভিয়ার প্রাথমিক টাকা পরিমাণ হচ্ছে initial_money।
        initial_money = 23 
        # তিনি প্রতি টাকায় ৩ টি বেগেল কিনলেন 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # বেগেল কিনার পরে, অলিভিয়ার কাছে হচ্ছে 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # উত্তর হল ৮.''',
    ''' 
        # লিয়ার কাছে ৩২টি চকোলেট ছিল এবং তার বোনের কাছে ছিল ৪২টি। 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # যদিও তারা ৩৫টি চকোলেট খায়। 
        eaten_chocolates = 35 
        # বাকি থাকা চকোলেটের সংখ্যা হচ্ছে 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # উত্তর হল ৩৯'''
]


sw_example_list = [
    ''' 
        #Roger alianza na mipira ya tenisi 5. 
        tennis_balls = 5 
        #Viboko vya 2 kila kimoja na mipira ya tenisi 3 ni 
        bought_balls = 2 * 3 tennis balls 
        #Jibu ni 
        answer = tennis_balls + bought_balls 
        return answer
        #Jibu ni 11''',
    ''' 
        #Kwa mwanzo, kulikuwa na kompyuta 9 kwenye chumba cha seva. 
        initial_computers = 9 
        #Kuanzia Jumatatu hadi Alhamisi, kuna siku 4. 
        days = 4 
        #Kompyuta 5 ziliwekwa kila siku 
        added_computers_per_day = 5 
        #Jumla ya kompyuta zilizoongezwa ni 
        days * added_computers_per_day = 4 * 5 = 20 
        #Jumla ya kompyuta kwenye chumba cha seva ni 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Jibu ni 29.''',
    ''' 
        #Kwa mwanzo, kulikuwa na magari 3. 
        initial_cars = 3 
        #Magari 2 zaidi yalifika. 
        arriving_cars = 2 
        #Jumla ya magari kwenye maegesho ni 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Jibu ni 5.''',
    ''' 
        #Shawn ana vitu vya kuchezea 5. 
        initial_toys = 5 
        #Alipata vitu vya kuchezea 2 kutoka kwa mama yake 
        initial_toys + 2 = 5 + 2 = 7 vitu vya kuchezea. 
        #Alipata vitu vingine 2 kutoka kwa baba yake, sasa ana 
        answer = 7 + 2 = 9 vitu vya kuchezea jumla. 
        return answer
        #Jibu ni 9.''',
    ''' 
        #Michael alianza na mipira ya gofu 58
        initial_balls = 58
        #Jumanne, alipoteza mipira ya gofu 23.
        lost_on_tuesday = 23
        #Jumatano, alipoteza mipira mingine 2 ya gofu.
        lost_on_wednesday = 2
        #Kwa hivyo, mwisho wa Jumatano, ana 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Jibu ni 33.''',
    ''' 
        #Kiasi cha awali cha pesa cha Olivia kama initial_money.
        initial_money = 23 
        #Alijua mikate mitano kwa $3 kila moja 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Baada ya kununua mikate ya bageli, Olivia 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Jibu ni 8.''',
    ''' 
        #Leah alikuwa na 32 na idadi ya chokoleti dada yake alikuwa na 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Ikiwa walila chokoleti 35 
        eaten_chocolates = 35 
        #Idadi ya chokoleti zilizobaki ni 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Jibu ni 39'''
]

ru_example_list = [
    ''' 
        # Роджер начал с 5 теннисных мячей. 
        tennis_balls = 5 
        # 2 банки по 3 теннисных мяча каждая 
        bought_balls = 2 * 3 теннисных мяча 
        # Ответ 
        answer = tennis_balls + bought_balls 
        return answer
        # Ответ 11''',
    ''' 
        # Изначально в серверной комнате было 9 компьютеров. 
        initial_computers = 9 
        # С понедельника по четверг 4 дня. 
        days = 4 
        # Каждый день добавляется 5 компьютеров 
        added_computers_per_day = 5 
        # Общее количество добавленных компьютеров 
        days * added_computers_per_day = 4 * 5 = 20 
        # Общее количество компьютеров в серверной комнате 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        # Ответ 29.''',
    ''' 
        # Изначально было 3 машины. 
        initial_cars = 3 
        # Прибыли еще 2 машины. 
        arriving_cars = 2 
        # Общее количество машин на парковке 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        # Ответ 5.''',
    ''' 
        # У Шона было 5 игрушек. 
        initial_toys = 5 
        # Он получил 2 игрушки от мамы. 
        initial_toys + 2 = 5 + 2 = 7 игрушек. 
        # Затем он получил еще 2 игрушки от папы, теперь у него всего 
        answer = 7 + 2 = 9 игрушек. 
        return answer
        # Ответ 9.''',
    ''' 
        # Майкл начал с 58 гольф-мячами
        initial_balls = 58
        # Во вторник он потерял 23 гольф-мяча.
        lost_on_tuesday = 23
        # В среду он потерял еще 2 гольф-мяча.
        lost_on_wednesday = 2
        # Таким образом, к концу среды у него есть 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        # Ответ 33.''',
    ''' 
        # Исходная сумма денег у Оливии как начальные деньги.
        initial_money = 23 
        # Она купила пять бубликов по $3 каждый 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        # После покупки бубликов у Оливии есть 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        # Ответ 8.''',
    ''' 
        # У Лии было 32 и количество шоколадок у ее сестры было 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        # Если они съели 35 шоколадок 
        eaten_chocolates = 35 
        # Осталось 
        answer = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        # Ответ 39.''',
    ''' 
        # Начальное количество яблок у Сергея 
        initial_apples = 37 
        # Он съел 4 яблока вечером 
        eaten_evening = 4 
        # И 2 яблока утром следующего дня. 
        eaten_morning_next_day = 2 
        # Сколько яблок осталось у Сергея? 
        answer = initial_apples - eaten_evening - eaten_morning_next_day = 37 - 4 - 2 = 31 
        return answer
        # Ответ 31.''',
    ''' 
        # Сумма денег, которая была у Михаила изначально.
        initial_money = 98
        # Он потратил 19 долларов на новую рубашку.
        spent_on_shirt = 19
        # И 25 долларов на новые джинсы.
        spent_on_jeans = 25
        # Оставшаяся у него сумма денег:
        answer = initial_money - spent_on_shirt - spent_on_jeans = 98 - 19 - 25 = 54
        return answer
        # Ответ 54.''',
    ''' 
        # У Миши было 14 батонов хлеба.
        initial_bread_loaves = 14
        # Он купил еще 8 батонов.
        bought_bread_loaves = 8
        # После покупки у него было всего:
        answer = initial_bread_loaves + bought_bread_loaves = 14 + 8 = 22.
        return answer
        # Ответ 22.'''
]

th_example_list = [
    ''' 
        # โรเจอร์เริ่มต้นด้วยลูกเทนนิส 5 ลูก 
        tennis_balls = 5 
        # ซื้อเพิ่ม 2 กระป๋อง แต่ละกระป๋องมีลูกเทนนิส 3 ลูก 
        bought_balls = 2 * 3 
        # คำตอบคือ 
        answer = tennis_balls + bought_balls 
        return answer
        # คำตอบคือ 11''',
    ''' 
        # เริ่มต้นด้วยคอมพิวเตอร์ 9 เครื่องในห้องเซิร์ฟเวอร์ 
        initial_computers = 9 
        # มี 4 วัน ตั้งแต่วันจันทร์ถึงวันพฤหัสบดี 
        days = 4 
        # เพิ่มคอมพิวเตอร์ 5 เครื่องต่อวัน 
        added_computers_per_day = 5 
        # จำนวนคอมพิวเตอร์ที่เพิ่มขึ้นทั้งหมด 
        total_added_computers = days * added_computers_per_day 
        # จำนวนคอมพิวเตอร์ทั้งหมดในห้องเซิร์ฟเวอร์ 
        answer = initial_computers + total_added_computers 
        return answer
        # คำตอบคือ 29''',
    ''' 
        # เริ่มต้นด้วยรถยนต์ 3 คัน 
        initial_cars = 3 
        # มีรถยนต์เพิ่มเข้ามาอีก 2 คัน 
        arriving_cars = 2 
        # จำนวนรถยนต์ทั้งหมดในที่จอด 
        answer = initial_cars + arriving_cars 
        return answer
        # คำตอบคือ 5''',
    ''' 
        # ชอว์นมีของเล่นอยู่ 5 ชิ้น 
        initial_toys = 5 
        # เขาได้รับของเล่นเพิ่ม 2 ชิ้นจากแม่ 
        # ต่อมาเขาได้รับของเล่นเพิ่มอีก 2 ชิ้นจากพ่อ 
        answer = initial_toys + 2 + 2 
        return answer
        # คำตอบคือ 9''',
    ''' 
        # ไมเคิลเริ่มต้นด้วยกอล์ฟบอล 58 ลูก 
        initial_balls = 58
        # เขาสูญเสียกอล์ฟบอล 23 ลูกในวันอังคาร 
        # และเสียอีก 2 ลูกในวันพุธ 
        answer = initial_balls - 23 - 2
        return answer
        # คำตอบคือ 33''',
    ''' 
        # โอลิเวียเริ่มต้นด้วยเงิน 23 บาท 
        initial_money = 23 
        # เธอซื้อเบเกิล 15 ชิ้นด้วยเงินทั้งหมด 
        total_cost_bagels = 15 
        # จำนวนเงินที่เหลือหลังจากซื้อเบเกิล 
        answer = initial_money - total_cost_bagels 
        return answer
        # คำตอบคือ 8''',
    ''' 
        # ลีอามีช็อกโกแลต 32 ชิ้นและน้องสาวเธอมี 42 ชิ้น 
        leah_chocolates = 32 
        sister_chocolates = 42 
        # พวกเขาทานช็อกโกแลตไป 35 ชิ้น 
        eaten_chocolates = 35 
        # จำนวนช็อกโกแลตที่เหลือ 
        remaining_chocolates = (leah_chocolates + sister_chocolates) - eaten_chocolates 
        return remaining_chocolates
        # คำตอบคือ 39'''
]


te_example_list = [
    ''' 
        # రోజర్ వద్ద 5 టెన్నిస్ బాల్స్ ఉన్నాయి. 
        tennis_balls = 5 
        # 2 టిన్నులు కొన్నారు, ప్రతి టిన్నులో 3 టెన్నిస్ బాల్స్ ఉన్నాయి 
        bought_balls = 2 * 3 
        # సమాధానం 
        answer = tennis_balls + bought_balls 
        return answer
        # సమాధానం 11''',
    ''' 
        # సర్వర్ గదిలో మొదట 9 కంప్యూటర్లు ఉన్నాయి. 
        initial_computers = 9 
        # సోమవారం నుండి గురువారం వరకు 4 రోజులు ఉన్నాయి. 
        days = 4 
        # ప్రతి రోజు 5 కంప్యూటర్లు చేర్చబడ్డాయి 
        added_computers_per_day = 5 
        # మొత్తం చేర్చబడిన కంప్యూటర్ల సంఖ్య 
        total_added_computers = days * added_computers_per_day 
        # సర్వర్ గదిలో మొత్తం కంప్యూటర్ల సంఖ్య 
        answer = initial_computers + total_added_computers 
        return answer
        # సమాధానం 29''',
    ''' 
        # ప్రారంభంలో 3 కార్లు ఉన్నాయి. 
        initial_cars = 3 
        # మరియు 2 కొత్త కార్లు రాబట్టబడ్డాయి. 
        arriving_cars = 2 
        # పార్కింగ్ లోట్ లో మొత్తం కార్ల సంఖ్య 
        answer = initial_cars + arriving_cars 
        return answer
        # సమాధానం 5''',
    ''' 
        # షాన్ వద్ద 5 బొమ్మలు ఉన్నాయి. 
        initial_toys = 5 
        # అతను తన తల్లి నుండి 2 బొమ్మలు పొందాడు 
        # అనంతరం తన తండ్రి నుండి మరొక 2 బొమ్మలు పొందాడు 
        answer = initial_toys + 2 + 2 
        return answer
        # సమాధానం 9''',
    ''' 
        # మైకేల్ గోల్ఫ్ బంతులతో 58 మొదలుపెట్టాడు 
        initial_balls = 58
        # అతను మంగళవారం 23 గోల్ఫ్ బంతులు కోల్పోయాడు 
        # బుధవారం మరో 2 బంతులు కోల్పోయాడు 
        answer = initial_balls - 23 - 2
        return answer
        # సమాధానం 33''',
    ''' 
        # ఒలివియా వద్ద ప్రారంభ నగదు 23 రూపాయలు 
        initial_money = 23 
        # ఆమె 15 బేగల్స్ కొనుగోలు కోసం ఖర్చుచేసిన మొత్తం ధర 
        total_cost_bagels = 15 
        # బేగల్స్ కొనుగోలు అనంతరం మిగిలిన నగదు 
        answer = initial_money - total_cost_bagels 
        return answer
        # సమాధానం 8''',
    ''' 
        # లియా వద్ద 32 చాక్లెట్లు మరియు ఆమె సోదరి వద్ద 42 చాక్లెట్లు ఉన్నాయి 
        leah_chocolates = 32 
        sister_chocolates = 42 
        # వారు 35 చాక్లెట్లు తిన్నారు 
        eaten_chocolates = 35 
        # మిగిలిన చాక్లెట్ల సంఖ్య 
        remaining_chocolates = (leah_chocolates + sister_chocolates) - eaten_chocolates 
        return remaining_chocolates
        # సమాధానం 39'''
]





###############
# AFRIMGSM examplar
##############


amh_example_list = [
    ''' 
        #ሮጀር በ 5 የቴኒስ ኳሶች ጀመረ። 
        tennis_balls = 5 
        #እያንዳንዳቸው 3 የቴኒስ ኳሶች 2 ጣሳዎች
        bought_balls = 2 * 3 tennis balls 
        #መልሱ ነው።
        answer = tennis_balls + bought_balls 
        return answer
        #መልሱ 11 ነው።''',
    ''' 
        #መጀመሪያ ላይ በአገልጋዩ ክፍል ውስጥ 9 ኮምፒውተሮች ነበሩ።
        initial_computers = 9 
        #ከሰኞ እስከ ሐሙስ 4 ቀናት አሉ። 
        days = 4 
        #በየቀኑ 5 ኮምፒውተሮች ተጨመሩ
        added_computers_per_day = 5 
        #ጠቅላላ የተጨመሩ ኮምፒውተሮች ብዛት ነው።
        days * added_computers_per_day = 4 * 5 = 20 
        #በአገልጋዩ ክፍል ውስጥ ያሉት አጠቃላይ የኮምፒዩተሮች ብዛት
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #መልሱ 29 ነው።''',
    ''' 
        #መጀመሪያ ላይ 3 መኪኖች አሉ.
        initial_cars = 3 
        #2 ተጨማሪ መኪኖች መጡ።
        arriving_cars = 2 
        #በመኪና ማቆሚያ ቦታ ውስጥ ያሉት አጠቃላይ የመኪናዎች ብዛት
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #መልሱ 5 ነው።''',
    ''' 
        #Shawn 5 መጫወቻዎች አሉት. 
        initial_toys = 5 
        #ከእናቱ 2 መጫወቻዎችን አግኝቷል
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #ከአባቱ 2 ተጨማሪ መጫወቻዎችን አግኝቷል, ስለዚህ አሁን አለው 
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #መልሱ 9 ነው።''',
    ''' 
        #ማይክል በ58 የጎልፍ ኳሶች ጀመረ
        initial_balls = 58
        #ማክሰኞ 23 የጎልፍ ኳሶችን አጥቷል።
        lost_on_tuesday = 23
        #እሮብ እለት 2 ተጨማሪ የጎልፍ ኳሶችን አጥቷል።
        lost_on_wednesday = 2
        #ስለዚህ, እሮብ መጨረሻ ላይ, እሱ አለው
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #መልሱ 33 ነው።''',
    ''' 
        #የኦሊቪያ የመጀመሪያ የገንዘብ መጠን እንደ መጀመሪያ_ገንዘብ።
        initial_money = 23 
        #አምስት ቦርሳዎችን እያንዳንዳቸው በ3 ዶላር ገዛች።
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #ሻንጣዎቹን ከገዙ በኋላ ኦሊቪያ አላት 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #መልሱ 8 ነው።''',
    ''' 
        #ሊያ ዕድሜዋ 32 ሲሆን እህቷ የነበራት የቸኮሌት ብዛት 42 ነበር። 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #35 ቸኮሌት ከበሉ
        eaten_chocolates = 35 
        #የተቀረው የቸኮሌት ብዛት ነው። 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #መልሱ 39 ነው።'''              
]


ewe_example_list = [
    ''' 
        #Roger dze egɔme kple tenisbɔl 5. 
        tennis_balls = 5 
        #2 gaze siwo me tenisbɔl 3 le ɖesiaɖe nye
        bought_balls = 2 * 3 tennis balls 
        #Ŋuɖoɖoae nye be
        answer = tennis_balls + bought_balls 
        return answer
        #Ŋuɖoɖoae nye 11''',
    ''' 
        #Le gɔmedzedzea me la, kɔmpiuta 9 ye nɔ server room la me.
        initial_computers = 9 
        #Tso Memleɖa vaseɖe Yawoɖa, ŋkeke 4 ye nɔa anyi.
        days = 4 
        #Wotsɔa kɔmpiuta 5 kpena ɖe eŋu gbesiagbe
        added_computers_per_day = 5 
        #Kɔmpiuta siwo wotsɔ kpe ɖe eŋu ƒe xexlẽme katã nye
        days * added_computers_per_day = 4 * 5 = 20 
        #kɔmpiuta siwo katã le server xɔa me ƒe xexlẽme katã nye
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Ŋuɖoɖoae nye 29.''',
    ''' 
        #Le gɔmedzedzea me la, ʋu 3 ye nɔa anyi.
        initial_cars = 3 
        #Ʋu 2 bubuwo va ɖo. 
        arriving_cars = 2 
        #ʋu siwo katã le ʋutɔɖoƒea ƒe xexlẽme nye
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Ŋuɖoɖoae nye 5.''',
    ''' 
        #Fefenu 5 le Shawn si. 
        initial_toys = 5 
        #Exɔ fefenu 2 tso dadaa gbɔ
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Exɔ fefenu 2 bubu tso fofoa gbɔ, eyata fifia exɔe
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Ŋuɖoɖoae nye 9.''',
    ''' 
        #Michael dze egɔme kple golf-bɔl 58
        initial_balls = 58
        #Le Kuɖagbe la, ebu golf-bɔl 23.
        lost_on_tuesday = 23
        #Le Braɖagbe la, ebu golf-bɔl 2 bubu.
        lost_on_wednesday = 2
        #Eyata le Braɖagbe ƒe nuwuwu la, ewɔe
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Ŋuɖoɖoae nye 33.''',
    ''' 
        #Olivia ƒe ga home gbãtɔ abe ga_gɔmedzedze ene.
        initial_money = 23 
        #Eƒle bagel atɔ̃ ɖesiaɖe xɔ dɔlar 3
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Esi Olivia ƒle bagels-awo vɔ la, eƒlee
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Ŋuɖoɖoae nye 8.''',
    ''' 
        #Leah ƒe tsokolet ƒe xexlẽme nye 32 eye tsokolet agbɔsɔsɔme si nɔvianyɔnu nɔ si nye 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Ne woɖu tsokolet 35
        eaten_chocolates = 35 
        #Tsokolet ƒe xexlẽme susɔea nye
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Ŋuɖoɖoae nye 39.'''              
]


hau_example_list = [
    ''' 
        #Roger ya fara da kwallon tennis 5. 
        tennis_balls = 5 
        #Gwangwani 2 na ƙwallan tennis 3 kowanne yana
        bought_balls = 2 * 3 tennis balls 
        #Amsar ita ce
        answer = tennis_balls + bought_balls 
        return answer
        #Amsar ita ce 11''',
    ''' 
        #Da farko, akwai kwamfutoci 9 a cikin dakin uwar garken.
        initial_computers = 9 
        #Daga Litinin zuwa Alhamis, akwai kwanaki 4.
        days = 4 
        #An kara kwamfutoci 5 kowace rana
        added_computers_per_day = 5 
        #Jimlar adadin kwamfutoci da aka ƙara shine
        days * added_computers_per_day = 4 * 5 = 20 
        #jimlar yawan kwamfutoci a dakin uwar garken shine 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Amsar ita ce 29.''',
    ''' 
        #Da farko, akwai motoci 3.
        initial_cars = 3 
        #Karin motoci 2 sun iso. 
        arriving_cars = 2 
        #jimlar yawan motoci a filin ajiye motoci ne
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Amsar ita ce 5.''',
    ''' 
        #Shawn yana da kayan wasa 5.
        initial_toys = 5 
        #Ya samu kayan wasa 2 daga wajen mahaifiyarsa
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Ya sami karin kayan wasan yara guda 2 daga wurin mahaifinsa, don haka yanzu yana da
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Amsar ita ce 9.''',
    ''' 
        #Michael ya fara da kwallaye 58 na golf
        initial_balls = 58
        #A ranar Talata, ya yi asarar kwallaye 23 na golf.
        lost_on_tuesday = 23
        #A ranar Laraba, ya yi asarar karin kwallayen golf guda 2.
        lost_on_wednesday = 2
        #Saboda haka, a karshen Laraba, yana da
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Amsar ita ce 33.''',
    ''' 
        #Olivia ta farko adadin kudi kamar yadda initial_money.
        initial_money = 23 
        #Ta sayi jakunkuna biyar akan $3 kowanne
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Bayan siyan jakunkuna, Olivia tana da
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Amsar ita ce 8.''',
    ''' 
        #Leah tana da kamar 32 kuma adadin cakulan 'yar uwarta tana da 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Idan sun ci cakulan 35 
        eaten_chocolates = 35 
        #Sauran adadin cakulan shine 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Amsar ita ce 39.'''              
]


ibo_example_list = [
    ''' 
        #Roger ji bọọlụ tenis ise malite. 
        tennis_balls = 5 
        #Mkpọ 2 nke bọọlụ tenis 3 nke ọ bụla bụ
        bought_balls = 2 * 3 tennis balls 
        #Azịza ya bụ
        answer = tennis_balls + bought_balls 
        return answer
        #Azịza ya bụ 11''',
    ''' 
        #Na mbụ, e nwere kọmputa 9 n'ime ụlọ ihe nkesa.
        initial_computers = 9 
        #Site na Mọnde ruo Tọzdee, enwere ụbọchị 4.
        days = 4 
        #A na-agbakwunye kọmputa 5 kwa ụbọchị
        added_computers_per_day = 5 
        #Ngụkọta ọnụ ọgụgụ kọmputa agbakwunyere bụ
        days * added_computers_per_day = 4 * 5 = 20 
        #ngụkọta ọnụ ọgụgụ nke kọmputa na sava ụlọ bụ 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Azịza ya bụ 29.''',
    ''' 
        #Na mbụ, enwere ụgbọ ala 3.
        initial_cars = 3 
        #Ụgbọ ala 2 ọzọ bịarutere.
        arriving_cars = 2 
        #ngụkọta ọnụ ọgụgụ nke ụgbọ ala na-adọba ụgbọala bụ
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Azịza ya bụ 5.''',
    ''' 
        #Shawn nwere ihe egwuregwu ụmụaka 5.
        initial_toys = 5 
        #O nwetara ihe egwuregwu 2 n'aka nne ya
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #O nwetara ihe egwuregwu 2 ọzọ n'aka nna ya, yabụ ugbu a o nwere
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Azịza ya bụ 9.''',
    ''' 
        #Michael ji bọọlụ gọlfụ 58 malite
        initial_balls = 58
        #Na Tuesday, bọọlụ gọlfụ 23 tụfuru ya.
        lost_on_tuesday = 23
        #Na Wednesde, bọọlụ gọlfụ 2 ọzọ tụfuru ya.
        lost_on_wednesday = 2
        #Ya mere, na njedebe nke Wednesday, o nwere
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Azịza ya bụ 33.''',
    ''' 
        #Ọnụ ego mbụ nke Olivia dị ka initial_money.
        initial_money = 23 
        #Ọ zụtara akpa ise maka $3 nke ọ bụla
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Mgbe ịzụrụ akpa ndị ahụ, Olivia nwere
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Azịza ya bụ 8.''',
    ''' 
        #Leah nwere dị ka 32 na ọnụ ọgụgụ chọkọleti nwanne ya nwanyị nwere dị 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Ọ bụrụ na ha rie 35 chocolate
        eaten_chocolates = 35 
        #Ọnụ ọgụgụ chọkọletị fọdụrụnụ bụ
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Azịza ya bụ 39.'''              
]


kin_example_list = [
    ''' 
        #Roger yatangiranye imipira 5 ya tennis.	
        tennis_balls = 5 
        #Amabati 2 yumupira wa tennis buri umwe ni
        bought_balls = 2 * 3 tennis balls 
        #Igisubizo ni
        answer = tennis_balls + bought_balls 
        return answer
        #Igisubizo ni 11''',
    ''' 
        #Ku ikubitiro, hari mudasobwa 9 mucyumba cya seriveri.
        initial_computers = 9 
        #Kuva kuwa mbere kugeza kuwa kane, hari iminsi 4.
        days = 4 
        #Mudasobwa 5 zongerewe buri munsi
        added_computers_per_day = 5 
        #Umubare rusange wa mudasobwa wongeyeho ni
        days * added_computers_per_day = 4 * 5 = 20 
        #umubare rusange wa mudasobwa mucyumba cya seriveri ni
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Igisubizo ni 29.''',
    ''' 
        #Ku ikubitiro, hari imodoka 3.
        initial_cars = 3 
        #Izindi modoka 2 zirahagera.
        arriving_cars = 2 
        #umubare wimodoka zose muri parikingi ni
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Igisubizo ni 5.''',
    ''' 
        #Shawn afite ibikinisho 5.
        initial_toys = 5 
        #Yabonye ibikinisho 2 kwa nyina
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Yabonye ibindi bikinisho 2 kwa se, ubu rero arabifite
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Igisubizo ni 9.''',
    ''' 
        #Michael yatangiye afite imipira 58 ya golf
        initial_balls = 58
        #Ku wa kabiri, yatakaje imipira 23 ya golf.
        lost_on_tuesday = 23
        #Ku wa gatatu, yatakaje indi mipira 2 ya golf.
        lost_on_wednesday = 2
        #Kubwibyo, mu mpera zuwagatatu, afite
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Igisubizo ni 33.''',
    ''' 
        #Olivia umubare wambere wamafaranga nk initial_money.
        initial_money = 23 
        #Yaguze imifuka itanu kuri $ 3 buri umwe
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Nyuma yo kugura imifuka, Olivia afite
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Igisubizo ni 8.''',
    ''' 
        #Leah yari afite 32 naho umubare wa shokora mushiki we yari afite 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Niba bariye shokora 35
        eaten_chocolates = 35 
        #Umubare usigaye wa shokora ni
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Igisubizo ni 39.'''              
]



lin_example_list = [
    ''' 
        #Roger abandaki na 5 balles ya tennis.
        tennis_balls = 5 
        #2 bidons ya 3 balles ya tennis moko na moko ezali
        bought_balls = 2 * 3 tennis balls 
        #Eyano ezali
        answer = tennis_balls + bought_balls 
        return answer
        #Eyano ezali 11''',
    ''' 
        #Na ebandeli, ezalaki na baordinatɛrɛ 9 na salle ya serveur. 
        initial_computers = 9 
        #Kobanda mokolo ya mibale tii mokolo ya minei, ezali na mikolo 4.
        days = 4 
        #Bazalaki kobakisa baordinatɛrɛ 5 mokolo na mokolo
        added_computers_per_day = 5 
        #Motango mobimba ya baordinatɛrɛ oyo ebakisami ezali
        days * added_computers_per_day = 4 * 5 = 20 
        #motango mobimba ya ba ordinateurs na salle ya serveur ezali
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Eyano ezali 29.''',
    ''' 
        #Na ebandeli, mituka ezali 3.
        initial_cars = 3 
        #Mituka mosusu 2 ekomi. 
        arriving_cars = 2 
        #motango mobimba ya mituka na parking ezali
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Eyano ezali 5.''',
    ''' 
        #Shawn azali na 5 jouets. 
        initial_toys = 5 
        #Azuaki 2 jouets epayi ya maman na ye
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Azuaki 2 jouets mosusu epayi ya papa na ye, donc sikoyo azui
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Eyano ezali 9.''',
    ''' 
        #Michael abandaki na bale 58 ya golf
        initial_balls = 58
        #Na mokolo ya mibale, abungisaki bale 23 ya golf.
        lost_on_tuesday = 23
        #Na mokolo ya misato, abungisaki bale 2 mosusu ya golf.
        lost_on_wednesday = 2
        #Yango wana, na nsuka ya mokolo ya misato, azali na...
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Eyano ezali 33.''',
    ''' 
        #Motango ya mbongo ya liboso ya Olivia lokola initial_money.
        initial_money = 23 
        #Asombaki bagels mitano na dolare 3 mokomoko 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Nsima ya kosomba ba bagels, Olivia azali na yango 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Eyano ezali 8.''',
    ''' 
        #Leah azalaki na ba chocolats lokola 32 mpe motango ya ba chocolats oyo ndeko na ye ya mwasi azalaki na yango lokola 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Soki baliaki 35 chocolats
        eaten_chocolates = 35 
        #Motango oyo etikali ya ba chocolats ezali 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Eyano ezali 39.'''              
]


lug_example_list = [
    ''' 
        #Roger yatandikidde ku mipiira gya ttena 5.
        tennis_balls = 5 
        #Ebibbo 2 eby’emipira gya ttena 3 buli kimu kiri...
        bought_balls = 2 * 3 tennis balls 
        #Eky’okuddamu kiri nti
        answer = tennis_balls + bought_balls 
        return answer
        #Eky’okuddamu kiri nti 11''',
    ''' 
        #Mu kusooka, mu kisenge kya seeva mwalimu kompyuta 9.
        initial_computers = 9 
        #Okuva ku Mmande okutuuka ku Lwokuna, wabaawo ennaku 4.
        days = 4 
        #Kompyuta 5 zaayongerwako buli lunaku
        added_computers_per_day = 5 
        #Omuwendo gwa kompyuta zonna awamu ezigattibwako guli...
        days * added_computers_per_day = 4 * 5 = 20 
        #omuwendo gwonna ogwa kompyuta mu kisenge kya seeva guli
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Eky’okuddamu kiri nti 29.''',
    ''' 
        #Mu kusooka, mmotoka zibeera 3.
        initial_cars = 3 
        #Emmotoka endala 2 zituuse. 
        arriving_cars = 2 
        #omuwendo gwonna ogw’emmotoka mu ppaaka guli
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Eky’okuddamu kiri nti 5.''',
    ''' 
        #Shawn alina eby’okuzannyisa 5. 
        initial_toys = 5 
        #Yafuna toys 2 okuva ewa maama we
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Yafuna toys endala 2 okuva ewa taata we, kale kati alina
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Eky’okuddamu kiri nti 9.''',
    ''' 
        #Michael yatandikidde ku mipiira gya Golf 58
        initial_balls = 58
        #Ku Lwokubiri, yafiiriddwa emipiira gya Golf 23.
        lost_on_tuesday = 23
        #Ku Lwokusatu, yafiiriddwa emipiira gya Golf emirala 2.
        lost_on_wednesday = 2
        #N’olwekyo, ku nkomerero y’Olwokusatu, alina...
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Eky’okuddamu kiri nti 33.''',
    ''' 
        #Ssente za Olivia ezasooka nga initial_money.
        initial_money = 23 
        #Yagula bagels ttaano ku doola ssatu buli emu
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Oluvannyuma lw’okugula bagels, Olivia alina...
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Eky’okuddamu kiri nti 8.''',
    ''' 
        #Leah yalina nga 32 ate omuwendo gwa chocolate mwannyina gwe yalina nga 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Singa baalidde chocolate 35
        eaten_chocolates = 35 
        #Omuwendo gwa chocolate ogusigaddewo guli...
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Eky’okuddamu kiri nti 39.'''              
]




orm_example_list = [
    ''' 
        #Roger kubbaa teenisii 5n jalqabe.
        tennis_balls = 5 
        #2 qaruuraa kubbaa teenisii 3 tokkoon tokkoon isaanii
        bought_balls = 2 * 3 tennis balls 
        #Deebiin isaa
        answer = tennis_balls + bought_balls 
        return answer
        #The answer is 11''',
    ''' 
        #Jalqaba kutaa sarvarii keessa kompiitaroonni 9 turan.
        initial_computers = 9 
        #Isniina hanga Kamisaatti guyyoota 4tu jira.
        days = 4 
        #Guyyaatti kompiitara 5 dabalameera
        added_computers_per_day = 5 
        #Walumaagalatti lakkoofsi kompiitara itti dabalame
        days * added_computers_per_day = 4 * 5 = 20 
        #lakkoofsi waliigalaa kompiitara kutaa sarvarii keessa jiran
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Deebiin isaa 29 dha.''',
    ''' 
        #Jalqaba irratti konkolaataa 3tu jira.
        initial_cars = 3 
        #Konkolaattonni dabalataa 2 ni dhufu. 
        arriving_cars = 2 
        #lakkoofsa waliigalaa konkolaattota buufata konkolaataa keessa jiran
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Deebiin isaa 5.''',
    ''' 
        #Shawn meeshaalee taphaa 5 qaba.
        initial_toys = 5 
        #Meeshaalee taphaa 2 haadha isaa irraa argate 
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Abbaa isaa irraa meeshaalee taphaa 2 dabalataan argateera, kanaaf amma argateera 
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Deebiin isaa 9.''',
    ''' 
        #Maayikeel kubbaa goolfii 58n jalqabe
        initial_balls = 58
        #Kibxata darbe kubbaa goolfii 23 dhabe.
        lost_on_tuesday = 23
        #Kibxata darbe kubbaa goolfii 2 dabalataan dhabe.
        lost_on_wednesday = 2
        #Kanaaf dhuma Roobii irratti...
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Deebiin isaa 33 dha.''',
    ''' 
        #Maallaqni Oliiviyaan jalqabaa akka initial_money.
        initial_money = 23 
        #Baageelii shan tokkoon tokkoon isaanii doolaara 3n bitte
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Bagels erga bitee booda Oliiviyaan qabdi 
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Deebiin isaa 8.''',
    ''' 
        #Liyaan akka 32, lakkoofsi chokoleetii obboleettiin ishee ammoo 42 qaba ture. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Yoo isaan chokoleetii 35 nyaatan
        eaten_chocolates = 35 
        #Lakkoofsi chokoleetii hafe ammoo 
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Deebiin isaa 39 dha.'''              
]





sna_example_list = [
    ''' 
        #Roger akatanga aine mabhora mashanu etennis.
        tennis_balls = 5 
        #2 makani emabhora matatu etennis rimwe nerimwe riri
        bought_balls = 2 * 3 tennis balls 
        #Mhinduro ndeyekuti
        answer = tennis_balls + bought_balls 
        return answer
        #Mhinduro ndeye 11''',
    ''' 
        #Pakutanga, kwaive nemakomputa 9 mukamuri yeseva. 
        initial_computers = 9 
        #Kubva Muvhuro kusvika China, pane mazuva mana.
        days = 4 
        #5 makomputa akawedzerwa zuva rega rega
        added_computers_per_day = 5 
        #Nhamba yese yemakomputa akawedzerwa ndeye 
        days * added_computers_per_day = 4 * 5 = 20 
        #nhamba yese yemakomputa ari mukamuri yeseva ndiyo
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #The answer is 29.''',
    ''' 
        #Pakutanga, pane 3 motokari.
        initial_cars = 3 
        #2 dzimwe mota dzinosvika.
        arriving_cars = 2 
        #nhamba yose yemotokari munzvimbo yekupaka ndiyo 
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Mhinduro ndi5.''',
    ''' 
        #Shawn ane matoyi mashanu. 
        initial_toys = 5 
        #Akawana matoyi maviri kubva kuna amai vake
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Akawana zvimwe matoyi maviri kubva kuna baba vake, saka iye zvino ave nazvo 
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Mhinduro ndi9.''',
    ''' 
        #Michael akatanga aine 58 mabhora egorofu
        initial_balls = 58
        #NeChipiri, akarasikirwa nemabhora egorofu makumi maviri nematatu.
        lost_on_tuesday = 23
        #NeChitatu, akarasikirwa nemamwe mabhora egorofu maviri.
        lost_on_wednesday = 2
        #Naizvozvo, pakupera kweChitatu, ane
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Mhinduro ndeye 33.''',
    ''' 
        #Mari yekutanga yaOlivia se initial_money.
        initial_money = 23 
        #Akatenga mabhegi mashanu ne$3 rimwe nerimwe
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Mushure mekutenga mabheji, Olivia ane
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Mhinduro ndi8.''',
    ''' 
        #Leah aive aine makumi matatu nemaviri uye nhamba yemachokoreti hanzvadzi yake yaive makumi mana nemaviri.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Kana vakadya 35 chocolates
        eaten_chocolates = 35 
        #Nhamba yasara yemachokoreti ndeye
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Mhinduro ndeye 39.'''              
]



sot_example_list = [
    ''' 
        #Roger o simolotse ka dibolo di le 5 tsa thenese. 
        tennis_balls = 5 
        #Dikotikoti di le 2 tsa dibolo di le 3 tsa thenese nngwe le nngwe ke
        bought_balls = 2 * 3 tennis balls 
        #Karabo ke gore
        answer = tennis_balls + bought_balls 
        return answer
        #Karabo ke 11''',
    ''' 
        #Kwa tshimologong, go ne go na le dikhomphutara di le 9 mo phaposing ya disefara.
        initial_computers = 9 
        #Go tloga ka Mosupologo go fitlha ka Labone, go na le malatsi a le 4.From Monday to Thursday, there are 4 days. 
        days = 4 
        #Go tsenngwa dikhomphutara di le 5 letsatsi le letsatsi
        added_computers_per_day = 5 
        #Palogotlhe ya dikhomphutara tse di tsentsweng ke
        days * added_computers_per_day = 4 * 5 = 20 
        #palogotlhe ya dikhomphutara tse di mo phaposing ya disefara ke
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Karabo ke 29.''',
    ''' 
        #Kwa tshimologong, go na le dikoloi di le 3.
        initial_cars = 3 
        #Dikoloi tse dingwe tse 2 di a goroga.
        arriving_cars = 2 
        #palogotlhe ya dikoloi tse di mo lefelong la go phaka dikoloi ke
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Karabo ke 5.''',
    ''' 
        #Shawn o na le ditshamekisi di le 5.
        initial_toys = 5 
        #O amogetse ditshamekisi di le 2 go tswa go mmaagwe
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #O amogetse ditshamekisi tse dingwe gape di le 2 go tswa go rraagwe, ka jalo jaanong o na le
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Karabo ke 9.''',
    ''' 
        #Michael o simolotse ka dibolo tsa kolofo di le 58
        initial_balls = 58
        #Ka Labobedi, o ne a latlhegelwa ke dibolo di le 23 tsa kolofo.
        lost_on_tuesday = 23
        #Ka Laboraro, o ne a latlhegelwa ke dibolo tse dingwe gape di le 2 tsa kolofo.
        lost_on_wednesday = 2
        #Ka jalo, kwa bokhutlong jwa Laboraro, o na le . 
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #The answer is 33.''',
    ''' 
        #Madi a ntlha a ga Olivia jaaka initial_money.
        initial_money = 23 
        #O ne a reka di-bagel di le tlhano ka R100 nngwe le nngwe
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Fa a sena go reka di-bagel, Olivia o
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Karabo ke 8.''',
    ''' 
        #Leah o ne a na le di le 32 mme palo ya ditšhokolete tse kgaitsadie a neng a na le tsone e ne e le 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Fa ba ka ja ditšhokolete di le 35
        eaten_chocolates = 35 
        #Palo e e setseng ya ditšhokolete ke
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Karabo ke 39.'''              
]



twi_example_list = [
    ''' 
        #Roger de tɛnis bɔɔl 5 na efii ase.
        tennis_balls = 5 
        #2 cans a 3 tennis bɔɔl biara yɛ
        bought_balls = 2 * 3 tennis balls 
        #Mmuae no ne sɛ
        answer = tennis_balls + bought_balls 
        return answer
        #Mmuae no ne 11''',
    ''' 
        #Mfiase no, na kɔmputa 9 na ɛwɔ server dan no mu. 
        initial_computers = 9 
        #Efi Memeneda kosi Dwoda no, ɛyɛ nnafua 4.
        days = 4 
        #Wɔde kɔmputa 5 kaa ho da biara 
        added_computers_per_day = 5 
        #Kɔmputa dodow a wɔde aka ho nyinaa yɛ
        days * added_computers_per_day = 4 * 5 = 20 
        #kɔmputa dodow a ɛwɔ server dan no mu nyinaa yɛ
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Mmuae no ne 29.''',
    ''' 
        #Mfiase no, na kar 3 na ɛwɔ hɔ.
        initial_cars = 3 
        #Kar afoforo 2 ba.
        arriving_cars = 2 
        #kar dodow a ɛwɔ baabi a wɔde kar sisi no nyinaa yɛ
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Mmuae no ne 5.''',
    ''' 
        #Shawn wɔ agode 5. 
        initial_toys = 5 
        #Onyaa agode 2 fii ne maame hɔ
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Ɔnyaa agodeɛ 2 bio fii ne papa hɔ, enti seesei wanya
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Mmuae no ne 9.''',
    ''' 
        #Michael de golf bɔɔl 58 na efii ase
        initial_balls = 58
        #Yawda no, ɔhweree golf bɔɔl 23.
        lost_on_tuesday = 23
        #Dwoda no, ɔhweree golf bɔɔl 2 foforo.
        lost_on_wednesday = 2
        #Enti, wɔ Dwoda awiei no, wayɛ
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Mmuae no ne 33.''',
    ''' 
        #Olivia sika dodow a edi kan no sɛ initial_money.
        initial_money = 23 
        #Ɔtɔɔ bagel anum de gyee $3 biara
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Bere a Olivia atɔ bagels no awie no, wayɛ
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Mmuae no ne 8.''',
    ''' 
        #Ná Leah wɔ 32 na na chocolate dodow a ne nuabea wɔ no yɛ 42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Sɛ wodii chocolate 35 a
        eaten_chocolates = 35 
        #Chocolate dodow a aka no yɛ
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Mmuae no ne 39.'''              
]


wol_example_list = [
    ''' 
        #Roger mingi tàmbali ak 5 balon tennis. 
        tennis_balls = 5 
        #2 poti 3 balon tennis bu nekk
        bought_balls = 2 * 3 tennis balls 
        #Tontu li mooy
        answer = tennis_balls + bought_balls 
        return answer
        #Tontu li mooy 11''',
    ''' 
        #Bi ñuy tàmbali, amoon na 9 ordinatër ci saalu serwër bi.
        initial_computers = 9 
        #Lu ko dalee altine ba alxamis, amna 4 fan.
        days = 4 
        #5 ordinatër lañuy yokk bis bu nekk
        added_computers_per_day = 5 
        #Limu ordinatër yiñ yokk yépp mooy
        days * added_computers_per_day = 4 * 5 = 20 
        #limu ordinatër yi ci saalu serwër bi mooy 
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Tontu li mooy 29.''',
    ''' 
        #Bi ñuy tàmbali, amna ñatti oto.
        initial_cars = 3 
        #2 oto yu bees yegsi.
        arriving_cars = 2 
        #limu oto yi ci gaaraas bi mooy
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Tontu li mooy 5.''',
    ''' 
        #Shawn amna 5 fowukaay.
        initial_toys = 5 
        #Dafa am ñaari fowukaay ci yaayam
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Dafa am ñaari fowukaay ci pàppaam, kon leegi amna
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Tontu li mooy 9.''',
    ''' 
        #Michael mingi tàmbali ak 58 balu golf
        initial_balls = 58
        #Ci talaata, mu ñàkk 23 balon golf.
        lost_on_tuesday = 23
        #Ci Alarba, mu ñàkk yeneen ñaari balon golf.
        lost_on_wednesday = 2
        #Kon, ci njeextelu alarba, amna
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Tontu li mooy 33.''',
    ''' 
        #Xaalis bi Olivia njëkka am mooy initial_money.
        initial_money = 23 
        #Mu jënd juróomi bagels benn $3
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Ginaaw bi Olivia jëndee bagel yi,
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Tontu li mooy 8.''',
    ''' 
        #Leah amoon na 32 sokolaa, rakkam bu jigéen amoon na 42 sokolaa. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Suñu lekkee 35 sokolaa
        eaten_chocolates = 35 
        #limu sokolaa yi des mooy
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Tontu li mooy 39.'''              
]



xho_example_list = [
    ''' 
        #URoger waqala ngeebhola zentenetya ezi-5. 
        tennis_balls = 5 
        #Iitoti ezi-2 zeebhola zentenetya ezi-3 inye
        bought_balls = 2 * 3 tennis balls 
        #Impendulo ithi
        answer = tennis_balls + bought_balls 
        return answer
        #Impendulo ngu 11''',
    ''' 
        #Ekuqaleni, bekukho iikhompyutha ezili-9 kwigumbi leseva. 
        initial_computers = 9 
        #Ukususela ngoMvulo ukuya ngoLwesine, kukho iintsuku ezi-4.
        days = 4 
        #Iikhompyutha ezi-5 zongezwa ngosuku ngalunye
        added_computers_per_day = 5 
        #Inani lilonke leekhompyuter ezongeziweyo
        days * added_computers_per_day = 4 * 5 = 20 
        #inani elipheleleyo leekhompyuter kwigumbi lomncedisi li
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Impendulo ngu 29.''',
    ''' 
        #Ekuqaleni, kukho iimoto ezi-3.
        initial_cars = 3 
        #Iimoto ezi-2 ngaphezulu zifikile.
        arriving_cars = 2 
        #inani lilonke leemoto kwindawo yokupaka
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Impendulo ngu-5.''',
    ''' 
        #UShawn uneethoyi ezi-5.
        initial_toys = 5 
        #Wafumana iithoyi ezi-2 kumama wakhe
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Ufumene ezinye izinto zokudlala ezi-2 kutata wakhe, ngoku unazo 
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Impendulo ngu9.''',
    ''' 
        #UMichael waqala ngeebhola zegalufa ezingama-58
        initial_balls = 58
        #NgoLwesibini, uphulukene neebhola zegalufa ezingama-23.
        lost_on_tuesday = 23
        #NgoLwesithathu, uphulukene neebhola zegalufa ezi-2 ngaphezulu.
        lost_on_wednesday = 2
        #Ngoko ke, ekupheleni kukaLwesithathu, uye
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Impendulo ngu 33.''',
    ''' 
        #Imali yokuqala kaOlivia njengoko initial_money.
        initial_money = 23 
        #Wathenga iibhegi ezintlanu nge-$3 inye
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Emva kokuthenga ii-bagels, u-Olivia uye
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Impendulo ngu-8.''',
    ''' 
        #ULeah wayenama 32 kunye nenani letshokholethi udade wabo wayenazo ngama 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Ukuba batye iitshokolethi ezingama-35
        eaten_chocolates = 35 
        #Inani eliseleyo leetshokolethi li
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Impendulo ngu 39.'''              
]


yor_example_list = [
    ''' 
        #Roger bẹrẹ pẹlu awọn bọọlu tẹnisi 5. 
        tennis_balls = 5 
        #Awọn agolo 2 ti awọn bọọlu tẹnisi 3 kọọkan jẹ
        bought_balls = 2 * 3 tennis balls 
        #Idahun si jẹ
        answer = tennis_balls + bought_balls 
        return answer
        #Idahun si jẹ 11''',
    ''' 
        #Ni ibẹrẹ, awọn kọnputa 9 wa ninu yara olupin naa.
        initial_computers = 9 
        #Lati Ọjọ Aarọ si Ọjọbọ, awọn ọjọ mẹrin wa.
        days = 4 
        #Awọn kọnputa 5 ni a ṣafikun ni ọjọ kọọkan
        added_computers_per_day = 5 
        #Awọn lapapọ nọmba ti awọn kọmputa kun ni
        days * added_computers_per_day = 4 * 5 = 20 
        #lapapọ nọmba ti awọn kọmputa ni yara olupin ni
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Idahun si jẹ 29.''',
    ''' 
        #Ni ibẹrẹ, awọn ọkọ ayọkẹlẹ 3 wa.
        initial_cars = 3 
        #Awọn ọkọ ayọkẹlẹ 2 diẹ sii de. 
        arriving_cars = 2 
        #lapapọ nọmba ti paati ni o pa pupo
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Idahun si jẹ 5.''',
    ''' 
        #Shawn ni awọn nkan isere 5.
        initial_toys = 5 
        #O ni awọn nkan isere meji lati ọdọ iya rẹ
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #O ni awọn nkan isere meji diẹ sii lati ọdọ baba rẹ, nitorinaa o ni
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Idahun si jẹ 9.''',
    ''' 
        #Michael bẹrẹ pẹlu awọn bọọlu gọọfu 58
        initial_balls = 58
        #Ni ọjọ Tuesday, o padanu awọn bọọlu golf 23.
        lost_on_tuesday = 23
        #Ni ọjọ Wẹsidee, o padanu awọn bọọlu golf meji diẹ sii.
        lost_on_wednesday = 2
        #Nitorina, ni opin Wednesday, o ni
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Idahun si jẹ 33.''',
    ''' 
        #Iye owo akọkọ ti Olivia bi initial_money.
        initial_money = 23 
        #O ra baagi marun fun $3 kọọkan
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Lẹhin rira awọn baagi, Olivia ni
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Idahun si jẹ 8.''',
    ''' 
        #Leah ni bi 32 ati nọmba awọn chocolate ti arabinrin rẹ ni bi 42.
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Ti won ba je 35 chocolates
        eaten_chocolates = 35 
        #Awọn ti o ku nọmba ti chocolates ni
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Idahun si jẹ 39.'''              
]



zul_example_list = [
    ''' 
        #URoger uqale ngamabhola ethenisi ama-5.
        tennis_balls = 5 
        #Amathini ama-2 wamabhola ethenisi ama-3 lilinye linawo
        bought_balls = 2 * 3 tennis balls 
        #Impendulo ithi
        answer = tennis_balls + bought_balls 
        return answer
        #Impendulo ithi 11''',
    ''' 
        #Ekuqaleni, bekunamakhompyutha angu-9 ekamelweni leseva.
        initial_computers = 9 
        #Kusukela ngoMsombuluko kuya kuLwesine, kunezinsuku ezi-4.
        days = 4 
        #Amakhompyutha angu-5 ayengezwa usuku ngalunye
        added_computers_per_day = 5 
        #Isamba senani lamakhompyutha angeziwe
        days * added_computers_per_day = 4 * 5 = 20 
        #inani eliphelele lamakhompyutha egumbini leseva li
        answer = initial_computers + total_added_computers = 9 + 20 = 29
        return answer
        #Impendulo ithi 29.''',
    ''' 
        #Ekuqaleni, kunezimoto ezi-3.
        initial_cars = 3 
        #2 ezinye izimoto ezifikayo. 
        arriving_cars = 2 
        #inani eliphelele lezimoto endaweni yokupaka
        answer = initial_cars + arriving_cars = 3 + 2 = 5. 
        return answer
        #Impendulo ngu-5.''',
    ''' 
        #UShawn unamathoyizi angu-5. 
        initial_toys = 5 
        #Uthole amathoyizi ama-2 kumama wakhe 
        initial_toys + 2 = 5 + 2 = 7 toys. 
        #Uthole amanye amathoyizi angu-2 kubaba wakhe, manje usewatholile
        answer = 7 + 2 = 9 toys in total. 
        return answer
        #Impendulo ithi 9.''',
    ''' 
        #UMichael waqala ngamabhola egalofu angama-58, impendulo ingu-9.
        initial_balls = 58
        #NgoLwesibili, ulahlekelwe amabhola egalufu angama-23.
        lost_on_tuesday = 23
        #NgoLwesithathu, ulahlekelwe amabhola egalufu angu-2 ngaphezulu.
        lost_on_wednesday = 2
        #Ngakho-ke, ekupheleni kwangoLwesithathu, usenakho
        answer = initial_balls - lost_on_tuesday - lost_on_wednesday = 58 - 23 - 2 = 33.
        return answer
        #Impendulo ithi 33.''',
    ''' 
        #Inani lokuqala lemali lika-Olivia njenge initial_money.
        initial_money = 23 
        #Wathenga amabheji amahlanu ngo-$3 lilinye 
        total_cost_bagels = number_bagels * cost_one_beagel = 15 
        #Ngemva kokuthenga ama-bagels, u-Olivia usenawo
        answer = initial_money - total_cost_bagels = 23 - 15 = 8 
        return answer
        #Impendulo ithi 8.''',
    ''' 
        #U-Leah wayeneminyaka engama-32 kanti isibalo sikashokholethi udadewabo sasingu-42. 
        leah_chocolates = 32 
        sister_chocolates = 42 
        total_chocolates = leah_chocolates + sister_chocolates = 32 + 42 = 74 
        #Uma bedle oshokoledi abangama-35
        eaten_chocolates = 35 
        #Inombolo esele yoshokoledi ithi
        answer = remaining_chocolates = total_chocolates - eaten_chocolates = 74 - 35 = 39 
        return answer
        #Impendulo ithi 39.'''              
]

