from ...builder.modules.header_footer import HeaderFooter
import yaml

def parse_frontmatter(frontmatter_text) -> HeaderFooter:
        yaml_content = frontmatter_text.strip()
        if yaml_content.startswith('---'):
            yaml_content = yaml_content[3:].lstrip('\n')
        if yaml_content.endswith('---'):
            yaml_content = yaml_content[:-3].rstrip('\n')
        data = yaml.safe_load(yaml_content)
        return HeaderFooter(
            teacher=data.get('teacher', ''),
            study=data.get('study', ''),
            gradeOfSchool=str(data.get('gradeOfSchool', '')),
            unit=data.get('unit', ''),
            topic=data.get('title', '')
        )
