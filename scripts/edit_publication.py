#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交互式脚本用于添加或编辑 publications TSV 文件
支持 books.tsv, conference.tsv, journel.tsv
"""

import csv
import curses
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
        return text
    return f"{color}{text}{Colors.RESET}"

def print_success(text: str):
    print(colorize(text, Colors.BRIGHT_GREEN))

def print_error(text: str):
    print(colorize(text, Colors.BRIGHT_RED))

def print_warning(text: str):
    print(colorize(text, Colors.BRIGHT_YELLOW))

def print_info(text: str):
    print(colorize(text, Colors.BRIGHT_BLUE))

def print_header(text: str):
    print(colorize(text, Colors.BOLD + Colors.WHITE))

PROJECT_ROOT = Path(__file__).parent.parent
TSV_FILES = {
    '1': ('books', PROJECT_ROOT / '_pages' / 'books.tsv'),
    '2': ('conference', PROJECT_ROOT / '_pages' / 'conference.tsv'),
    '3': ('journal', PROJECT_ROOT / '_pages' / 'journel.tsv'),
}

# 验证规则
def validate_pub_date(pub_date: str, file_type: str) -> tuple[bool, str]:
    if not pub_date.strip():
        return False, "发布日期不能为空"
    
    if file_type == 'conference':
        if not pub_date.isdigit() or len(pub_date) != 2:
            return False, "会议论文的发布日期应为两位数字（如 26, 25）"
        year = int(pub_date)
        if year < 10 or year > 99:
            return False, "会议论文的发布日期应在 10-99 之间"
    elif file_type in ['journal', 'books']:
        if not pub_date.isdigit() or len(pub_date) != 4:
            return False, "期刊/书籍的发布日期应为四位数字（如 2025, 2024）"
        year = int(pub_date)
        if year < 1900 or year > 2100:
            return False, "期刊/书籍的发布日期应在 1900-2100 之间"
    
    return True, ""

def validate_url(url: str, url_type: str) -> tuple[bool, str]:
    if not url.strip():
        return True, ""
    if url_type == 'paper_url' and not url.startswith('http'):
        if '\t' in url or '\n' in url:
            return False, "文件名不能包含制表符或换行符"
        return True, ""
    if url.startswith('http://') or url.startswith('https://'):
        return True, ""
    if url.startswith('github.com/') or url.startswith('www.github.com/'):
        return True, ""
    return False, "URL 格式不正确，应以 http:// 或 https:// 开头，或为本地文件名"

def validate_required_field(value: str, field_name: str) -> tuple[bool, str]:
    if not value.strip():
        return False, f"{field_name} 不能为空"
    if '\t' in value:
        return False, f"{field_name} 不能包含制表符"
    return True, ""

def get_columns(file_path: Path) -> List[str]:
    if not file_path.exists() or file_path.stat().st_size == 0:
        return [
            'pub_date', 'title', 'venue', 'type', 'full_venue', 'authors',
            'citation', 'paper_url', 'code_url', 'slides_url', 'video_url', 'hero_img'
        ]
    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
        return first_line.split('\t')

def read_tsv(file_path: Path) -> tuple[List[Dict[str, str]], List[str]]:
    columns = get_columns(file_path)
    if not file_path.exists() or file_path.stat().st_size == 0:
        return [], columns
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        if reader.fieldnames != columns:
            columns = list(reader.fieldnames) if reader.fieldnames else columns
        return list(reader), columns

def write_tsv(file_path: Path, data: List[Dict[str, str]], columns: List[str]):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter='\t', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)

def get_input(prompt: str, default: str = '', required: bool = True, validator=None) -> str:
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
                return ''
            else:
                print_warning("  此字段为必填项，请重新输入")
                continue
        if validator:
            is_valid, error_msg = validator(value)
            if not is_valid:
                print_error(f"  ❌ {error_msg}")
                continue
        return value

def ensure_columns(data: Dict[str, str], columns: List[str], fallback: Optional[Dict[str, str]] = None):
    for col in columns:
        if col not in data:
            if fallback:
                data[col] = fallback.get(col, '')
            else:
                data[col] = ''

def collect_publication_info(file_type: str, existing: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    mode = "编辑" if existing else "添加"
    print("\n" + colorize("="*60, Colors.BRIGHT_CYAN))
    print_header(f"{mode} {file_type.upper()} 条目")
    print(colorize("="*60, Colors.BRIGHT_CYAN))
    pub: Dict[str, str] = {} if existing is None else dict(existing)

    if file_type == 'conference':
        validator = lambda x: validate_pub_date(x, 'conference')
        default = pub.get('pub_date', '')
        pub['pub_date'] = get_input("发布日期 (两位数字，如 26)", default=default, required=True, validator=validator)
    else:
        validator = lambda x: validate_pub_date(x, file_type)
        default = pub.get('pub_date', '')
        pub['pub_date'] = get_input("发布日期 (四位数字，如 2025)", default=default, required=True, validator=validator)

    pub['title'] = get_input(
        "标题",
        default=pub.get('title', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "标题")
    )

    pub['venue'] = get_input(
        "会议/期刊简称 (如 AAAI, CVPR, TMC)",
        default=pub.get('venue', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "会议/期刊简称")
    )

    auto_types = {
        'conference': 'conference',
        'journal': 'Journal',
        'books': 'book'
    }
    default_type = pub.get('type') or auto_types.get(file_type, 'book')
    pub['type'] = default_type
    print_info(f"✓ 类型已设置为：{pub['type']}")

    pub['full_venue'] = get_input(
        "完整会议/期刊名称",
        default=pub.get('full_venue', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "完整会议/期刊名称")
    )

    pub['authors'] = get_input(
        "作者列表 (用英文逗号分隔，如：Author1, Author2, Cong Wang*)",
        default=pub.get('authors', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "作者列表")
    )

    pub['citation'] = get_input("引用信息 (可选项，URL 形式)", default=pub.get('citation', ''), required=False)
    paper_url_validator = lambda x: validate_url(x, 'paper_url')
    pub['paper_url'] = get_input(
        "论文链接 (可选项，URL 或本地文件名，如 cvpr25.pdf)",
        default=pub.get('paper_url', ''),
        required=False,
        validator=paper_url_validator
    )

    code_url_validator = lambda x: validate_url(x, 'code_url')
    pub['code_url'] = get_input(
        "代码链接 (可选项，GitHub URL)",
        default=pub.get('code_url', ''),
        required=False,
        validator=code_url_validator
    )

    slides_url_validator = lambda x: validate_url(x, 'slides_url')
    pub['slides_url'] = get_input(
        "幻灯片链接 (可选项，URL 或本地文件名)",
        default=pub.get('slides_url', ''),
        required=False,
        validator=slides_url_validator
    )

    video_url_validator = lambda x: validate_url(x, 'video_url')
    pub['video_url'] = get_input(
        "视频链接",
        default=pub.get('video_url', ''),
        required=False,
        validator=video_url_validator
    )

    pub['hero_img'] = get_input("封面图片", default=pub.get('hero_img', ''), required=False)
    return pub

def get_edit_input(prompt: str, old_value: str, required: bool = True, validator=None) -> str:
    while True:
        shown_old_value = old_value if old_value else 'Null'
        print(colorize(f"{prompt}: {shown_old_value}", Colors.BRIGHT_BLACK))
        value = input(colorize("新值 (回车保持不变): ", Colors.BRIGHT_CYAN)).strip()
        if not value:
            if old_value:
                return old_value
            if not required:
                return ''
            print_warning("  此字段为必填项，请输入新值")
            continue
        if '\t' in value:
            print_error("  ❌ 输入不能包含制表符")
            continue
        if validator:
            is_valid, error_msg = validator(value)
            if not is_valid:
                print_error(f"  ❌ {error_msg}")
                continue
        return value

def collect_publication_edits(file_type: str, existing: Dict[str, str]) -> Dict[str, str]:
    print("\n" + colorize("="*60, Colors.BRIGHT_CYAN))
    print_header(f"编辑 {file_type.upper()} 条目")
    print(colorize("="*60, Colors.BRIGHT_CYAN))
    pub: Dict[str, str] = dict(existing)

    if file_type == 'conference':
        validator = lambda x: validate_pub_date(x, 'conference')
        pub['pub_date'] = get_edit_input("发布日期 (两位数字)，原", pub.get('pub_date', ''), required=True, validator=validator)
    else:
        validator = lambda x: validate_pub_date(x, file_type)
        pub['pub_date'] = get_edit_input("发布日期 (四位数字)，原", pub.get('pub_date', ''), required=True, validator=validator)

    pub['title'] = get_edit_input(
        "标题",
        pub.get('title', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "标题")
    )

    pub['venue'] = get_edit_input(
        "会议/期刊简称，原",
        pub.get('venue', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "会议/期刊简称")
    )

    auto_types = {
        'conference': 'conference',
        'journal': 'Journal',
        'books': 'book'
    }
    default_type = pub.get('type') or auto_types.get(file_type, 'book')
    pub['type'] = default_type
    print_info(f"✓ 类型已设置为：{pub['type']}")

    pub['full_venue'] = get_edit_input(
        "完整会议/期刊名称，原",
        pub.get('full_venue', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "完整会议/期刊名称")
    )

    pub['authors'] = get_edit_input(
        "作者列表，原",
        pub.get('authors', ''),
        required=True,
        validator=lambda x: validate_required_field(x, "作者列表")
    )

    pub['citation'] = get_edit_input("引用信息 (可选项，URL 形式)", pub.get('citation', ''), required=False)

    paper_url_validator = lambda x: validate_url(x, 'paper_url')
    pub['paper_url'] = get_edit_input(
        "论文链接 (可选项，URL 或本地文件名)，原",
        pub.get('paper_url', ''),
        required=False,
        validator=paper_url_validator
    )

    code_url_validator = lambda x: validate_url(x, 'code_url')
    pub['code_url'] = get_edit_input(
        "代码链接 (可选项，GitHub URL)，原",
        pub.get('code_url', ''),
        required=False,
        validator=code_url_validator
    )

    slides_url_validator = lambda x: validate_url(x, 'slides_url')
    pub['slides_url'] = get_edit_input(
        "幻灯片链接 (可选项，URL 或本地文件名)，原",
        pub.get('slides_url', ''),
        required=False,
        validator=slides_url_validator
    )

    video_url_validator = lambda x: validate_url(x, 'video_url')
    pub['video_url'] = get_edit_input(
        "视频链接，原",
        pub.get('video_url', ''),
        required=False,
        validator=video_url_validator
    )

    pub['hero_img'] = get_edit_input("封面图片，原", pub.get('hero_img', ''), required=False)
    return pub

def show_summary(pub: Dict[str, str], title: str = "输入摘要"):
    print("\n" + colorize("="*60, Colors.BRIGHT_CYAN))
    print_header(title)
    print(colorize("="*60, Colors.BRIGHT_CYAN))
    for key, value in pub.items():
        if value:
            print(f"  {colorize(key, Colors.BRIGHT_BLUE):15}: {value}")
    print(colorize("="*60, Colors.BRIGHT_CYAN))

def show_edit_diff(original: Dict[str, str], updated: Dict[str, str]):
    print("\n" + colorize("="*60, Colors.BRIGHT_CYAN))
    print_header("修改摘要")
    print(colorize("="*60, Colors.BRIGHT_CYAN))
    for key in sorted(set(list(original.keys()) + list(updated.keys()))):
        old_val = original.get(key, '')
        new_val = updated.get(key, '')
        if old_val == new_val:
            print(f"  {colorize(key, Colors.BRIGHT_BLACK):15}: {old_val}")
        else:
            print(f"  {colorize(key, Colors.BRIGHT_BLUE):15}: {colorize(old_val, Colors.BRIGHT_BLACK)} -> {colorize(new_val, Colors.BRIGHT_GREEN)}")
    print(colorize("="*60, Colors.BRIGHT_CYAN))

def _build_diff_lines(original: Dict[str, str], updated: Dict[str, str]) -> List[str]:
    lines: List[str] = []
    for key in sorted(set(list(original.keys()) + list(updated.keys()))):
        old_val = original.get(key, '')
        new_val = updated.get(key, '')
        shown_old_val = old_val if old_val else 'Null'
        shown_new_val = new_val if new_val else 'Null'
        if old_val == new_val:
            lines.append(f"  {key}: {shown_old_val}")
        else:
            lines.append(f"- {key}: {shown_old_val}")
            lines.append(f"+ {key}: {shown_new_val}")
            lines.append("")
    return lines

def curses_diff_view(stdscr, original: Dict[str, str], updated: Dict[str, str]) -> bool:
    curses.curs_set(0)
    stdscr.keypad(True)
    top = 0
    lines = _build_diff_lines(original, updated)
    instructions = "↑/↓ 滚动, s 保存, Esc 返回"
    while True:
        height, width = stdscr.getmaxyx()
        list_height = max(1, height - 3)
        stdscr.erase()
        stdscr.addnstr(0, 0, instructions, width - 1)
        stdscr.hline(1, 0, '-', width)
        for i in range(list_height):
            idx = top + i
            if idx >= len(lines):
                break
            stdscr.addnstr(2 + i, 0, lines[idx], width - 1)
        stdscr.refresh()
        key = stdscr.getch()
        if key in (curses.KEY_UP, ord('k')):
            top = max(0, top - 1)
        elif key in (curses.KEY_DOWN, ord('j')):
            top = min(max(0, len(lines) - list_height), top + 1)
        elif key in (curses.KEY_NPAGE,):
            top = min(max(0, len(lines) - list_height), top + list_height)
        elif key in (curses.KEY_PPAGE,):
            top = max(0, top - list_height)
        elif key in (ord('s'), ord('S')):
            return True
        elif key in (27, ord('q')):
            return False

def show_diff_and_choose_save(original: Dict[str, str], updated: Dict[str, str]) -> bool:
    if sys.stdin.isatty() and sys.stdout.isatty():
        try:
            return curses.wrapper(lambda stdscr: curses_diff_view(stdscr, original, updated))
        except curses.error:
            pass
    show_edit_diff(original, updated)
    return confirm_action("确认保存修改？")

def confirm_action(prompt: str) -> bool:
    answer = input(colorize(f"\n{prompt} (y/n): ", Colors.BRIGHT_YELLOW)).strip().lower()
    return answer == 'y'

def format_preview(entry: Dict[str, str], index: int) -> str:
    pub_date = entry.get('pub_date', '----')
    venue = entry.get('venue', '').strip() or 'N/A'
    title = entry.get('title', '').strip() or 'Untitled'
    max_title = 50
    if len(title) > max_title:
        title = title[:max_title - 1] + '…'
    return f"{index+1:>3}. {pub_date:<6} | {venue:<10} | {title}"

def curses_select_entry(stdscr, entries: List[Dict[str, str]]) -> Optional[int]:
    curses.curs_set(0)
    stdscr.keypad(True)
    highlight = 0
    top = 0
    height, width = stdscr.getmaxyx()
    list_height = max(1, height - 4)
    instructions = "↑/↓ 选择, Enter 确认, q 或 Esc 取消"
    while True:
        stdscr.erase()
        stdscr.addnstr(0, 0, instructions, width - 1)
        stdscr.hline(1, 0, '-', width)
        for idx in range(top, min(top + list_height, len(entries))):
            row = idx - top + 2
            preview = format_preview(entries[idx], idx)
            attr = curses.A_REVERSE if idx == highlight else curses.A_NORMAL
            stdscr.addnstr(row, 0, preview, width - 1, attr)
        stdscr.refresh()
        key = stdscr.getch()
        if key in (curses.KEY_UP, ord('k')):
            highlight = (highlight - 1) % len(entries)
        elif key in (curses.KEY_DOWN, ord('j')):
            highlight = (highlight + 1) % len(entries)
        elif key in (curses.KEY_ENTER, 10, 13):
            return highlight
        elif key in (27, ord('q')):
            return None
        if highlight < top:
            top = highlight
        elif highlight >= top + list_height:
            top = highlight - list_height + 1

def fallback_numeric_selector(entries: List[Dict[str, str]]) -> Optional[int]:
    print_warning("终端不支持箭头选择，使用数字选择模式")
    for idx, entry in enumerate(entries, start=1):
        print(format_preview(entry, idx - 1))
    print("  0. 取消")
    while True:
        choice = input(colorize("请选择要编辑的条目编号: ", Colors.BRIGHT_CYAN)).strip()
        if choice == '0':
            return None
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(entries):
                return idx
        print_warning("无效输入，请重新输入")

def select_entry(entries: List[Dict[str, str]]) -> Optional[int]:
    if not entries:
        return None
    if sys.stdin.isatty() and sys.stdout.isatty():
        try:
            return curses.wrapper(lambda stdscr: curses_select_entry(stdscr, entries))
        except curses.error:
            return fallback_numeric_selector(entries)
    return fallback_numeric_selector(entries)

def choose_file() -> Optional[tuple[str, Path]]:
    while True:
        print("\n" + "="*60)
        print("Publications 管理工具")
        print("="*60)
        print("\n请选择要操作的 publication 类型：")
        print("  1. books")
        print("  2. conference")
        print("  3. journal")
        print("  0. 退出")
        choice = input("\n请输入选项 (0-3): ").strip()
        if choice == '0':
            return None
        if choice in TSV_FILES:
            return TSV_FILES[choice]
        print_warning("无效的选项，请重新输入")

def choose_action(file_label: str) -> Optional[str]:
    print(f"\n已选择 {file_label}.tsv")
    print("请选择操作：")
    print("  1. 添加新条目")
    print("  2. 编辑已有条目")
    print("  0. 返回上一层")
    return input("请输入选项 (0-2): ").strip()

def add_entry_flow(file_type: str, file_path: Path, data: List[Dict[str, str]], columns: List[str]):
    new_pub = collect_publication_info(file_type)
    ensure_columns(new_pub, columns)
    show_summary(new_pub)
    if not confirm_action("确认添加此条目？"):
        print_warning("已取消添加")
        return
    data.append(new_pub)
    try:
        data.sort(key=lambda x: int(x.get('pub_date', '0') or '0'), reverse=True)
    except (ValueError, TypeError):
        pass
    write_tsv(file_path, data, columns)
    print_success(f"✅ 成功添加条目到 {file_path}")
    print_info(f"   文件现在包含 {len(data)} 条记录")

def edit_entry_flow(file_type: str, file_path: Path, data: List[Dict[str, str]], columns: List[str]):
    if not data:
        print_warning("当前文件没有可编辑的条目")
        return
    print_info(f"共有 {len(data)} 条记录，可选择条目进行编辑")
    while True:
        selected_index = select_entry(data)
        if selected_index is None:
            return
        original = dict(data[selected_index])
        updated = collect_publication_edits(file_type, existing=original)
        ensure_columns(updated, columns, fallback=original)
        should_save = show_diff_and_choose_save(original, updated)
        if not should_save:
            continue
        data[selected_index] = updated
        try:
            data.sort(key=lambda x: int(x.get('pub_date', '0') or '0'), reverse=True)
        except (ValueError, TypeError):
            pass
        write_tsv(file_path, data, columns)
        print_success(f"✅ 已更新第 {selected_index + 1} 条记录并写入 {file_path}")


def main():
    while True:
        selection = choose_file()
        if selection is None:
            print("退出程序")
            return
        file_type, file_path = selection
        data, columns = read_tsv(file_path)
        print(f"\n当前 {file_type}.tsv 中有 {len(data)} 条记录")
        edit_entry_flow(file_type, file_path, data, columns)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n已退出")
