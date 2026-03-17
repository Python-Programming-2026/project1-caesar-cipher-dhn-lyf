import customtkinter as ctk
import tkinter as tk
import cipher
from tkinter import messagebox
from cipher import caesar_cipher
from crack import CaesarCracker

# 设置外观模式和颜色主题
ctk.set_appearance_mode("System")  # 可选: "System" (跟随系统), "Dark", "Light"
ctk.set_default_color_theme("blue")  # 可选: "blue", "green", "dark-blue"

class CaesarCipherApp:
    def __init__(self):
        # 创建主窗口
        self.window = ctk.CTk()
        self.window.title("凯撒密码工具 v1.0")
        self.window.geometry("700x500")  # 宽度x高度
        
        # 设置窗口图标（可选）
        # self.window.iconbitmap("icon.ico")
        
        # 构建界面
        self.create_widgets()
        
    def create_widgets(self):
        """创建所有界面组件"""
        
        # 1. 标题标签
        title_label = ctk.CTkLabel(
            self.window, 
            text="🔐 凯撒密码加解密器",
            font=("Arial", 24, "bold")
        )
        title_label.pack(pady=20)  # pady是上下边距
        
        # 2. 输入框架
        input_frame = ctk.CTkFrame(self.window)
        input_frame.pack(padx=20, pady=10, fill="x")
        
        # 输入标签
        input_label = ctk.CTkLabel(
            input_frame, 
            text="输入文本:",
            font=("Arial", 14)
        )
        input_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        # 输入文本框（带滚动条）
        self.input_text = ctk.CTkTextbox(
            input_frame,
            height=120,
            font=("Consolas", 12) 
        )
        self.input_text.pack(padx=10, pady=(0, 10), fill="x")
        
        # 3. 控制框架
        control_frame = ctk.CTkFrame(self.window)
        control_frame.pack(padx=20, pady=10, fill="x")
        
        # 第一行：移位值控制
        shift_label = ctk.CTkLabel(
            control_frame, 
            text="移位值 (0-25):",
            font=("Arial", 12)
        )
        shift_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # 滑动条
        self.shift_var = tk.IntVar(value=3)
        self.shift_slider = ctk.CTkSlider(
            control_frame,
            from_=0,
            to=25,
            number_of_steps=25,  # 25个整数步长
            variable=self.shift_var,
            width=200
        )
        self.shift_slider.grid(row=0, column=1, padx=10, pady=10)
        
        # 数字显示
        self.shift_label = ctk.CTkLabel(
            control_frame,
            textvariable=self.shift_var,
            width=30,
            font=("Arial", 12, "bold")
        )
        self.shift_label.grid(row=0, column=2, padx=(0, 10))
        
        # 4. 按钮框架
        button_frame = ctk.CTkFrame(self.window)
        button_frame.pack(pady=20)
        
        # 按钮
        btn_style = {
            "width": 100,
            "height": 40,
            "font": ("Arial", 12, "bold")
        }
        
        self.encrypt_btn = ctk.CTkButton(
            button_frame,
            text="加密",
            command=self.encrypt_text,
            fg_color="#4CAF50",  # 绿色
            hover_color="#45a049",
            **btn_style
        )
        self.encrypt_btn.pack(side="left", padx=10)
        
        self.decrypt_btn = ctk.CTkButton(
            button_frame,
            text=" 解密", 
            command=self.decrypt_text,
            fg_color="#2196F3",  # 蓝色
            hover_color="#1976D2",
            **btn_style
        )
        self.decrypt_btn.pack(side="left", padx=10)
        
        self.ai_crack_btn = ctk.CTkButton(
            button_frame,
            text=" 破解",
            command=self.ai_crack_text,
            fg_color="#FF9800",  # 橙色
            hover_color="#F57C00",
            **btn_style
        )
        self.ai_crack_btn.pack(side="left", padx=10)
        
        self.clear_btn = ctk.CTkButton(
            button_frame,
            text="🗑️ 清空",
            command=self.clear_text,
            fg_color="#F44336",  # 红色
            hover_color="#D32F2F",
            **btn_style
        )
        self.clear_btn.pack(side="left", padx=10)
        
        # 5. 输出框架
        output_frame = ctk.CTkFrame(self.window)
        output_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        output_label = ctk.CTkLabel(
            output_frame,
            text="输出结果:",
            font=("Arial", 14)
        )
        output_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        # 输出文本框
        self.output_text = ctk.CTkTextbox(
            output_frame,
            height=150,
            font=("Consolas", 12)
        )
        self.output_text.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        
        # 6. 状态栏
        self.status_label = ctk.CTkLabel(
            self.window,
            text="就绪",
            font=("Arial", 10)
        )
        self.status_label.pack(pady=5)
        
    def encrypt_text(self):
        """加密按钮回调函数"""
        try:
            text = self.input_text.get("1.0", "end-1c").strip()
            if not text:
                messagebox.showwarning("警告", "请输入要加密的文本！")
                return
                
            shift = self.shift_var.get()
            result = cipher.caesar_cipher(text, shift, mode='encrypt')
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.status_label.configure(text=f"✓ 加密完成 (shift={shift})")
            
        except Exception as e:
            messagebox.showerror("错误", f"加密失败: {str(e)}")
    
    def decrypt_text(self):
        """解密按钮回调函数"""
        try:
            text = self.input_text.get("1.0", "end-1c").strip()
            if not text:
                messagebox.showwarning("警告", "请输入要解密的文本！")
                return
                
            shift = self.shift_var.get()
            result = cipher.caesar_cipher(text, shift, mode='decrypt')
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.status_label.configure(text=f"✓ 解密完成 (shift={shift})")
            
        except Exception as e:
            messagebox.showerror("错误", f"解密失败: {str(e)}")
    
    def ai_crack_text(self):
        """破解按钮回调函数"""
        try:
            text = self.input_text.get("1.0", "end-1c").strip()
            if not text:
                messagebox.showwarning("警告", "请输入要破解的密文！")
                return
                
            cracker = CaesarCracker()
            
            results = cracker.crack(text, top_n=3)
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "🤖 AI破解结果:\n\n")
            
            for i, (score, shift, plaintext) in enumerate(results):
                self.output_text.insert("end", 
                    f"{i+1}. shift={shift} (置信度: {score:.1%})\n")
                self.output_text.insert("end", f"   {plaintext}\n\n")
                
            self.status_label.configure(text="✓ AI破解完成")
            
        except Exception as e:
            messagebox.showerror("错误", f"AI破解失败: {str(e)}")
    
    def clear_text(self):
        """清空所有文本"""
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.status_label.configure(text="已清空")
    
    def run(self):
        """运行应用程序"""
        self.window.mainloop()

# 主题切换功能（扩展功能）
def toggle_theme():
    """切换深色/浅色模式"""
    current = ctk.get_appearance_mode()
    if current == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

if __name__ == "__main__":
    # 创建并运行应用
    app = CaesarCipherApp()
    
    # 添加主题切换按钮（可选）
    theme_btn = ctk.CTkButton(
        app.window,
        text="🌓 切换主题",
        command=toggle_theme,
        width=80,
        height=30,
        font=("Arial", 10)
    )
    theme_btn.place(x=10, y=10)  # 放在左上角
    
    app.run()