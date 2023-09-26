import tkinter
from tkinter import*
from tkinter import ttk
from decimal import Decimal



def simplex(coef, ogr, table):
    n = len(coef)
    nn = n
    for i in range(len(ogr)):
        if ogr[i][n] < 0:
            for j in range(n + 1):
                ogr[i][j] = ogr[i][j] * (-1)       #проверяю А0 на неотриөателҗностҗ
    aa = []
    A0 = []
    for i in range(n+1):
        a = []
        for j in range(len(ogr)):
            a.append(ogr[j][i])
        if i == n:
            A0 = a
        else:
            aa.append(a)
    base = []
    for i in range(len(ogr)):
        bas = []
        for j in range(len(ogr)):
            if j == i:
                bas.append(1)
            else:
                bas.append(0)
        if bas in aa:
            base.append(aa.index(bas))
            print('base = ', base)
        else:
            aa.append(bas)          #срздаю базисные векторы
            base.append(n)
            n+=1

    for i in range(n - nn):
        coef.append('-m')
    iter = 0
    return tabl(n, base, aa, A0, nn, coef, iter, table)

def tabl(n, base, aa, A0, nn, coef, iter, table):
    global ind_1, ind, out
    delta = []
    delta_1 = []
    delta_a0 = 0
    for i in range(n):
        delta.append(0)
        delta_1.append(0)
    fl1 = False
    for i in range(len(base)):
        if '-m' == str(coef[base[i]]):
            fl1 = True
    if fl1 == False:
        for i in range(n):
            if i >= nn:
                for j in range(len(base)):
                    aa[i][j] = 0
    print("")
    print("---------------")
    print("")
    print(coef)
    print('base = ', base)
    for i in range(n):
        for j in range(len(base)):

            if coef[base[j]] == '-m':
                # print(delta_1)
                delta_1[i] -= Decimal(str(aa[i][j]))
            else:
                delta[i]+=Decimal(aa[i][j]*Decimal(coef[base[j]]))
        if coef[i] == '-m':
            delta_1[i]+=1
        else:
            delta[i] -= coef[i]
    for i in range(len(base)):
        if coef[base[i]]!='-m':
            delta_a0 += A0[i]*coef[base[i]]
    print('del = ', delta)
    print('del` = ', delta_1, '   ', delta_a0)

    if fl1 == False:
        for i in range(len(delta_1)):
            delta_1[i] = 10

    flag = True
    minn = 10
    min_1 = 10
    ind_1 = 0
    for i in range(len(delta)):
        if (delta[i]<0) or(delta_1[i]<0):
            flag = False
            if delta[i]<0 and delta[i]<minn:
                minn = Decimal(delta[i])
                ind = i
            if delta_1[i]<0 and delta_1[i]<min_1:
                min_1 = Decimal(delta_1[i])
                ind_1 = i
    print('min = ', minn)
    lst = []
    lst_1 = []
    lst_1.append('№')
    lst_1.append("Base")
    lst_1.append("C(b)")
    for i in range(n + 1):
        lst_1.append("A" + str(i))
    lst.append(lst_1)
    for i in range(len(base)):
        lst_2 = []
        for j in range(n + 4):
            if (j == 0):
                lst_2.append(str(i + 1))
            elif (j == 1):
                lst_2.append("A" + str(base[i] + 1))
            elif (j == 2):
                lst_2.append(str(coef[base[i]]))
            else:
                lst_2.append(Decimal(aa[j - 4][i]).quantize(Decimal('1.00')))
        lst.append(lst_2)
    lst_3 = []
    for i in range(n + 4):
        if (i <= 1):
            lst_3.append(" ")
        if (i == 2):
            lst_3.append("del'")
        if (i == 3):
            lst_3.append(str(delta_a0))
        if (i > 3):
            lst_3.append(str(Decimal(delta[i - 4]).quantize(Decimal('1.00'))))
    lst_4 = []
    for i in range(n + 4):
        if (i <= 1):
            lst_4.append(" ")
        if (i == 2):
            lst_4.append("del''")
        if (i == 3):
            lst_4.append(" ")
        if (i > 3):
            lst_4.append(str(Decimal(delta_1[i - 4]).quantize(Decimal('1.00'))))

    lst.append(lst_3)
    lst.append(lst_4)
    lst.append('')
    clm = []
    for i in range(len(lst[0])):
        clm.append(lst[0][i])
    if iter == 0:
        table['columns'] = clm

    for i in range(len(lst)):
        print(lst[i])


    for row in lst:
        table.insert('', 'end', values=row)
    table.column("#0", width=0)
    # table.column("#1", width=50, minwidth=10)
    for i in range(len(lst[0])):
        table.column(lst[0][i], width = 100, minwidth=20)
    if flag:
        table.insert("", "end", values="Ответ:   "+str(Decimal(delta_a0).quantize(Decimal("1"))))
        table.pack(fill=tkinter.BOTH, side=tkinter.RIGHT, padx=10, pady=10)
        return Decimal(delta_a0).quantize(Decimal("1"))
    min_otn = 10000000000
    if min_1<0:
        for i in range(len(base)):
            if aa[ind_1][i]>0:
                if A0[i]/aa[ind_1][i]<min_otn:
                    min_otn = A0[i]/aa[ind_1][i]
                    out = i
                    print('minotn = ', min_otn)

    elif minn<0:
        for i in range(len(base)):
            if aa[ind][i]>0:
                print('-----', A0[i]/aa[ind][i])
                if A0[i]/aa[ind][i]<min_otn:

                    min_otn = A0[i]/aa[ind][i]
                    out = i
                    print('minotn = ', min_otn)

    lst = []
    lst_1 = []
    lst_1.append('№')
    lst_1.append("Base")
    lst_1.append("C(b)")
    for i in range(n + 1):
        lst_1.append("A" + str(i))
    lst.append(lst_1)
    for i in range(len(base)):
        lst_2 = []
        for j in range(n + 4):
            if (j == 0):
                lst_2.append(str(i + 1))
            elif (j == 1):
                lst_2.append("A" + str(base[i] + 1))
            elif (j == 2):
                lst_2.append(str(coef[base[i]]))
            else:
                lst_2.append(Decimal(aa[j - 4][i]).quantize(Decimal('1.00')))
        lst.append(lst_2)
    lst_3 = []
    for i in range(n + 4):
        if (i <= 1):
            lst_3.append(" ")
        if (i == 2):
            lst_3.append("del")
        if (i == 3):
            lst_3.append(str(Decimal(delta_a0).quantize(Decimal('1.00'))))
        if (i > 3):
            lst_3.append(str(Decimal(delta[i - 4]).quantize(Decimal('1.00'))))
    lst.append(lst_3)
    lst.append('')
    for i in range(len(lst)):
        print(lst[i])

    # clm = []
    # for i in range(len(lst)):
    #     clm.append(lst[i])
    # if iter == 0:
    #     table['columns'] = clm
    # table.column("#0", width = 0)
    # if iter == 0:
    #     table['columns'] = clm
    # for row in lst:
    #     table.insert('', 'end', values=row)
    # table.column("")
    # table.pack(fill=tkinter.BOTH, side=tkinter.RIGHT, padx=10, pady=10)

    if delta_1[ind_1]<0:
        ind = ind_1
    print('a0 = ',A0)
    print("")
    for i in range(len(aa)):
        print(aa[i])
    print("")
    print("---------------")
    print("")
    # for i in range(n+4):
    #     root.grid_columnconfigure(i+1, minsize=90)
    # root.grid_rowconfigure(0, minsize=150+150*len(base))
    # ooo = Label(text = "").grid(row = 0, column = iter*(len(base)+3))
    # n_lbl = Label(text = "№",font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4" ).grid(row = 1+iter*(len(base)+4), column = 1)
    # base_lbl = Label(text = "Base",font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 1+iter*(len(base)+4), column = 2)
    # cb_lbl = Label(text = "C(b)", font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 1+iter*(len(base)+4),column = 3)
    # for i in range(n+1):
    #     if i>nn and (i-1)not in base:
    #         continue
    #     else:
    #         a_lbl = Label(text = "A"+str(i),font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 1+iter*(len(base)+4),column = 4+i)
    # for i in range(len(base)):
    #     lbl = Label(text = str(i+1),font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 2+i+iter*(len(base)+4), column = 1)
    # for i in range(len(base)):
    #     b_lbl = Label(text = "A"+str(base[i]+1),font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 2+i+iter*(len(base)+4), column = 2)
    # for i in range(len(base)):
    #     cb = Label(text = str(coef[base[i]]), font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 2+i+iter*(len(base)+4), column = 3)
    # for i in range(len(base)):
    #     a0 = Label(text = str(A0[i]), font =  ('Malgun Gothic Semilight', 18),bg = "#FFFAF4").grid(row = 2+i+iter*(len(base)+4), column = 4)
    # for i in range(len(base)):
    #
    #         for j in range(n):
    #             if j >= nn and (j - 1) not in base:
    #                 continue
    #             else:
    #                 ai_lbl = Label(text=str(aa[j][i]), font=('Malgun Gothic Semilight', 18),bg="#FFFAF4").grid(row=2+i+iter*(len(base)+4), column = 5+j)



    iter+=1
    return(iteration(coef, aa, base, ind, out,n, A0, nn, iter,table))

