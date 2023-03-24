import random

real_story = '''Парень задолжал очень большую сумму местному банку. Он провел вечер в баре и сильно напился. 
Вернувшись домой, он забыл закрыть дверь. Пришедшие за ним коллекторы вломились в дом и начали ему угрожать, 
он выдал место хранения ценных вещей. Коллекторы забрали все драгоценности и ушли, а пьяный парень в бреду пришел к 
выводу, что жить смысла больше нет и повесился.'''

__questions = [('Я крепка, как скала, но рушусь от слова. Что я?', ['тишина']),
               ('Умнейший человек не замечает одного... Что же это?', ['собственный нос', 'нос', 'свой нос']),
               ('Дочь морская, но в воде умираю. Что я?', ['соль']),
               ('У меня бывает борода. Меня можно испортить. Да и ростом бываю не высок. Ниже пояса. Кто я ?',
                ['шутка', 'Прикол', 'анекдот', 'каламбур', 'шуточка']),
               ('Девять одинаковых кошек в лодке, одна cпрыгнула. Сколько осталось ?',
                ['ни одной', 'ноль', 'нисколько', 'не осталось']),
               ('Чего хочет тот, кто полностью удовлетворен ?', ['ничего']),
               ('Я — вода и по воде плаваю. Кто я?', ['льдинка', 'лед', 'лёд', 'ледышка']),
               ('Все меня топчут, а я — всё лучше.', ['тропинка', 'тропа', 'дорожка']),
               ('Что невозможно удержать и десяти минут, хотя оно легче пёрышка?', 'дыхание'),
               ('Я ем и голодаю, а мой брат идет и пропадает', ['огонь', 'костер', 'костёр', 'пламя']),
               ('От головы до хвоста 12 м, а от хвоста до головы 0 м. Что это?', ['год']),
               ('Что не может увеличить лупа в треугольнике?', ['углы', 'угол']),
               ('Чем их больше, тем вес меньше. Что это?', ['дырки', 'дыры', 'отверстия', 'дырочки']),
               ('Какой пробкой нельзя заткнуть ни одну бутылку?',
                ['дорожной', 'автомобильной', 'машинной', 'транспортной']),
               ('Завязать можно, а развязать нельзя.', ['разговор', 'роман'])]

__evidences = [
    'Тело было найдено матерью погибшего на следующий день после смерти, он был повешен на петле, под его ногами была опрокинутая табуретка.',
    'Соседи заявили, что парень возвращался домой поздно вечером очень пьяным.',
    'Мать утверждала, что ее сын был очень жизнерадостным человеком и никогда бы такого не совершил.',
    'Выяснилось, что у парня было множество долгов.',
    'При обыске квартиры обнаружили пропажу ценных вещей.']

__first_part = '''"Здравствуйте детектив! Вы как раз вовремя, давайте я вас провожу к погибшему", - голос полицейского
казался неестественно звонким. "Спасибо, я разберусь", - не убирая прилипшую к губам сигарету, ответил Джейкоб. Блэк поднялся
по лестнице и увидел дверь с характерной желто-черной лентой. Он приложил немало усилий, пытаясь открыть ее, но 
все было напрасно - дверь не поддавалась.'''
__first_link = 'Помогите Джейкобу открыть дверь - ответьте на загадку'
__first_success = 'Наконец, приложив нечеловеческие усилия, Джейкоб смог отворить эту дверь, немного изучив комнату и тело погибшего он записал первую улику к себе в дневник:'
__first_fail = 'Ржавая ручка так и не поддалась детективу, к сожалению, зацепки по этому делу ему придется искать в другом месте.'

__second_part = '''Из соседней двери вышел мужчина в темном фраке и закурил, бросив жалобный, но в то же время осудительный взгляд
на дверь в квартиру погибшего. Когда сосед уже почти ушел, Джейкоб крикнул ему вслед: "Постойте, мистер". Блэк подошел к мужчине
и хотел было расспросить его о том, что ему известно о погибшем, но заметил, что мужчина сильно нервничает и торопится побыстрее уйти'''
__second_link = 'Сосед явно что-то знает, помогите Блэку разговорить незнакомца'
__second_success = '''"Черт, с тобой!" - ответил мужчина и начал свой рассказ о вчерашнем вечере... 
Так в дневнике Блэка появилась новая улика: '''
__second_fail = '"Мне некогда!" - рявкнул мужчина и скрылся прежде чем Джейкоб смог что-либо предпринять.'

__third_part = '''Выйдя из мрачного подъезда и закурив очередную сигарету, Блэк уже собирался уходить. 
"Постойте, постойте!" - плачущим голосом закрчиала женщина вслед шерифу. Обернувшись, Джейкоб увидел как странная, заплаканная
женщина подбежала к полицейской машине, преграждавшей путь к подъезду. "Это мой сын! Пустите!" - кричала женщина,
но полицейские не пускали ее. Блэк подошел к патрульному и попросил его пропустить эту женщину. Полицейский нахмурился
и с недоверием посмотрел на детектива'''
__third_link = '''Помогите Блэку убедить патрульного пропустить женщину'''
__third_success = '''Сильно нехотя полицейский согласился пропустить даму. Джейкоб провел женщину
к ближайшей лавочке, успокоил, рассказал, что он детектив, которому поручено расследовать это дело и внимательно выслушал
все, что она ему рассказала. Так у Блэка появилась новая запись в дневнике: '''
__third_fail = '''Грозно посмотрев на него и отвернувшись, полицейский дал понять Джейкобу, что не пропустит эту даму.
Что же, придется Блэку искать улики в другом месте.'''

