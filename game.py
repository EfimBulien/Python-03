import json
import csv
import random

def game_start():
    while True:
        choice = input('Начать игру? (Да/Нет): ').lower()
        if choice == 'да':
            print()
            choose_character()
            break
        elif choice == 'нет':
            print('До свидания.')
            breakpoint()
            break
        else:
            print("Введите 'Да' или 'Нет'.")

def saves():
    print('Прежде, чем начать игру, вы должны определиться с выбором вашего героя. Как вас зовут?')
    name = str(input('Введите ваше имя: '))
    data = {
        "name": name
    }
    with open('save.json', 'w') as file:
        json.dump(data, file, indent=4)


    def save_to_csv(user_name, this_stage):
        data = [[user_name, this_stage]]

        with open('save_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
def choose_character():
    
    while True:
        try:
            
            characters = ['Маг', 'Асассин', 'Лучник', 'Варвар']
            descriptions = {'Маг': 'Вы владеете различными заклинаниями.','Асассин': 'Вы достаточно ловки, чтобы избежать атак врага и нанести точечный удар.','Лучник': 'Меткая стрелба - ваш конёк! Издалека вы куда опаснее для врагов.','Варвар': 'Только грубая сила и топор. Решайте все проблемы самым простым способом.'}
            for i, character in enumerate(characters):
                    print(f'{i+1}. {character}')
            try:
                choice_characters = int(input('Выберете класс своего персонажа: '))
                character = characters[int(choice_characters)-1]
                print(f'Вы {character.lower()} по имени {name}.')
                print(f'{descriptions[character]}')
                game_loop()
            except ValueError:
                print('Вы не выбрали персонажа.')
            if character == characters[int(choice_characters)-1]:
                break
        except:
            print('Попробуйте снова.')
            choose_character()
            break

def game_loop():
    
    while True:
        print('Находясь в городе вы понимаете, что жизнь здесь скучная и рутинная. Вы решаете отправиться в новое приключение, дабы найти сокровище или раздобыть немного денег.')
        choice = input('Вы согласный отправиться в путь? (Да/Нет): ').lower()
        if choice == 'да':
            print('Удачи в приключении!')
            game()
            break
        elif choice == 'нет':
            print('До свидания.')
            breakpoint()
            break
        else:
            print("Введите 'Да' или 'Нет'.")

def game():
    
    try:
        print('В очередном своём приключении вы заблудились в глубоком темном лесу... посреди чащи в ночи стоит странный незнакомец в темно-сером потрёпанном плаще.')
        actions = {'1': 'Поговорить', '2': 'Попробовать сразиться', '3': 'Пройти мимо не обращая внимания'}
        while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Поговорить\'.')
                    talk()
                    break
                case '2':
                    print('Вы выбрали действие \'Попробовать сразиться\'.')
                    fight_1()
                    break
                case '3':
                    print('Вы выбрали действие \'Пройти мимо не обращая внимания\'.')
                    continue_path()
                    break
                case _:
                    print('Неверный выбор. Попробуйте еще раз.')
                    break
    except:
            print('Попробуйте снова.')
            game()

def talk():
    
    name_n = 'Авгур'
    print(f'Заговорив с подозрительным незнакомцем, выяснилось, что на самом деле вы говорите с могущественным некромантом по имени {name_n}.')
    print('Так просто вы уже не уйдёте, вам стоит рещить, что делать дальше.')
    actions = {'1': 'Попробовать договориться', '2': 'Попробовать сразиться'}
    while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            try:
                choice = input('Введите номер действия: ')
                match choice:
                    case '1':
                        print('Вы выбрали действие \'Попробовать договориться\'.')
                        dialog()
                    case '2':
                        print('Вы выбрали действие \'Попробовать сразиться\'.')
                        fight_1()
                        break
            except:
                print('Попробуйте снова.')
                talk()
                break
                    
def dialog():
    
    name_n = 'Авгур'
    dialog = random.randint(1,20)
    if dialog <= 10:
        print('Благодаря вашему участию в гильдии и невероятному красноречию удалось убедить злого некроманта \'Авгура\' отпустить вас.')
        continue_path()
    else:
        print('Не смототря на ваши превосходные умения убеждения и навыки красноречия вам не удалось убедить некроманта. Ваши попытки убеждения лишь рассмешили \'Авгура\'.')
        print(f'Почувствовав вашу нечтожность, {name_n} решает убить вас. Придется защищаться.')
        fight_1()

