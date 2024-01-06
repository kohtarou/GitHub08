import random

# キャラクターのレア度と確率
characters = {
    "星4": 7.0,
    "星3": 35.0,
    "星2": 58.0
}

# ダイヤ消費数
diamonds_per_pull = 5

# ガチャ回数、消費ダイヤ数、引いたキャラクター
pull_count = 0
total_diamonds = 0
pulled_characters = []

def pull_gacha(times):
    global pull_count
    global total_diamonds
    global pulled_characters

    for _ in range(times):
        pull_count += 1
        total_diamonds += diamonds_per_pull
        pulled_characters.append(pull_character())

def pull_character():
    rand_num = random.uniform(0, 100)
    cumulative = 0
    for character, probability in characters.items():
        cumulative += probability
        if rand_num <= cumulative:
            return character

def reset():
    global pull_count
    global total_diamonds
    global pulled_characters

    pull_count = 0
    total_diamonds = 0
    pulled_characters = []

def print_status():
    print("ガチャ回数:", pull_count)
    print("消費ダイヤ数:", total_diamonds)
    print("引いたキャラクター:", pulled_characters)

while True:
    print("\n1: ガチャを一回引く")
    print("2: ガチャを十回引く")
    print("3: ステータスを表示")
    print("4: リセット")
    print("5: 終了")
    choice = input("選択してください: ")
    if choice == "1":
        pull_gacha(1)
    elif choice == "2":
        pull_gacha(10)
    elif choice == "3":
        print_status()
    elif choice == "4":
        reset()
    elif choice == "5":
        break