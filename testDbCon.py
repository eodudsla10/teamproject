import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='nydb', charset='utf8')


# db 연결 함수
def conDB(con):
    print("===========연결됨===========")
    return con.cursor()

# db 연결해제 함수
def closeDB(con):
    print("===========해제함===========")
    con.close()

# db에서 사용자 input searchword
def SearchWord(sword):
    curs = conDB(conn)
    sql = "select P_Title from PRIDATA where P_Title like %s"
    like_val = f'%{sword}%'
    curs.execute(sql, like_val)

    data = curs.fetchall()
    
    for i in range(len(data)):
        print(data[i])
    closeDB(conn)

# db에서 모든데이터 출력
def selectall():
    curs = conDB(conn)
    sql = "select * from PRIDATA"
    curs.execute(sql)

    data = curs.fetchall()

    for i in range(len(data)):
        print(data[i])

    closeDB(conn) 

# db에서 사용자 input searchstring
def SearchData(searchStr):
    curs = conDB(conn)
    strlist = tuple(searchStr.split(' '))
    listsize = len(strlist)

    # 1) 타이틀 이름 겹치는 거 뽑아내는 부분========================================================
    data = [0 for i in range(listsize)]
    for i in range(listsize):
        sql = "select P_Title from PRIDATA where P_Title like %s"
        like_val = f'%{strlist[i]}%'
        curs.execute(sql, like_val)

        data[i] = curs.fetchall()
    # ========================================================================================

    # 2)카테고리가 겹치는 거 뽑아내는 부분=========================================================
    tempCate = [0 for i in range(listsize)]   # 매칭이 된 키워드만 따로 다시 저장하는 용도

    sql = "select C_Value from CATEGORY"
    curs.execute(sql)
    dataCategory = curs.fetchall()

    cnt = 0
    for i in range(listsize):  
        for j in range(len(dataCategory)):
            if strlist[i] in dataCategory[j]:
                tempCate[cnt] = strlist[i]
                cnt += 1

    tempCate = list(set(tempCate))  # 임의로 넣어둔 0을 제거한다
    tempCate.remove(0)

    for i in range(len(tempCate)):
        sql = "select pri.P_Title from PRIDATA as pri join CATEGORY as c on c.C_Id = pri.P_Category where c.C_Value = %s"
        like_val = f'{tempCate[i]}'
        curs.execute(sql, like_val)

        selectedCateData = curs.fetchall()
        # print(selectedCateData)
    # ========================================================================================

    # 1, 2 겹치는거 거르는 부분=================================================================
    for i in range(len(selectedCateData)):
        for j in range(len(data)):
            if selectedCateData[i] in data[j]:
                print(selectedCateData[i])
    # ========================================================================================

    closeDB(conn)

# word = input()
word = '팰팍 룸메이트 구함'
SearchData(word)
# SearchWord(word)
# selectall()+