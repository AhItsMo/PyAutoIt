import clr
import os
import autoit


class Repo:
    # Out of date
    def old_install_msi(self):
        current_path = os.getcwd()
        print current_path
        clr.AddReference(current_path + "\DLLs\TestStack.White.dll")
        from TestStack.White import InputDevices
        from TestStack.White import UIItems
        from TestStack.White import WindowsAPI

    # Jenkins automated installation
    def install_jenkins(self):
        autoit.auto_it_set_option("MouseClickDelay", 1000)
        autoit.run("msiexec /package D:\Automation\Projects\WhiteRide\Repo\jenkins.msi")
        autoit.win_wait_active("Jenkins 1.651.2 Setup", 30)
        autoit.control_click_wait("Jenkins 1.651.2 Setup", "[ID:995]", 10)
        autoit.control_click_wait("Jenkins 1.651.2 Setup", "[ID:1100]", 10)
        autoit.control_click_wait("Jenkins 1.651.2 Setup", "[ID:1071]", 60)
        autoit.control_click_wait("Jenkins 1.651.2 Setup", "[ID:968]", 20)
        autoit.control_click_wait("Jenkins 1.651.2 Setup", "[ID:971]", 120)
        # autoit.run("C:\\Users\\mabdelmonem\\Downloads\\jenkins-1.651.2\\jenkins.msi")
        # autoit.win_wait_active("[VALUE:Run]", 3)
        # autoit.control_send("[VALUE:Run]", "Open", "C:\Users\mabdelmonem\Downloads\jenkins-1.651.2\jenkins.msi")
        # autoit.run("C:\Users\mabdelmonem\Downloads\jenkins-1.651.2\jenkins.msi")
        # autoit.control_send_by_handle("Start", "Start", "{LWINDOWN}r{LWINUP}")
        # autoit.run("explorer.exe")
        # autoit.win_wait_active("[VALUE:Libraries]", 5)
        # autoit.control_send("[CLASS:#32769]", "[CLASS:Shell_TrayWnd]", "{LWINDOWN}r{LWINUP}")
        # autoit.run("msiexec /package D:\Automation\Projects\WhiteRide\Repo\jenkins.msi")
        # jenkins_window = autoit.win_wait("Jenkins 1.651.2 Setup", 3, "")
        # window_handle = autoit.win_get_handle_as_text("Jenkins 1.651.2 Setup")
        # next_handle = autoit.control_get_handle_as_text("Jenkins 1.651.2 Setup", "[ID:995]")
        # print next_handle
        # print window_handle
        # autoit.control_click_by_handle(window_handle, next_handle)
        # print autoit.control_get_handle("0x0000000000020E64", "Next")
        # autoit.control_send("[VALUE:Run]", "Open", "C:\Users\mabdelmonem\Downloads\jenkins-1.651.2\jenkins.msi")
        # autoit.control_click("[VALUE:Run]", "OK")
        # autoit.win_wait_active("[VALUE:Open File - Security Warning]", 3)
        # autoit.control_click("[VALUE:Open File - Security Warning]", "Run")
        # autoit.run("notepad.exe")
        # autoit.win_wait_active("[CLASS:Notepad]", 3)
        # autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
        # autoit.win_close("[CLASS:Notepad]")
        # autoit.control_click("[Class:#32770]", "Button2")
        # autoit.win_wait_active("Jenkins 1.651.2 Setup", 5)

    # ASTA automated installation - WIP/Incomplete
    def install_ast(self):
        autoit.auto_it_set_option("MouseClickDelay", 1000)
        autoit.run("D:\Automation\Projects\WhiteRide\Repo\setup.exe")

        window_name = "CareFusion - Alaris System Tracking Application Configuration v3.0"
        # autoit.win_wait_active(window_name, 30)
        autoit.control_wait_visible(window_name, "[ID:2495]", "IsVisible")
        autoit.control_click_wait(window_name, "[ID:2495]", 20)     # Welcome screen - Next

        # window_name = "CareFusion - Alaris System Tracking Application Configuration v3.0 - InstallShield Wizard"
        # autoit.win_wait_active(window_name, 30)
        # autoit.control_click_wait(window_name, "[ID:2125]", 10)     # Data Base Inst. Mode - New Instance RadioButton
        # autoit.control_click(window_name, "[ID:2495]")              # Data Base Inst. Mode - Next
        #
        # window_name = "CareFusion - Alaris System Tracking Application Configuration v3.0"
        # autoit.win_wait_active(window_name, 30)
        # autoit.control_click_wait(window_name, "[ID:2495]", 20)     # Data Base Initialization - Next
        # autoit.control_click_wait(window_name, "[ID:2524]", 120)    # Ready to Install - Install




    # def click_add_task_button(self):
    #     global mainWindow = app.GetWindow("Wpf Todo")
    #     button = mainWindow.Get[Button]("AddTaskButton")
    #     button.Click()

    # Not Working
    # def install_jenkins(self):
    #     current_path = os.getcwd()
    #     clr.AddReference(current_path + "\DLLs\CodedUITestProject2.dll")
    #     clr.AddReference(current_path + "\DLLs\TestStack.White.dll")
    #     from TestStack.White import Application
    #     from TestStack.White.UIItems import Button
    #     appPath = "D:\\Automation\\Projects\\TestStack.White\\
        # White\\src\\Samples\\Wpf\\WpfTodo\\bin\\Debug\\WpfTodo.exe"
    #     app = Application.Launch(appPath)
    #     mainWindow = app.GetWindow("Wpf Todo")
    #     button = mainWindow.Get[Button]("AddTaskButton")
    #     button.Click()
        # from CodedUITestProject12 import CodedUITestProject2
        # CodedUITestProject2.CodedUITest1.CodedUITestMethod1()
