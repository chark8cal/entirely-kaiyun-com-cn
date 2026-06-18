from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://www.entirely-kaiyun.com.cn"
SAMPLE_KEYWORD = "开云"

@dataclass
class Note:
    title: str
    content: str
    keyword: str
    url: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self) -> str:
        words = self.content.split()
        preview = " ".join(words[:10]) + ("..." if len(words) > 10 else "")
        return f"[{self.keyword}] {self.title}: {preview}"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "content": self.content,
            "keyword": self.keyword,
            "url": self.url,
            "tags": self.tags,
            "created_at": self.created_at,
        }

def format_note_simple(note: Note) -> str:
    return (
        f"=== {note.keyword.upper()} NOTE ===\n"
        f"Title: {note.title}\n"
        f"URL: {note.url}\n"
        f"Content: {note.content}\n"
        f"Tags: {', '.join(note.tags) if note.tags else 'なし'}\n"
        f"Created: {note.created_at}\n"
    )

def format_note_long(note: Note) -> str:
    separator = "=" * 50
    return (
        f"{separator}\n"
        f"  Keyword:   {note.keyword}\n"
        f"  Title:     {note.title}\n"
        f"  URL:       {note.url}\n"
        f"  Tags:      {' | '.join(note.tags) if note.tags else '—'}\n"
        f"  Created:   {note.created_at}\n"
        f"{separator}\n"
        f"  Content:\n"
        f"  {note.content}\n"
        f"{separator}\n"
    )

def format_note_compact(note: Note) -> str:
    tag_str = " ".join(f"#{t}" for t in note.tags) if note.tags else ""
    return f"{note.keyword} | {note.title} | {note.url} {tag_str} [{note.created_at}]"

def generate_example_notes() -> List[Note]:
    notes = [
        Note(
            title="开云平台介绍",
            content="这是一个关于开云的简要介绍，包含基础功能和使用说明。用户可以通过该平台获取多样化服务。",
            keyword=SAMPLE_KEYWORD,
            url=SAMPLE_URL,
            tags=["介绍", "平台"],
        ),
        Note(
            title="使用方法",
            content="开云的使用方法非常简单，首先访问官方网站，然后注册账户，即可开始体验所有功能。",
            keyword=SAMPLE_KEYWORD,
            url=SAMPLE_URL + "/guide",
            tags=["教程", "入门"],
        ),
        Note(
            title="常见问题FAQ",
            content="收集了开云用户最常询问的问题，包括账户安全、支付方式、技术支持等。",
            keyword=SAMPLE_KEYWORD,
            url=SAMPLE_URL + "/faq",
            tags=["帮助", "FAQ"],
        ),
    ]
    return notes

def show_all_notes(notes: List[Note], formatter=format_note_simple) -> None:
    for i, note in enumerate(notes, 1):
        print(f"Note #{i}")
        print(formatter(note))
        print()

def find_notes_by_keyword(notes: List[Note], keyword: str) -> List[Note]:
    return [n for n in notes if keyword.lower() in n.keyword.lower()]

if __name__ == "__main__":
    sample_notes = generate_example_notes()
    print(">>> All notes (simple format):")
    show_all_notes(sample_notes, format_note_simple)
    print("\n>>> All notes (long format):")
    show_all_notes(sample_notes, format_note_long)
    print("\n>>> All notes (compact format):")
    show_all_notes(sample_notes, format_note_compact)
    matched = find_notes_by_keyword(sample_notes, "开云")
    print(f"\n>>> Found {len(matched)} note(s) containing '开云'")
    for note in matched:
        print(note.summary())