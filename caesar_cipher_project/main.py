# main.py

try:
    import gui
    from gui import CaesarCipherApp
    
    if __name__ == "__main__":
        print(" 启动凯撒密码工具...")
        app = CaesarCipherApp()
        app.run()
        
except ImportError as e:
    print(f"❌ 错误: 无法导入模块 - {e}")
    print("请检查 gui.py 和 cipher.py 是否存在")
    input("按回车键退出...")