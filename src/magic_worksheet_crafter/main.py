from .parser.markdown_parser import MarkdownParser
from .builder.document_builder import DocumentBuilder
from .config import load_config

def main(source_markdown: str, output_docx: str):
    with open(source_markdown, "r", encoding="utf-8") as f:
        markdown = f.read()

    parser = MarkdownParser(markdown)
    sections = parser.parse()

    config = load_config()
    builder = DocumentBuilder(
        output_docx,
        colors=[config.color_primary, config.color_secondary],
        logo_path=config.logo_path,
        icon_paths=config.icon_paths,
    )

    builder.build(sections)
    builder.save()

def cli():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("source_markdown", help="Path to the input Markdown file")
    parser.add_argument("output_docx", help="Path for the output DOCX file")
    args = parser.parse_args()
    main(args.source_markdown, args.output_docx)

if __name__ == "__main__":
    cli()
