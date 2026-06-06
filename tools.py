"""
Animation Tools - AI动画工具
支持动画生成、CSS动画、过渡效果
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AnimationTools:
    """
    AI动画工具
    支持：CSS动画、过渡效果、SVG动画
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_css_animation(self, description: str, duration: str = "1s") -> str:
        """生成CSS动画"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成CSS动画：

描述：{description}
时长：{duration}

要求：
1. 流畅自然
2. 包含关键帧
3. 可直接使用"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def generate_transition(self, element: str, properties: List[str]) -> str:
        """生成过渡效果"""
        if not self.client:
            return "LLM客户端未配置"

        properties_text = ", ".join(properties)

        prompt = f"""请为{element}生成CSS过渡效果：

属性：{properties_text}

要求：
1. 平滑过渡
2. 悬停触发
3. 可直接使用"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        return response.choices[0].message.content

    def generate_loading_animation(self, style: str = "spinner") -> str:
        """生成加载动画"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{style}风格的加载动画：

要求：
1. 纯CSS实现
2. 流畅循环
3. 可自定义颜色
4. 只返回HTML+CSS代码"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def generate_scroll_animation(self, effect: str) -> str:
        """生成滚动动画"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{effect}滚动动画：

要求：
1. 使用Intersection Observer
2. 平滑触发
3. 可配置
4. 包含JavaScript"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_svg_animation(self, description: str) -> str:
        """生成SVG动画"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成SVG动画：

描述：{description}

要求：
1. SMIL或CSS动画
2. 流畅循环
3. 可直接使用
4. 只返回SVG代码"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def suggest_animations(self, context: str) -> List[Dict]:
        """建议动画效果"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为以下场景建议动画效果：

场景：{context}

请返回JSON格式：
[
    {{"name": "动画名称", "description": "描述", "trigger": "触发方式", "css": "CSS代码"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"suggestion": content}]


def create_tools(**kwargs) -> AnimationTools:
    """创建动画工具"""
    return AnimationTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Animation Tools")
    print()

    # 测试
    animation = tools.generate_css_animation("元素从左侧滑入", "0.5s")
    print(animation)
