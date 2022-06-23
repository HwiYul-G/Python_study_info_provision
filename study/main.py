import tkinter as tk
from tkinter import CENTER, ttk

from CourseJson import CourseJson


def search_category_btn_click():
    # 이전 검색 삭제
    for i in searched_data_treeview.get_children():
        searched_data_treeview.delete(i)
    # 새롭게 추가
    category = course_combobox.get()
    cj = CourseJson()
    rows = cj.search_category(category) # type(rows) is 'list'
    for row in rows:
        treeValues = (cj.get_course_nm(row), cj.get_course_request_dt(row), cj.get_course_dt(row), cj.get_dept_name(row))
        searched_data_treeview.insert('','end',values=treeValues)
        
def search_course_nm_btn_click():
    for i in searched_data_treeview.get_children():
        searched_data_treeview.delete(i)
    course_nm = course_name_entry.get()
    cj = CourseJson()
    rows = cj.search_course_nm_2(course_nm)
    for row in rows:
        treeValues = (cj.get_course_nm(row), cj.get_course_request_dt(row), cj.get_course_dt(row), cj.get_dept_name(row))
        searched_data_treeview.insert('','end',values=treeValues)

def treeview_double_click(searched_data_treeview):
    item = searched_data_treeview.selection()
    print(item)

#  == main ==
root = tk.Tk()
root.title("학습 정보 이썬")
root.geometry('844x500') # 추후 수정
root.resizable(False,False)

label1 = tk.Label(root,text="강의 카테고리")
label1.grid(row=0,column=0,sticky='w',padx=15)

# 추후 list 정리 필요
course_list = ['4차 산업혁명','ACP','ATC','DIY','FAT','ITQ','ITQ한글','MOS','OA','TAT','가족생활','건강관리','공인중개사','관광통역안내사','교양상식'
            ,'글쓰기','기본이론','독일어','동양철학','디자인','러시아어','리눅스마스터','마술','문제풀이','문화','미술','미용','바리스타','반려동물','법정/의무'
            ,'베트남어','비지니스','사무자동화','사회복지사','서울시민대학','소셜미디어','스페인어','스포츠지도사','시니어취업','시험대비','실내건축','심화이론','아랍어'
            ,'악기','애니메이션','에너지교육','역사','영상제작','영어일반','영어회화','요리','요양보호사','워드프로세서','웹디자인','유통관리사','은퇴설계'
            ,'이탈리아어','인도네시아어','인문학','일본어일반','자녀교육','재테크','전기기능사','전기기사','전산세무','전산응용','전산회계','정보처리기사','정책','조리/미용','주택관리사' 
            ,'중국어 일반','직업상담사','창업','창의교육','철학','청소년상담사','취업','컴퓨터활용','컴퓨터활용능력','코딩','태국어','포르투갈어','포스트코로나','프랑스어'
            ,'프로그래밍','필기','한국사능력검정','한국어','한국어능력시험','핵심이론','회화'] 
course_combobox= ttk.Combobox(root,width=40, values=course_list)
course_combobox.grid(row=0,column=1,sticky='w')

label2 = tk.Label(root, text="강의명")
label2.grid(row=1,column=0, sticky='w',padx=15)

course_name_entry = ttk.Entry(root,width=43)
course_name_entry.grid(row=1,column=1,sticky='w')

search_btn1 = ttk.Button(root,text="카테고리 검색",command = search_category_btn_click)
search_btn1.grid(row=0,column=2)
search_btn2 = ttk.Button(root, text="강의명 검색", command=search_course_nm_btn_click)
search_btn2.grid(row=1, column=2)


searched_data_treeview = ttk.Treeview(root, columns=('강의명','수강신청 시작 일자','강의 시작 일자','기관명'),show='headings', height=20)
searched_data_treeview.column('강의명',width=320)
searched_data_treeview.column('수강신청 시작 일자',width=190)
searched_data_treeview.column('강의 시작 일자',width=130)
searched_data_treeview.column('기관명',width=80)
searched_data_treeview.heading('강의명',text="강의명",anchor=CENTER)
searched_data_treeview.heading('수강신청 시작 일자',text="수강신청 시작 일자",anchor=CENTER)
searched_data_treeview.heading('강의 시작 일자',text="강의 시작 일자",anchor=CENTER)
searched_data_treeview.heading('기관명',text="기관명",anchor=CENTER)
searched_data_treeview.grid(row=2,column=0,columnspan=2,padx=15,pady=10)
searched_data_treeview.bind("<Double-1>",treeview_double_click)


root.mainloop()