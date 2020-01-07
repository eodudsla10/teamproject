import list_data
import testDbCon
while (True):
    if __name__ == "__main__":
        Keyword = input("검색어를 입력하시오 :")
    extract = testDbCon.SearchData(Keyword)

    print("=================== 결과창입니다 =================== ")
    print(extract)
    print("================================================== ")
    
    Choice = input("선택하시오 :   [1] 메인으로 돌아가기 [2] 종료하기")
    if Choice == '2':
        break
print("프로그램을 종료합니다.")

