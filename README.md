# potato-pythonocc
在 [pythonocc](https://github.com/tpaviot/pythonocc-core) 的基础上增加了一些喜欢的功能，实际更贴近一般 CAD 一些

## 安装
[conda主页](https://anaconda.org/ovo-tim/potato-pythonocc)
安装：
``` bash
conda install -c "ovo-tim/label/dev" potato-pythonocc
```
(全部由 [github action](https://github.com/ovo-Tim/potato-pythonocc/actions/workflows/conda-pack.yml) 自动打包上传, 目前 MacOS 上传时出现问题)

## 更改
### 增加对 PySide6 的支持
实测 PySide2 一堆 BUG, 
直接 `load_backend("qt-pyside6")` 即可食用

### zoom at cursor
实现在鼠标处缩放功能，而不是原版的定点缩放。
这个可以通过设定 `qtViewer3d.zoom_at_cursor = False` 关掉

### 无需切换即可选中 点线面
原版需按`G`切换选择模式，现在无需切换即可选择(自动帮你切换成需要的选择模式)

### 记录 Viewer3d 所有的 shape
记录了每次调用 `Viewer3d.DisplayShape()` 创建的所有图形。保存在 `Viewer3d.shapes` 里

### 重写了部分格式的导出函数，实现多个模型导出一个文件
使用: `导出函数(shapes 列表, 导出路径)`

已支持函数:
- step: `write_step_file`
- ~~STL: `write_stl_file`(暂时无法使用)~~
- iges: `write_iges_file`
- brep: `write_brep_file` (新增)

一个例子:
``` python
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeTorus, BRepPrimAPI_MakeBox

from OCC.Extend.DataExchange import write_step_file, write_iges_file, write_brep_file

# creates a basic shape
my_torus = BRepPrimAPI_MakeTorus(20.0, 10.0).Shape()
box = BRepPrimAPI_MakeBox(30.0, 30.0, 18.0).Shape()

write_step_file([my_torus, box], "./test.step")
write_iges_file([my_torus, box], "./test.iges")
write_brep_file([my_torus, box], "./test.brep")
```
