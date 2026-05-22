#!/usr/bin/env python3
import re

from .shared.segment_type import SegmentType

from .modules.frontmatter_parser import parse_frontmatter
from .modules.text_task_parser import parse_to_text_task
from .modules.info_text_parser import parse_to_information_text
from .modules.table_task_parser import parse_table_task
from .modules.single_choice_parser import parse_single_choice
from .modules.source_text_parser import parse_to_source_text

class MarkdownParser:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text

    def parse(self):

        sections = self._get_sections('<!-- Section -->')
        frontmatter = parse_frontmatter(sections[0])
        exercises = self._create_segments(sections[1])

        solutions = None
        if(len(sections) > 2):
            solutions = self._create_segments(sections[2])
        sources = None
        if(len(sections) > 3):
            sources = self._create_segments(sections[3])

        return {'frontmatter': frontmatter, 'exercises': exercises, 'solutions': solutions, 'sources': sources}

    def _create_segments(self, section):

        list_of_segments = []
        task_text = section
        segments = re.split(r'<!--\s*(\w+)\s*-->', task_text)
        segments = [s.strip() for s in segments if s.strip()]  # Remove empty sections and trim whitespace

        for index in range(0, len(segments), 2):
            typeAsString = segments[index].upper()
            type = SegmentType[typeAsString]

            match(type):
                case SegmentType.INFOTEXT:
                    segment = parse_to_information_text(segments[index + 1])    
                case SegmentType.TEXTTASK:
                    segment = parse_to_text_task(segments[index + 1])
                case SegmentType.TABLETASK:
                    segment = parse_table_task(segments[index + 1])
                case SegmentType.SINGLECHOICE:
                    segment = parse_single_choice(segments[index + 1])
                case SegmentType.SOURCES:
                    segment = parse_to_source_text(segments[index + 1])
                case _:
                    pass
            list_of_segments.append(segment)
        
        return list_of_segments

    def _strip_leading_content(self, section: str) -> str:
        match = re.search(r'<!--', section)
        if match:
            return section[match.start():]
        return section

    def _get_sections(self, section_delimiter):        
        sections = re.split(rf'^\s*{section_delimiter}\s*$', self.markdown_text, flags=re.MULTILINE)        
        sections = [s.strip() for s in sections if s.strip()]
        
        ### Remove all content which is not <!-- ... --> from the exercises and solutions section
        sections[1] = self._strip_leading_content(sections[1])
        sections[2] = self._strip_leading_content(sections[2])
 
        return sections
    