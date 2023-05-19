for i in range(0,5):
    class 수학:
        def 부피(self,a,b):
            결=3.14*a*a*b
            return 결
        def 겉넓이(self,a,b):
            결과=2*3.14*a*b+3.14*a*a+3.14*a*a
            return 결과
    반지름=input("반지름을 입력하세요:")
    높이=input("높이 입력:")
    중등수학=수학()
    print(f"반지름이 {반지름}이고, 높이가{높이}일 떄, 원기둥 겉넓이는{중등수학.겉넓이(int(반지름),int(높이))}이고,원기둥 부피는{중등수학.부피(int(반지름),int(높이))}입니다")

    class math:
        def 넓이(self,a,b):
            결과=a*b/2
            return 결과
    밑변=input("밑변을 입력하세요")
    높이=input("높이를 입력하세요")
    샥=math()
    print(f"밑변이 {밑변}이고, 높이가 {높이}일 떄, 삼각형의 넓이는 {샥.넓이(int(밑변),int(높이))}입니다.")