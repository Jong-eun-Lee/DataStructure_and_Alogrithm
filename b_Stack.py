## Stack
# 작성자: 이종은

class Stack: # 클래스 생성
    def __init__(self): # 메소드 생성
        self.items = []
    '''
    __init__은 생성함수.
    괄호 안의 self는 생성된 객체 자체를 가리킴.
    
    S = Stack()
    과 같이 인스턴스 만들어 주면 자동으로 생성함수가 호출됨.
    
    생성함수를 작성하지 않으면
    인스턴스 생성 시
    객체는 아무런 attribute가 없게 됨.
    
    self.__속성이름
    과 같이 만들면 클래스 안에서만 접근할 수 있는
    비공개 속성이 됨.
    '''

    def push(self, val):
        self.items.append(val)
    # push의 time complexity는 O(1)
        
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    # O(1)
            
    def top(self):
        try:
            return self.items[-1] # 가장 마지막에 있는 것 return. 삭제는 안 함.
        except IndexError:
            print("Stack is empty")
    # O(1)
    
    def __len__(self):
        return len(self.items)
    # O(1)
    # 왜냐하면 items라는 리스트에서
    # 원소 개수가 몇 개인지 항상 관리하고 있기 때문    
    '''
    __len__ 은 스페셜 메소드다.
    len(S)
    를 호출하면 파이썬은 자동으로
    S에 있는 스페셜 메소드 __len__()을 부름.
    즉 len(S)를 실행하면
    S.__len()__을 실행한 것과 같음.
    '''
    
    def isEmpty(self):
        return self.__len__() == 0
    # O(1)