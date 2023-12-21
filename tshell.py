def gns(n,d,name,f="jpg"):
    # 计算位数
    tx=""
    # 生成编号序列
    for i in range(1, n+1):
        # 使用字符串格式化确保位数不足时用0补全
        number = f"{i:08d}"
        
        tx=tx+f"![](../img/{d}/{number}.{f})\n"
    with open(f"{d}.md","w") as f:
            f.write(f"# {name}")
            f.write(tx)    
        
            
d=input("请输入这是第几本 即img/<数字> 的这个数字\n")
n=int(input("\n请输入有多少张图片 即最后一张图片的编号 例如最后一张图片编号是00000022 就输入22\n")) 
name=input("\n请输入本子名字 仅标用\n")
print(f"\n md文件生成成功 请在github的README.md末尾 加入\n- [{name}](./dir/{d}.md)")       
gns(n,d,name)        