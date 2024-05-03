from card import Card
import random

class GameDealer:
    def __init__(self):
        self.deck = list()
        self.suit_number = 13
        self.make_deck() # deck 생성 함수 실행 후 shuffle 함수도 실행
        self.shuffle_deck()

    def make_deck(self):
        '''
        GameDealer객체는 card_suits,	card_number를 이용하여
        Card 객체 생성 및 리스트(deck)에 저장
        ex) card = Card('♠', 10)
        '''
        print("[GameDealer] 초기 카드 생성")
        card_suits = ['♠', '♥', '♣', '◆']
        card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for shape in card_suits:
            for num in card_numbers:
                card = Card(shape, num)
                self.deck.append(card)
        self.print_deck()

    def shuffle_deck(self):
        '''
        리스트 deck의 값을 랜덤하게 섞음
        '''
        print("[GameDealer] 카드 랜덤하게 섞기")
        random.shuffle(self.deck)
        self.print_deck()

    def card_draw(self, player1, player2, num):
        '''
        deck에서 10장씩 각 player에게 주고 dealer덱에서는 삭제
        num = 몇장의 카드를 나눠줄 것인지
        '''
        print("=" * 40)
        print(f"카드 나누어 주기: {num}장")
        for i in range(num):
            player1.holding_card_list.append(self.deck.pop())
            player2.holding_card_list.append(self.deck.pop())
        self.print_deck()
        # player1.display_two_card_lists()
        # player2.display_two_card_lists()

    # 반복문을 이용해 deck에 있는 Card 객체를 하나씩 출력 (1줄에 13장)
    def print_deck(self):
        print("-"*40)
        print("[GameDealer] 딜러가 가진 카드 수 :", len(self.deck))
        for idx, card in enumerate(self.deck, start=1):
            print(card, end=' ')
            if idx % 13 == 0:
                print()
        print()





if	__name__ == '__main__':
    dealer = GameDealer()

    # print(dealer.deck[1])