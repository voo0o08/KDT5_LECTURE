# 12.4
game = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(game['health'])
print(game['movement_speed'])

# 12.5 딕셔너리에 게임 캐릭터 능력치 저장하기
'''
표준입력1 : health health_regen mana mana_regen
표준입력2 : 575.6 1.7 338.8 1.63
'''
info = input("능력치 종류 : ").split()
info_val = input("능력치 종류 값: ").split()

game = {info[0]: info_val[0],
        info[1]: info_val[1],
        info[2]: info_val[2],
        info[3]: info_val[3]}
print(game)