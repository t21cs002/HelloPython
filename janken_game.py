'''
Created on 2023/10/13

@author: t21cs002
'''
import random

class JankenGame:
    def __init__(self):
        self.choices = ['グー', 'チョキ', 'パー']
        self.results = ['Aの勝ち', 'Bの勝ち', '引き分け']

    def play(self, player_a_choice, player_b_choice):
        # 勝敗判定
        if player_a_choice == player_b_choice:
            result = self.results[2]  # 引き分け
        elif (player_b_choice - player_a_choice + 3) % 3 == 1:
            result = self.results[0]  # プレイヤーAの勝ち
        else:
            result = self.results[1]  # プレイヤーBの勝ち

        # 出力
        output = f'Aの手: {self.choices[player_a_choice]} v.s. Bの手: {self.choices[player_b_choice]} → {result}'
        return output

# Usage example
if __name__ == "__main__":
    game = JankenGame()
    
    # プレイヤーAとプレイヤーBの手をランダムに選択
    player_a_choice = random.randint(0, 2)
    player_b_choice = random.randint(0, 2)

    result = game.play(player_a_choice, player_b_choice)
    print(result)