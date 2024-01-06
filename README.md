# potato-pythonocc
在 [pythonocc](https://github.com/tpaviot/pythonocc-core) 的基础上增加了一些喜欢的功能，实际更贴近一般 CAD 一些

<!-- vscode-markdown-toc -->
* 1. [安装](#)
* 2. [更改](#-1)
	* 2.1. [使用 qtpy 加载 QT 增加对 PySide6 的支持](#qtpyQTPySide6)
	* 2.2. [zoom at cursor](#zoomatcursor)
	* 2.3. [无需切换即可选中 点线面](#-1)
	* 2.4. [重写了部分格式的导出函数，实现多个模型导出一个文件](#-1)
	* 2.5. [重写高亮主题](#-1)
	* 2.6. [增加新的坐标转换函数](#-1)
	* 2.7. [增加网格捕捉功能](#-1)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name=''></a>安装
[conda主页](https://anaconda.org/ovo-tim/potato-pythonocc)
安装：
``` bash
conda install -c "ovo-tim/label/dev" potato-pythonocc
```
(全部由 [github action](https://github.com/ovo-Tim/potato-pythonocc/actions/workflows/conda-pack.yml) 自动打包上传, 目前 MacOS 上传时出现问题)

##  2. <a name='-1'></a>更改

###  2.1. <a name='qtpyQTPySide6'></a>使用 qtpy 加载 QT 增加对 PySide6 的支持
实测 PySide2 一堆 BUG,

~~直接 `load_backend("qt-pyside6")` 即可食用~~

设置 `QT_API` 环境变量即可，例：`os.environ['QT_API'] = 'pyside6'`

(`qtpy` 可能打破了 `SimpleGui` 原本的结构，不建议使用，有逝可以提 issus)

###  2.2. <a name='zoomatcursor'></a>zoom at cursor
实现在鼠标处缩放功能，而不是原版的定点缩放。
这个可以通过设定 `qtViewer3d.zoom_at_cursor = False` 关掉

###  2.3. <a name='-1'></a>无需切换即可选中 点线面
原版需按`G`切换选择模式，现在无需切换即可选择(自动帮你切换成需要的选择模式)

###  2.4. <a name='-1'></a>重写了部分格式的导出函数，实现多个模型导出一个文件
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

###  2.5. <a name='-1'></a>重写高亮主题
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

###  2.6. <a name='-1'></a>增加新的坐标转换函数
使用：`qtViewer3d.ConvertPos(X, Y)`

相比于 `display.View.Convert`， `ConvertPos` 会将鼠标限制与某一个面上
###  2.7. <a name='-1'></a>增加网格捕捉功能
设置 `qtViewer3d.grid_snap` 即可设置捕捉距离，设0禁用
