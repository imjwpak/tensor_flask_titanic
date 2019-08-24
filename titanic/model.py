'''
survival	생존여부	0 = No, 1 = Yes
pclass	승선권	1 = 1st, 2 = 2nd, 3 = 3rd
sex	성별
Age	나이
sibsp	동반한 형제, 자매, 배우자
parch	동반한 부모, 자식
ticket	티켓번호
fare	티켓의 요금
cabin	객식번호
embarked	승선한 항구명	C = 쉐부로, Q = 퀜즈타운, S = 사우스햄튼
'''
import pandas as pd
import numpy as np

class TitanicModel:
    def __init__(self):
        self._context = None
        self._fname = None
        self._train = None
        self._test = None
        self._test_id = None

    @property # 인스턴스 변수
    def context(self) -> object:return self._context # getter : Java에서 getContext라고 보면 됨

    @context.setter
    def context(self, context): self._context = context # setter

    @property
    def fname(self) -> object:return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object:return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object:return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def test_id(self) -> object:return self._test_id

    @test_id.setter
    def test_id(self, test_id): self._test_id = test_id
    
    # -> 이게 있으면 getter라고 보면 됨
    def new_file(self) -> str: return self._context + self._fname # lambda 메모리를 쓰는건

    def new_dfame(self) -> object:
        file = self.new_file()
        return pd.read_csv(file)

    # 프로세스 정리. 다른 곳에서 이걸 호출해서 사용됨. feature 정리할때 사용.
    def hook_process(self, train, test) -> object:
        print('---------------1.  ------------------------')
        print('---------------2.  ------------------------')
        print('---------------3.  ------------------------')
        









