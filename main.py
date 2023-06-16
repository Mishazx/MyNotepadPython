import wx
import os
import datetime
import webbrowser

nameApp = "Текстовый редактор"
app = wx.App()

class Window(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (800,600))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show(True)

        bar = wx.MenuBar()  
        self.SetMenuBar(bar)

        buffer = None

        fileMenu = wx.Menu()
        changeMenu = wx.Menu()
        formatMenu = wx.Menu()
        viewMenu = wx.Menu()
        helpMenu = wx.Menu()

        bar.Append(fileMenu, "Файл")
        bar.Append(changeMenu, "Правка")
        bar.Append(formatMenu, "Формат")
        bar.Append(viewMenu, "Вид")
        bar.Append(helpMenu, "Cправка")

        newWindowItem = fileMenu.Append(wx.ID_ANY, "Новое Окно\tCTRL+SHIFT+N", "Создать новое окно")
        createItem = fileMenu.Append(wx.ID_ANY, "Создать\tCTRL+N", "Создать новый файл")
        openItem = fileMenu.Append(wx.ID_OPEN, "Открыть...\tCTRL+O", "Нажмите чтоб открыть файл")
        saveItem = fileMenu.Append(wx.ID_ANY, "Сохранить\tCTRL+S", "Сохрать файл")
        saveAsItem = fileMenu.Append(wx.ID_ANY, "Сохранить как...\tCTRL+SHIFT+S", "Сохранить как файл")
        fileMenu.AppendSeparator()
        settingsItem = fileMenu.Append(wx.ID_ANY, "Параметры страницы...", "Настройки страницы")
        printItem = fileMenu.Append(wx.ID_ANY, "Печать...\tCTRL+P", "Настройки страницы")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT, "Выход", "Нажмите чтоб выйти из программы")

        undoItem = changeMenu.Append(wx.ID_UNDO, "Отменить\tCTRL+Z", "Отменить последние действие")
        changeMenu.AppendSeparator()
        cutItem = changeMenu.Append(wx.ID_CUT, "Вырезать\tCTRL+X", "Вырезать текст")
        copyItem = changeMenu.Append(wx.ID_COPY, "Копировать\tCTRL+C", "Копировать текст")
        pasteItem = changeMenu.Append(wx.ID_PASTE, "Вставить\tCTRL+V", "Вставить текст")
        removeItem = changeMenu.Append(wx.ID_REMOVE, "Удалить\tDel", "Удалить текст")
        changeMenu.AppendSeparator()
        searchEthItem = changeMenu.Append(wx.ID_ANY, "Поиск с помощью Yandex...\tCTRL+E", "Поиск в яндекс")
        findItem = changeMenu.Append(wx.ID_ANY, "Найти...\tCTRL+F", "Найти в тексте")
        findNextItem = changeMenu.Append(wx.ID_ANY, "Найти далее\tF3", "Найти далее по тексту")
        findPastItem = changeMenu.Append(wx.ID_ANY, "Найти ранее\tSHIFT+F3", "Найти ранее по тексту")
        replaceItem = changeMenu.Append(wx.ID_ANY, "Заменить...\tCTRL+H", "Заменить в тексте")
        comeItem = changeMenu.Append(wx.ID_ANY, "Перейти...\tCTRL+G", "Перейти по тексту")
        changeMenu.AppendSeparator()
        selectAllItem = changeMenu.Append(wx.ID_ANY, "Выделить все\tCTRL+A", "Выделить весь текст")
        timeAndDateItem = changeMenu.Append(wx.ID_ANY, "Время и дата\tF5", "Время и дата")
                
        TransferWordsItem = formatMenu.Append(wx.ID_ANY, "Перенос по словам")
        fontItem = formatMenu.Append(wx.ID_ANY, "Шрифт...")

        zoomInItem = viewMenu.Append(wx.ID_ANY, "Увеличить", "Увеличить")
        zoomOutItem = viewMenu.Append(wx.ID_ANY, "Отдалить", "Отдалить")
        StrStateItem = viewMenu.Append(wx.ID_ANY, "Строка состояния", "Строка состояния")

        aboutItem = helpMenu.Append(wx.ID_ABOUT,"О программе", "Нажмите чтоб получить информацию о программе")

        self.Bind(wx.EVT_MENU, self.NewWindow, newWindowItem)
        self.Bind(wx.EVT_MENU, self.Create, createItem)
        self.Bind(wx.EVT_MENU, self.Open, openItem)
        self.Bind(wx.EVT_MENU, self.Save, saveItem)
        self.Bind(wx.EVT_MENU, self.SaveAs, saveAsItem)
        self.Bind(wx.EVT_MENU, self.Exit, exitItem)

        #self.bind(wx.EVT_MENU, self.Undo, undoItem)

        self.Bind(wx.EVT_MENU, self.SearchEth, searchEthItem)
        self.Bind(wx.EVT_MENU, self.Come, comeItem)
        self.Bind(wx.EVT_MENU, self.SelectAll, selectAllItem)
        self.Bind(wx.EVT_MENU, self.DateAndTime, timeAndDateItem)

        self.Bind(wx.EVT_MENU, self.About, aboutItem)

        newapp = None       

    # def __del__(self):
    #     self.Close(True)


    def Create(self, e):
        dlgCreate = wx.TextEntryDialog (self, 'имя входного файла', 'новый файл')
        if dlgCreate.ShowModal() == wx.ID_OK:
            self.filename = dlgCreate.GetValue() + '.txt'
            file = open(self.filename, 'w+')
            file.write(self.control.GetValue())
            file.close()
            self.SetName(f"{self.filename} - Текстовый редактор")

    def NewWindow(self, e):
        newapp = wx.App()
        newwnd = Window(self, nameApp)
        newapp.MainLoop()
        newwnd.__del__()

    def Open(self, e):
        self.dirname = ""
        dlgOpen = wx.FileDialog (self, "Выбрать файл", self.dirname, " ", "*.*", wx.FD_OPEN)
        if dlgOpen.ShowModal() == wx.ID_OK:
            self.filename = dlgOpen.GetFilename()
            self.dirname = dlgOpen.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            self.SetName(f"{self.filename} - Текстовый редактор")
            f.close()
        dlgOpen.Destroy()
        
    def Save(self ,e):
        try:
            f = open(self.filename, 'w')
            f.write(self.control.GetValue())
            f.close()
        except:
            wx.MessageBox("Создайте файл", "Ошибка", wx.ICON_HAND)

    def SaveAs(self, e):
        self.dirname = ""
        dlgSaveAs = wx.FileDialog (self, "Выбрать файл", self.dirname, " ", "*.*", wx.FD_SAVE)
        if dlgSaveAs.ShowModal() == wx.ID_OK:
            self.filename = dlgSaveAs.GetFilename()
            self.dirname = dlgSaveAs.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w+')
            f.write(self.control.GetValue())
            f.close()
        dlgSaveAs.Destroy()

    def Exit(self, e):
        self.Close (True)

    def Cut(self, e):
        self.text = self.FindFocus()
        if self.text is not None:
            self.text.Cut()

    def Paste(self, e):
        if self.text is not None:
            self.control.AppendText(self.text)

    def SearchEth(self, e):
        self.buffer = self.FindFocus()
        tmp = self.buffer.GetValue()
        url = f"https://yandex.ru/search/?text={tmp}&search_source=dzen_desktop_safe&lr=213"
        if tmp != "":
            webbrowser.open(url)

    def Come(self, e):
        dlgCome = wx.TextEntryDialog (self, 'Переход на строку файла', 'Переход на другую строку')
        if dlgCome.ShowModal() == wx.ID_OK:
            self.numberStr = dlgCome.GetValue()
            

    def SelectAll(self , e):
        self.control.SelectAll()    

    def DateAndTime(self ,e):
        today = datetime.datetime.now()
        today = today.strftime("%H:%M %d.%m.%Y")
        self.control.AppendText(str(today))
        

    def Undo(self, e):
        return 

    def About(self, e):
        dlg = wx.MessageDialog(self, "Текстовый редактор", "О текстовом редакторе", wx.OK)
        dlg.ShowModal()

    # Обработка событий
    def onKeyPress(self, e):
        keycode = e.GetKeyCode()
        print(keycode == wx.WXK_CONTROL)
        if keycode == wx.WXK_CONTROL & wx.WXK_SHIFT & wx.WXK_CONTROL_N:
            self.NewWindow(self, e)
        elif keycode == wx.WXK_CONTROL & wx.WXK_CONTROL_N:
            self.Create(self, e)
        elif keycode == wx.WXK_CONTROL & wx.WXK_CONTROL_O :
            self.Open(self, e)
        elif keycode == wx.WXK_CONTROL & wx.WXK_CONTROL_S :
            self.Save(self, e)
        elif keycode == wx.WXK_SHIFT & wx.WXK_CONTROL & wx.WXK_CONTROL_S :
            self.SaveAs(self, e)
        elif keycode == wx.WXK_CONTROL & wx.WXK_CONTROL_X:
            self.Cut(self, e)
        elif keycode == wx.WXK_CONTROL & wx.WXK_CONTROL_V:
            self.Paste(self, e)
        elif keycode == wx.WXK_F5:
            self.DateAndTime(self, e)

        e.Skip()


wnd = Window(None, nameApp)
app.MainLoop()


