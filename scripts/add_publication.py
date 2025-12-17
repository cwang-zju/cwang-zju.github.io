#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交互式脚本用于添加或编辑 publications TSV 文件
支持 books.tsv, conference.tsv, journel.tsv
"""

import csv
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

# ANSI 颜色代码
class Colors:
    """ANSI 颜色代码"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # 前景色
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # 亮色
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

def colorize(text: str, color: str) -> str:
    """为文本添加颜色"""
    if not sys.stdout.isatty():
        # 如果不是终端，不添加颜色
        return text
    return f"{color}{text}{Colors.RESET}"

def print_success(text: str):
    """打印成功信息（绿色）"""
    print(colorize(text, Colors.BRIGHT_GREEN))

def print_error(text: str):
    """打印错误信息（红色）"""
    print(colorize(text, Colors.BRIGHT_RED))

def print_warning(text: str):
    """打印警告信息（黄色）"""
    print(colorize(text, Colors.BRIGHT_YELLOW))

def print_info(text: str):
    """打印信息（蓝色）"""
    print(colorize(text, Colors.BRIGHT_BLUE))

def print_prompt(text: str):
    """打印提示信息（青色）"""
    print(colorize(text, Colors.BRIGHT_CYAN))

def print_header(text: str):
    """打印标题（加粗白色）"""
    print(colorize(text, Colors.BOLD + Colors.WHITE))

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
TSV_FILES = {
    '1': ('books', PROJECT_ROOT / '_pages' / 'books.tsv'),
    '2': ('conference', PROJECT_ROOT / '_pages' / 'conference.tsv'),
    '3': ('journal', PROJECT_ROOT / '_pages' / 'journel.tsv'),
}

# 验证规则
def validate_pub_date(pub_date: str, file_type: str) -> tuple[bool, str]:
    """验证发布日期格式"""
    if not pub_date.strip():
        return False, "发布日期不能为空"
    
    if file_type == 'conference':
        # 会议论文：两位数字（如 26, 25）
        if not pub_date.isdigit() or len(pub_date) != 2:
            return False, "会议论文的发布日期应为两位数字（如 26, 25）"
        year = int(pub_date)
        if year < 10 or year > 99:
            return False, "会议论文的发布日期应在 10-99 之间"
    elif file_type in ['journal', 'books']:
        # 期刊和书籍：四位数字（如 2025, 2024）
        if not pub_date.isdigit() or len(pub_date) != 4:
            return False, "期刊/书籍的发布日期应为四位数字（如 2025, 2024）"
        year = int(pub_date)
        if year < 1900 or year > 2100:
            return False, "期刊/书籍的发布日期应在 1900-2100 之间"
    
    return True, ""

def validate_url(url: str, url_type: str) -> tuple[bool, str]:
    """验证 URL 格式"""
    if not url.strip():
        return True, ""  # URL 可以为空
    
    # 如果是本地文件（如 pdf），检查是否是文件名格式
    if url_type == 'paper_url' and not url.startswith('http'):
        # 本地文件，只检查是否包含非法字符
        if '\t' in url or '\n' in url:
            return False, "文件名不能包含制表符或换行符"
        return True, ""
    
    # HTTP/HTTPS URL 验证
    if url.startswith('http://') or url.startswith('https://'):
        return True, ""
    
    # GitHub 链接可以是简写形式
    if url.startswith('github.com/') or url.startswith('www.github.com/'):
        return True, ""
    
    return False, f"URL 格式不正确，应以 http:// 或 https:// 开头，或为本地文件名"

def validate_required_field(value: str, field_name: str) -> tuple[bool, str]:
    """验证必填字段"""
    if not value.strip():
        return False, f"{field_name} 不能为空"
    if '\t' in value:
        return False, f"{field_name} 不能包含制表符"
    return True, ""