def iteration(coef, aa, base, ind, out,n, A0, nn, iter,table):
    oporny = Decimal(aa[ind][out])
    aa_new = []
    base[out] = ind
    print('oporny = ',oporny)
    for i in range(n):
        anew = []
        for j in range(len(base)):
            if j == out:
                anew.append(Decimal(aa[i][j]/oporny))
            else:
                anew.append(Decimal(aa[i][j]-(aa[i][out]*aa[ind][j])/oporny))
        aa_new.append(anew)
    A0new = []
    for i in range(len(base)):
        # print(coef[base[i]])
        if i == out:
            A0new.append(Decimal(A0[i]/oporny))
        else:
            print(A0[i],'  ', A0[out],'  ', aa[ind][i],'  ', oporny)
            print("")
            print("")
            A0new.append(Decimal(A0[i] -((A0[out]*aa[ind][i])/oporny)))
    A0 = A0new
    aa = aa_new
    return tabl(n, base, aa, A0, nn, coef, iter, table)



def func():
    global  var, next, plus, coef_1, ogr_1
    func_text = Label(text = 'целевая функция',
                  fg = black, bg = backgr,
                  font = ('Malgun Gothic Semilight', 18)).place(x = 25, y = 120)
    number = int(num_of_var.get())
    num_ogr = int(num_of_ogr.get())
    x = 25+250
    y = 128

    coef_1 = []
    ogr_1 = []

    for i in range(number):
        koef = Entry(width = 5, font =  ('Malgun Gothic Semilight', 15),bg = "#FFFAF4")
        koef.place(x = x+i*100, y = y, width = 35, height = 26)
        coef_1.append(koef)
        var = Label(text = "x"+str(i+1), fg = black, bg = backgr,
                  font = ('Malgun Gothic Semilight', 17)).place(x = x+i*100+35, y = 120)
        if (i!= number -1):
            plus = Label(text = "+",  fg = black, bg = backgr,
                     font = ('Malgun Gothic Semilight', 18)).place(x = x+i*100+68, y = 120)
        else:
            maxx = Label(text = "-> max",  fg = black, bg = backgr,
                     font = ('Malgun Gothic Semilight', 18)).place(x = x+i*100+68, y = 120)

    limit_text = Label(text='ограничения',
                      fg=black, bg=backgr,
                      font=('Malgun Gothic Semilight', 18)).place(x=25, y=160)
    y = 175

    for i in range(num_ogr):
        lim = []
        for j in range(number+1):
            koeff = Entry(root, width=5, font=('Malgun Gothic Semilight', 15), bg = '#FFFAF4')
            koeff.place(x=x + j * 100, y=y+i*50, width=35, height=26)
            lim.append(koeff)
            if(j<number):
                var = Label(text="x" + str(j + 1), fg=black, bg=backgr,
                        font=('Malgun Gothic Semilight', 17)).place(x=x + j * 100 + 35, y=170+i*50)
            if (j < number - 1):
                plus = Label(text="+", fg=black, bg=backgr,
                             font=('Malgun Gothic Semilight', 18)).place(x=x + j * 100 + 68, y=170+i*50)
            elif(j<number):
                equal = Label(text = "=", fg = black, bg = backgr,
                              font=('Malgun Gothic Semilight', 18)).place(x=x + j * 100 + 68, y=170+i*50)
        ogr_1.append(lim)
    solution_btn = Button(text = "найти решение", command = lambda:fin(coef_1, ogr_1), font=('Malgun Gothic Semilight', 15))
    solution_btn.place(x = 400, y = 170+i*50+50)


