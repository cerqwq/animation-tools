# ✨ Animation Tools

AI动画工具，支持动画生成、CSS动画、过渡效果。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🎬 CSS动画生成
- 🔄 过渡效果生成
- ⏳ 加载动画生成
- 📜 滚动动画生成
- 🎨 SVG动画生成
- 💡 动画建议

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from animation_tools import create_tools

tools = create_tools()

# CSS动画
animation = tools.generate_css_animation("元素从左侧滑入", "0.5s")

# 过渡效果
transition = tools.generate_transition("按钮", ["transform", "opacity"])

# 加载动画
loading = tools.generate_loading_animation("spinner")

# 滚动动画
scroll = tools.generate_scroll_animation("淡入")

# SVG动画
svg = tools.generate_svg_animation("圆形进度条")

# 建议动画
suggestions = tools.suggest_animations("产品展示页面")
```

## 📁 项目结构

```
animation-tools/
├── tools.py       # 动画工具核心
└── README.md
```

## 📄 许可证

MIT License
