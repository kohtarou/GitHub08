import random

total_draws = 0
total_diamonds = 0
results = []

def draw():
    rand = random.randint(0, 100)
    if rand < 7.0:
        return "星4"
    elif rand < 42.0:
        return "星3"
    else:
        return "星2"

def draw_one():
    global total_draws, total_diamonds
    result = draw()
    results.append(result)
    total_draws += 1
    total_diamonds += 5
    display_results()

def draw_ten():
    global total_draws, total_diamonds
    for i in range(10):
        result = draw()
        results.append(result)
    results.append("---")  # 仕切りを追加
    total_draws += 10
    total_diamonds += 50
    display_results()

def display_results():
    results_str = ""
    for result in results:
        if result == "---":
            results_str += "\n---\n"  # 仕切りを追加
        else:
            results_str += result + " "  # 結果を追加
    print(f"結果:\n{results_str}")
    print(f"合計回数: {total_draws}")
    print(f"合計ダイヤ: {total_diamonds}")

def reset():
    global total_draws, total_diamonds, results
    total_draws = 0
    total_diamonds = 0
    results = []
    display_results()