__fourth_part = '''Перебирая документы связанные с Ричардом, Блэк нашел визитку печально известного банка "Сент-Льюис".
Приехав в главное здание, Блэк сходу встретился с презрительным взглядом главного администратора банка. "Что вам?" - с натянутой
улыбкой проговорил администратор. "Я хочу узнать подробности о счете Ричарда Паркера. Вот мое удостоверение", - с не менее натянутой
улыбкой ответил Джейкоб. "Извините, эта информация конфиденциальна", - коротко ответил администратор и удалился в свой офис.
Немного осмотревшись, Блэк замечает открытую дверь в архив...'''
__fourth_link = '''Помогите Джейкобу узнать нужную ему информацию, не привлекая лишнего внимания'''
__fourth_success = '''Пробравшись сквозь толпу клерков, Блэк ловко заныривает в архив. Перерыв с полсотни различных
документов, он наконец нашел нужные ему. Не тратя время на радость, он смог сбежать из помещения за секунду до прихода 
работника. Так в дневнике детектива появилась новая запись: '''
__fourth_fail = '''Стоило Блэку войти в помещение архива, как его тут же поймали охранники, заметившие этот дерзкий
поступок детектива. Сильно церемониться с Блэком не стали, но, к счастью для него, банку хватало различных скандалов
и его просто выкинули из здания.'''

__fifth_part = '''Уже придя домой, Джейкоб услышал гудок телефона. Он сильно устал за сегодня и надеялся хорошо отдохнуть, но,
увидев на экране мобильного звонок от начальства, он понял, что отдохнуть сейчас точно не получится. "Внимание... Джейкоб...
Мы получили очень важную... Это многое..." - звук был настолько ужасным, что Блэк едва мог разобрать отдельные слова.
"Нужно срочно починить антенну!" - Джейкоб вспомнил о сломанной антенне, которую он забывал починить уже несколько дней.'''
__fifth_link = '''Помогите детективу разобраться со сломанной антенной'''
__fifth_success = '''"Давай же! Ну давай... Да! Работает!" - Джейкоб все же смог починить злополучную антенну.
То, что он услышал от своих коллег, сильно шокировало Блэка... "Это и правда многое меняет..." - все, что смог
вымолвить детектив перед тем как помчаться в отдел'''
__fifth_fail = '''"Да, электрик из меня явно хуже чем детектив", - заключил детектив. 
"Не страшно, кажется я уже понял что к чему", - он второпях надел на себя фрак и направился в отдел.'''

user_evidences = []


def part_of_story_and_question(part_of_story, story_question_link, part_number, success, fail):
    print(part_of_story)
    print(story_question_link)
    question = random.choice(__questions)
    answer = input(question[0] + ' ')
    if answer.lower() in question[1]:
        print(success)
        print(f'"{__evidences[part_number]}"')
        user_evidences.append(__evidences[part_number])
    else:
        print(fail)
    __questions.remove(question)


def ending(evidences):
    if len(evidences) >= 3:
        replica = '''Собрав достаточное количество улик, Джейкоб пришел к выводу о том, что наверняка знает судьбу
погибшего юноши. Примчавшись в офис поздно ночью, он созвал всех, кто в нем находился, и торжественно заявил: '''
        print(replica)
    else:
        replica = '''Несмотря на небольшое количество улик, Джейкоб пришел к выводу о том, что наверняка знает судьбу
            погибшей. Примчавшись в офис поздно ночью, он созвал всех, кто в нем находился, и торжественно заявил: '''
        print(replica)
    ans = input('''Вот как умер Ричард Паркер: ''')
    variants = ['суицид', 'самоубийство', 'убил себя', 'повесился', 'покончил с собой']
    if ans.lower() in variants:
        # Фото успеха
        a1 = 'Да! Джейкоб как всегда оказался прав! Вот как все было на самом деле: '
        print(a1)
        print(real_story)
    else:
        a2 = '"Нет, постойте, кажется я ошибся!" - вскрикнул Джейкоб. Вот причина сметри Ричарда Паркера: '
        print(a2)
        ans = input('Выберите вариант: Самоубийство, Мать, Коллекторы')
        if ans.lower() in variants:
            # Фото успеха
            a3 = 'Да! Джейкоб как всегда оказался прав! Вот как все было на самом деле: '
            print(a3)
            print(real_story)
        else:
            # Фото поражения
            a4 = '''К сожалению, Джейкобу не удалось раскрыть это дело: его репутация была подорвана, 
а за решеткой оказался невиновный...'''
            print(a4)


def story():
    # Начальное фото
    # Фото двери
    part_of_story_and_question(__first_part, __first_link, 0, __first_success, __first_fail)
    # Фото соседа
    part_of_story_and_question(__second_part, __second_link, 1, __second_success, __second_fail)
    # Фото матери
    part_of_story_and_question(__third_part, __third_link, 2, __third_success, __third_fail)
    # Фото банка
    part_of_story_and_question(__fourth_part, __fourth_link, 3, __fourth_success, __fourth_fail)
    # Фото драгоценностей
    part_of_story_and_question(__fifth_part, __fifth_link, 4, __fifth_success, __fifth_fail)
    ending(user_evidences)


# story()

disclaimer = '''Не забывайте, курение вредит вашему здоровью!'''
