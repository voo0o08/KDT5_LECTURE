'''
게임 동작 파일
객체 생성 및 동작

과제 설명 :
속성 : 무늬, 번호
딜러, 흥부, 놀부 총 3개의 객체를 만든다.

-딜러 동작
동작1. 카드 생성
동작2. 랜덤하게 섞기
동작3. 각 선수들에게 카드 나눠주기

- 선수 동작
동작1. 카드 받기
동작2. 중복 카드 open
동작3. 카드 관리 (open / holding)

-> 과제는 cardgame.py 안에서 제어해야함!!(카지노 사장릠이라 생각)
'''
from card import Card
from player import Player
from gamedealer import GameDealer

def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부") # 객체 player1
    player2 = Player("놀부") # 객체 player2
    dealer = GameDealer() # 객체 dealer

    dealer.card_draw(player1, player2, 10)
    player1.display_two_card_lists()
    player2.display_two_card_lists()
    while True:
        user = input("********* 다음 단계 진행을 위해 Enter 키를 누르세요! *********")
        if user != "":
            print("user가 게임 종료를 원합니다.")
            break # user가 enter가 아닌 다른 것을 입력하면 게임 중단으로 판단

        if len(player1.holding_card_list) == 0 or len(player2.holding_card_list) == 0:
            print("플레이어의 카드가 모두 소진되었습니다.")
            break
        # 각 player에게 4장씩 카드를 나누어 줌
        dealer.card_draw(player1, player2, 4)
        # dealer.print_deck()
        player1.check_one_pair_card()
        player2.check_one_pair_card()
        if len(dealer.deck)==0:
            print("딜러의 카드가 모두 소진되었습니다.")
            break

# main문
if __name__ == "__main__":
    play_game()