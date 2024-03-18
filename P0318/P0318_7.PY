class Tv():
    serial_no=0  #>>클래스변수 공통 관리
    
    def __init__(self,color,name,size):
        self.color=color
        self.name=name
        self.size=size    #>>인스턴트 변수
        Tv.serial_no +=1  #>> 클래스 변수 #자동으로 번호를 순차적으로 매겨준다.
                            # 모든 클래스에서 공통으로 사용하는 변수
        
    def tv_print(self):
        print(f"tv : {self.serial_no},{self.color},{self.name},{self.size}")
        
c1=Tv("whilte","스마트tv",100)
c1.tv_print()

c2=Tv("black","fhd tv",70)
# c2.serial_no=2
c2.tv_print()

c3=Tv("silver","oled tv",82)
# c3.serial_no=3
c3.tv_print()