def validate_type(pub_type: str, file_type: str) -> tuple[bool, str]:
    """验证类型字段"""
    if not pub_type.strip():
        return False, "类型不能为空"
    
    expected_types = {
        'conference': ['conference'],
        'journal': ['Journal'],
        'books': ['book', 'Book']
    }
    
    if file_type in expected_types:
        if pub_type not in expected_types[file_type]:
            return False, f"类型应为：{', '.join(expected_types[file_type])}"
    
    return True, ""

def get_columns(file_path: Path) -> List[str]:
    """从文件第一行获取列名"""
    if not file_path.exists() or file_path.stat().st_size == 0:
        # 如果文件不存在，返回标准列名
        return [
            'pub_date', 'title', 'venue', 'type', 'full_venue', 'authors',
            'citation', 'paper_url', 'code_url', 'slides_url', 'video_url', 'hero_img'
        ]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
        return first_line.split('\t')

def read_tsv(file_path: Path) -> tuple[List[Dict[str, str]], List[str]]:
    """读取 TSV 文件，返回数据和列名"""
    columns = get_columns(file_path)
    
    if not file_path.exists() or file_path.stat().st_size == 0:
        return [], columns
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        # 确保列名匹配
        if reader.fieldnames != columns:
            columns = list(reader.fieldnames) if reader.fieldnames else columns
        return list(reader), columns

def write_tsv(file_path: Path, data: List[Dict[str, str]], columns: List[str]):
    """写入 TSV 文件"""
    # 确保目录存在
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter='\t', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)

def get_input(prompt: str, default: str = '', required: bool = True, validator=None) -> str:
    """获取用户输入并进行验证"""
    while True:
        if default:
            full_prompt = colorize(f"{prompt} [{default}]: ", Colors.BRIGHT_CYAN)
        else:
            if required:
                full_prompt = colorize(f"{prompt}: ", Colors.BRIGHT_CYAN)
            else:
                full_prompt = colorize(f"{prompt} (可选): ", Colors.BRIGHT_BLACK)
        
        value = input(full_prompt).strip()
        
        if not value:
            if default:
                value = default
            elif not required:
                return ""
            else:
                print_warning("  此字段为必填项，请重新输入")
                continue
        
        if validator:
            is_valid, error_msg = validator(value)
            if not is_valid:
                print_error(f"  ❌ {error_msg}")
                continue
        
        return value

def get_pub_date_validator(file_type: str):
    """获取发布日期验证器"""
    return lambda x: validate_pub_date(x, file_type)

def get_url_validator(url_type: str):
    """获取 URL 验证器"""
    return lambda x: validate_url(x, url_type)

