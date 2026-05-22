from enum import Enum

# class syntax
class SegmentType(Enum):
    FRONTMATTER = 1
    INFOTEXT = 2
    TEXTTASK = 3
    SINGLECHOICE = 4
    TABLETASK = 5
    SOURCES = 6
