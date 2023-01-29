import platform
print("#"*30,"System Information","#"*30)
m=platform.uname()
print(f"system : {m.system}")
print(f"Node Name : {m.node}")
print(f"Release : {m.release}")
print(f"Version : {m.version}")
print(f"Machine : {m.machine}")
print(f"processor : {m.processor}")