# potato-pythonocc
在 [pythonocc](https://github.com/tpaviot/pythonocc-core) 的基础上增加了一些喜欢的功能，实际更贴近一般 CAD 一些

<!-- TOC -->

- [potato-pythonocc](#potato-pythonocc)
    - [安装](#%E5%AE%89%E8%A3%85)
    - [更改](#%E6%9B%B4%E6%94%B9)
        - [增加对 PySide6 的支持](#%E5%A2%9E%E5%8A%A0%E5%AF%B9-pyside6-%E7%9A%84%E6%94%AF%E6%8C%81)
        - [zoom at cursor](#zoom-at-cursor)
        - [无需切换即可选中 点线面](#%E6%97%A0%E9%9C%80%E5%88%87%E6%8D%A2%E5%8D%B3%E5%8F%AF%E9%80%89%E4%B8%AD-%E7%82%B9%E7%BA%BF%E9%9D%A2)
        - [记录 Viewer3d 所有的 shape](#%E8%AE%B0%E5%BD%95-viewer3d-%E6%89%80%E6%9C%89%E7%9A%84-shape)
        - [重写了部分格式的导出函数，实现多个模型导出一个文件](#%E9%87%8D%E5%86%99%E4%BA%86%E9%83%A8%E5%88%86%E6%A0%BC%E5%BC%8F%E7%9A%84%E5%AF%BC%E5%87%BA%E5%87%BD%E6%95%B0%E5%AE%9E%E7%8E%B0%E5%A4%9A%E4%B8%AA%E6%A8%A1%E5%9E%8B%E5%AF%BC%E5%87%BA%E4%B8%80%E4%B8%AA%E6%96%87%E4%BB%B6)
        - [重写高亮主题](#%E9%87%8D%E5%86%99%E9%AB%98%E4%BA%AE%E4%B8%BB%E9%A2%98)
        - [增加 potaoViewer](#%E5%A2%9E%E5%8A%A0-potaoviewer)
            - [move_to_mouse](#move_to_mouse)
        - [增加新的坐标转换函数](#%E5%A2%9E%E5%8A%A0%E6%96%B0%E7%9A%84%E5%9D%90%E6%A0%87%E8%BD%AC%E6%8D%A2%E5%87%BD%E6%95%B0)
        - [增加网格捕捉功能](#%E5%A2%9E%E5%8A%A0%E7%BD%91%E6%A0%BC%E6%8D%95%E6%8D%89%E5%8A%9F%E8%83%BD)

<!-- /TOC -->

## 安装
[conda主页](https://anaconda.org/ovo-tim/potato-pythonocc)
安装：
``` bash
conda install -c "ovo-tim/label/dev" potato-pythonocc
```
(全部由 [github action](https://github.com/ovo-Tim/potato-pythonocc/actions/workflows/conda-pack.yml) 自动打包上传, 目前 MacOS 上传时出现问题)

## 更改

### 使用 qtpy 加载 QT 增加对 PySide6 的支持
实测 PySide2 一堆 BUG,

~~直接 `load_backend("qt-pyside6")` 即可食用~~

设置 `QT_API` 环境变量即可，例：`os.environ['QT_API'] = 'pyside6'`

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

### 重写高亮主题
现在支持直接高亮一个面
以前(只能高亮描边，不好看):
![](image/high%20light%20old.png)
现在：
可直接高亮面，且支持半透明:
![](image/high%20light1.png)
![](image/high%20light2.png)

自定义:
```python
qtViewer3d.set_highlight(self, 
                        select_color = Quantity_Color(颜色),
                        select_DisplayMode = 1, # 显示模式，建议为1
                        select_transparency = 0.5, # 透明度
                        dynamic_color = Quantity_Color(颜色),
                        dynamic_DisplayMode = 1,
                        dynamic_transparency = 0.35
                      )
```

### 增加 potaoViewer
在 `qtViewer3d` 的基础上增加了更多功能
- 增加 `ViewCube`
#### move_to_mouse
只需要调用 `potaoViewer.move_to_mouse` 并传入要移动的 `AIS_Shape` 就可以实时将图形移动到鼠标位置

### 增加新的坐标转换函数
使用：`qtViewer3d.ConvertPos(X, Y)`

相比于 `display.View.Convert`， `ConvertPos` 会将鼠标限制与某一个面上
### 增加网格捕捉功能
设置 `qtViewer3d.grid_snap` 即可设置捕捉距离，设0禁用