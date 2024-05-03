class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list() # 미공개 카드
        self.open_card_list = list() # 짝이 맞아 공개된 카드

    def add_card_list(self, card_list):
        pass

    def check_one_pair_card(self):
        '''
        heck 후 번호가 동일한 경우 holding에서 open으로 카드 이동
        '''
        print("="*40)
        print(f"{self.name}: 숫자가 같은 한쌍의 카드 검사")
        temp_pair_list = list() # 짝꿍 index list
        for i in range(len(self.holding_card_list)-1):
            for j in range(i+1, len(self.holding_card_list)):
                if self.holding_card_list[i].number == self.holding_card_list[j].number:
                    if i not in temp_pair_list and j not in temp_pair_list:
                        # print(self.holding_card_list[i].number)
                        # print(type(self.holding_card_list[i].number))
                        temp_pair_list.append(i)
                        temp_pair_list.append(j)
        temp_pair_list.sort(reverse=True) # 역순으로 돌려야 pop했을 떄 index 문제 안생김
        for idx in temp_pair_list:
            # print(idx)
            self.open_card_list.append(self.holding_card_list.pop(idx))
        # print(temp_pair_list)
        self.display_two_card_lists()

    def display_two_card_lists(self):
        '''
        두 개의 리스트를 출력하는 기능
        '''
        print("=" * 40)
        print(f"[{self.name}] Open card list:", len(self.open_card_list))
        for card in self.open_card_list:
            print(card, end="")
        print()

        print(f"[{self.name}] Holding card list:", len(self.holding_card_list))
        for card in self.holding_card_list:
            print(card, end=" ")
        print()