def fin(coef_1, ogr_1):
    global table_frame, scr, table
    coef = []
    ogr = []
    print(coef_1[0].get())
    for i in range(len(coef_1)):
        coef.append(int(coef_1[i].get()))
    for i in range(len(ogr_1)):
        puk = []
        for j in range(len(ogr_1[i])):
            puk.append(int(ogr_1[i][j].get()))
        ogr.append(puk)
    table_frame = Frame(root,width=200, height=200, bg = backgr).pack()
    scr = ttk.Scrollbar(table_frame)
    scr1 = ttk.Scrollbar(table_frame, orient='horizontal')
    scr1.pack(fill = tkinter.X, side = tkinter.BOTTOM)
    scr.pack(fill=tkinter.Y, side=tkinter.RIGHT)
    table = ttk.Treeview(master = table_frame, yscrollcommand=scr.set, xscrollcommand = scr1.set)
    scr.config(command=table.yview)
    scr1.config(command = table.xview())

    # clm = []
    # for i in range(20):
    #     clm.append(i)
    # print(clm)

    return(simplex(coef, ogr, table))



root = Tk()
root.title("Simplex")
# root.iconbitmap("icon.ico")
root.state('zoomed')
backgr = '#FFF8F0'
root['bg'] = backgr
brown = "#0C0C0A"
black = "#000000"

num_ofvar_text = Label(text = "количество переменных",fg = black, bg = backgr,
                  font = ('Malgun Gothic Semilight', 18)).place(x = 25, y = 10)

num_of_var = Entry(width = 5, font = ('Malgun Gothic Semilight', 14), bg = "#FFFAF4")
num_of_var.place(x = 320, y = 22, height = 26)
num_of_lim_txt = Label(text = "количество ограничений",
                       fg = black, bg = backgr,
                       font = ('Malgun Gothic Semilight', 18)).place(x = 25, y = 50)
num_of_ogr = Entry(width = 5, font = ('Malgun Gothic Semilight', 14), bg = "#FFFAF4")
num_of_ogr.place(x = 330, y = 60, height = 26)
ok = Button(text = "ok", command = func, font = ('Malgun Gothic Semilight', 14), bg = '#6C584C', fg = "#F0EAD2").place(x = 410, y = 35, width  = 40, height = 40)

# func_text.pack()

mainloop()