def continue_path():
    
    try:
        print('Вы решили продолжить свой путь. На вашем пути вы видите диких животных, как бы вы поступили?')
        actions = {'1': 'Попробовать сразиться', '2': 'Пройти мимо не обращая внимания'}
        while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Попробовать сразиться\'.')
                    print('Собравшись с мыслями вы принимаете решение сразиться с ними.')
                    fight_2()
                    break
                case '2':
                    print('Вы выбрали действие \'Пройти мимо не обращая внимания\'.')
                    print('Вы встречаете диких животных, сумев их обойти вы продолжаете свой путь.')
                    continue_path_2()
                    break
    except:
        print('Попробуйте снова.')
        continue_path()
        
def continue_path_2():
    
    try:
        print('Вы натыкаетесь на старую хижину.')
        actions = {'1': 'Зайти в хижину', '2': 'Продолжить свой путь'}
        while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Зайти в хижину\'.')
                    go_inside()
                    break
                case '2':
                    print('Вы выбрали действие \'Продолжить свой путь\'.')
                    final_1()
                    break
    except:
        print('Попробуйте снова')
        continue_path_2()

def go_inside():
    
    try:
        print('Вы заходите внутрь старой заброшенной хижины. Вы видите обгоревший домоход и сундук рядон с ним.')
        actions = {'1': 'Исследовать дымоход', '2': 'Заглянуть внутрь сундука', '3':'Ничего не сделать и продолжить свой путь'}
        while True:
            print('Что вы сделаете?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Исследовать дымоход\'.')
                    chimney()
                    break
                case '2':
                    print('Вы выбрали действие \'Заглянуть внутрь сундука\'.')
                    chest()
                    break
                case '3':
                    print('Вы выбрали действие \'Ничего не сделать и продолжить свой путь\'.')
                    print('Ничего не найдя внутри вы возвращаетесь на большую дорогу.')
                    final_1()
                    break
    except:
        print('Попробуйте снова')
        go_inside()

def chimney():
    
    win = random.randint(1, 18)
    if win == 2:
        print('В дымоходе вы нахолите небольшой свёрток, внутри которого лежит кусочек золота.')
        final_3()
    else:
        print('Ничего не найдя внутри вы возвращаетесь на большую дорогу.')
        final_1()
        
def chest():
    
    win = random.randint(1, 6)
    if win == 2:
        print('Внутри непреметного старого сундучка вы находите сокровища, которые и искали.')
        final_3()
    else:
        print('Ничего не найдя внутри вы возвращаетесь на большую дорогу.')
        final_1()
    
def fight_1():
    
    print('Собравшись с мыслями вы принимаете решение вступить в бой с могущественным неркомантом \'Авгуром\'.')
    win = random.randint(1, 15)
    if win // 5 or 3 == 0:
        print('Вы отважно сражались с \'Авгуром\' и в итоге победили!')
        continue_path()
    else:
        final_2()

def fight_2():
    
    win = random.randint(2, 12)
    if win == 2 or 4 or 6:
        print('Вы отважно сражались и в итоге одержали победу!')
        continue_path_2()
    else:
        final_2()
    
def final_1(user_name, this_stage):
    data = [[user_name, this_stage]]
    with open('save_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    print('В конце концов, вы смогли добраться до ближайшей таверны, в которой вы и планиуете переночевать.')
    print('Добравшись до ближайшей таверны вы засыпаете в комнате. Ваше приключение завершино и вы можете начать его снова.')
    game_start(user_name, this_stage)
  
def final_2(user_name, this_stage):
    
    print('Потеряв все силы вы теряете сознание и погибаете. Это был ваш последний бой, на данном моменте ваши приключения заканчиваются. Конец игры.')
    print('Ваше приключение завершино и вы можете начать его снова.')
    game_start(user_name, this_stage)   
    
def final_3(user_name, this_stage):
    data = [[user_name, this_stage]]
    with open('save_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    print('Вместе со своим сокровищем вы смогли добраться до ближайшей таверны, в которой вы и планиуете переночевать.')
    print('Вы победили!')
    print('Ваше приключение завершино и вы можете начать его снова.')
    game_start(user_name, this_stage)
    
name = str
game_start() 
