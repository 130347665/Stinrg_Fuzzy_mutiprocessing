import pymysql
import xlrd
import pymysql
import xlrd
def connect_database(dataname,user,password):
    db = pymysql.connect(host='127.0.0.1',port=3306,user=user,passwd=password,db=dataname, charset='utf8')
    return db
def read_excel(url):
    workbook = xlrd.open_workbook(r''+url)
    # 獲取所有sheet
    workbook.sheet_names()
    # 獲取 第一個 sheet
    sheet1_name = workbook.sheet_names()[0]
    print("第一個Sheet名稱："+sheet1_name)
    # 根據sheet索引或者名稱獲取sheet內容
    sheet1 = workbook.sheet_by_name('需分類的資料')
    # sheet的名稱，行數，列數
    # rows = sheet1.row_values(0)  # 獲取第1行內容
    # cols = sheet1.col_values(0)  # 獲取第1列內容
    # 獲取單元格內容的三種方法
    # sheet2.cell(1, 0).value.encode('utf-8')
    # sheet2.cell_value(1,0).encode('utf-8')
    # sheet2.row(1)[0].value.encode('utf-8')
    return sheet1
if __name__ == '__main__':
    conn = connect_database("sql_prductname", "root", "123456")
    cursor = conn.cursor()
    # 查
    # check_sql = "select * from student"
    # cursor.execute(check_sql)
    # data = cursor.fetchall()
    # for i in data:
    #     print(i)
    # 改
    # sql = " update student set age = 999 where name = 'liudehua'"
    # cursor.execute(sql)
    # conn.commit()
    # 增 和 改 差不多 除了sql改變其他不變
    #------------------獲取Excel表中的內容-----------
    sheet1 = read_excel('C:\\Users\\user\\Desktop\\Excel歷年資料\\爬取歷史品名\\品名大數據(未分類.xlsx')
    cols_1 = sheet1.col_values(0)  # 獲取第1列內容
    #print(cols_1)
    #cols_2 = sheet1.col_values(1)  # 獲取第1列內容
    #cols_3 = sheet1.col_values(2)  # 獲取第1列內容

    #print(cols_2)
    #print(cols_3)
    #------------------end-------------------------
    for i in range(2,len(cols_1)):
        print(cols_1[i])
        sql = "insert into product_total_name values("+str(i)+",'" +cols_1[i]+"')"
        print(sql)
        cursor.execute(sql)
    conn.commit()