def collect_publication_info(file_type: str) -> Dict[str, str]:
    """收集出版物信息"""
    print("\n" + colorize("="*60, Colors.BRIGHT_CYAN))
    print_header(f"添加新的 {file_type.upper()} 条目")
    print(colorize("="*60, Colors.BRIGHT_CYAN))
    
    pub = {}
    
    # pub_date
    if file_type == 'conference':
        pub_date_validator = get_pub_date_validator('conference')
        pub['pub_date'] = get_input(
            "发布日期 (两位数字，如 26)",
            required=True,
            validator=pub_date_validator
        )
    else:
        pub_date_validator = get_pub_date_validator(file_type)
        pub['pub_date'] = get_input(
            "发布日期 (四位数字，如 2025)",
            required=True,
            validator=pub_date_validator
        )
    
    # title
    pub['title'] = get_input(
        "标题",
        required=True,
        validator=lambda x: validate_required_field(x, "标题")
    )
    
    # venue
    pub['venue'] = get_input(
        "会议/期刊简称 (如 AAAI, CVPR, TMC)",
        required=True,
        validator=lambda x: validate_required_field(x, "会议/期刊简称")
    )
    
    # type - 根据文件类型自动设置
    if file_type == 'conference':
        pub['type'] = 'conference'
    elif file_type == 'journal':
        pub['type'] = 'Journal'
    elif file_type == 'books':
        pub['type'] = 'book'
    else:
        pub['type'] = 'book'  # 默认值
    
    print_info(f"✓ 类型已自动设置为：{pub['type']}")
    
    # full_venue
    pub['full_venue'] = get_input(
        "完整会议/期刊名称",
        required=True,
        validator=lambda x: validate_required_field(x, "完整会议/期刊名称")
    )
    
    # authors
    pub['authors'] = get_input(
        "作者列表 (用英文逗号分隔，如：Author1, Author2, Cong Wang*)",
        required=True,
        validator=lambda x: validate_required_field(x, "作者列表")
    )
    
    # citation
    pub['citation'] = get_input("引用信息 (可选项，URL 形式)", required=False)
    
    # paper_url
    paper_url_validator = get_url_validator('paper_url')
    pub['paper_url'] = get_input(
        "论文链接 (可选项，URL 或本地文件名，如 cvpr25.pdf)",
        required=False,
        validator=paper_url_validator
    )
    
    # code_url
    code_url_validator = get_url_validator('code_url')
    pub['code_url'] = get_input(
        "代码链接 (可选项，GitHub URL)",
        required=False,
        validator=code_url_validator
    )
    
    # slides_url
    slides_url_validator = get_url_validator('slides_url')
    pub['slides_url'] = get_input(
        "幻灯片链接 (可选项，URL 或本地文件名)",
        required=False,
        validator=slides_url_validator
    )
    
    # video_url
    video_url_validator = get_url_validator('video_url')
    pub['video_url'] = get_input(
        "视频链接",
        required=False,
        validator=video_url_validator
    )
    
    # hero_img
    pub['hero_img'] = get_input("封面图片", required=False)
    
    return pub

def show_summary(pub: Dict[str, str]):
    """显示输入摘要"""
    print("\n" + colorize("="*60, Colors.BRIGHT_CYAN))
    print_header("输入摘要：")
    print(colorize("="*60, Colors.BRIGHT_CYAN))
    for key, value in pub.items():
        if value:
            print(f"  {colorize(key, Colors.BRIGHT_BLUE):15}: {value}")
    print(colorize("="*60, Colors.BRIGHT_CYAN))

def main():
    """主函数"""
    print("\n" + "="*60)
    print("Publications 管理工具")
    print("="*60)
    print("\n请选择要添加的 publication 类型：")
    print("  1. books")
    print("  2. conference")
    print("  3. journal")
    print("  0. 退出")
    
    choice = input("\n请输入选项 (0-3): ").strip()
    
    if choice == '0':
        print("退出程序")
        sys.exit(0)
    
    if choice not in TSV_FILES:
        print("❌ 无效的选项")
        sys.exit(1)
    
    file_name, file_path = TSV_FILES[choice]
    
    # 读取现有数据和列名
    existing_data, columns = read_tsv(file_path)
    print(f"\n当前 {file_name}.tsv 中有 {len(existing_data)} 条记录")
    
    # 收集新条目信息
    new_pub = collect_publication_info(file_name)
    
    # 确保新条目包含所有列（缺失的列设为空字符串）
    for col in columns:
        if col not in new_pub:
            new_pub[col] = ''
    
    # 显示摘要
    show_summary(new_pub)
    
    # 确认
    confirm = input(colorize("\n确认添加此条目？(y/n): ", Colors.BRIGHT_YELLOW)).strip().lower()
    if confirm != 'y':
        print_warning("已取消")
        sys.exit(0)
    
    # 添加到数据列表
    existing_data.append(new_pub)
    
    # 按日期排序（最新的在前）
    try:
        existing_data.sort(key=lambda x: int(x['pub_date']), reverse=True)
    except (ValueError, KeyError):
        # 如果排序失败，保持原顺序
        pass
    
    # 写入文件
    try:
        write_tsv(file_path, existing_data, columns)
        print_success(f"\n✅ 成功添加条目到 {file_path}")
        print_info(f"   文件现在包含 {len(existing_data)} 条记录")
    except Exception as e:
        print_error(f"\n❌ 写入文件时出错：{e}")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print_warning("\n\n程序被用户中断")
        sys.exit(0)

