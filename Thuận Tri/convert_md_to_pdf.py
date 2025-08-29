#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chuyển đổi file Markdown sang PDF
Tác giả: Hải - Middle AI Engineer
"""

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

def convert_markdown_to_pdf(md_file_path, output_pdf_path):
    """
    Chuyển đổi file Markdown sang PDF
    
    Args:
        md_file_path (str): Đường dẫn file Markdown
        output_pdf_path (str): Đường dẫn file PDF đầu ra
    """
    try:
        # Đọc nội dung file Markdown
        with open(md_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Chuyển đổi Markdown sang HTML với extensions
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
        html_content = md.convert(markdown_content)
        
        # CSS để định dạng PDF
        css_content = """
        @page {
            size: A4;
            margin: 2cm;
        }
        
        body {
            font-family: 'DejaVu Sans', Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.6;
            color: #333;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }
        
        h1 {
            font-size: 24pt;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.3em;
        }
        
        h2 {
            font-size: 20pt;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 0.2em;
        }
        
        h3 {
            font-size: 16pt;
        }
        
        p {
            margin-bottom: 1em;
            text-align: justify;
        }
        
        ul, ol {
            margin-bottom: 1em;
            padding-left: 2em;
            list-style-position: outside;
        }
        
        ul {
            list-style-type: disc;
        }
        
        li {
            margin-bottom: 0.5em;
            line-height: 1.6;
            padding-left: 0.5em;
        }
        
        li::marker {
            color: #3498db;
            font-weight: bold;
        }
        
        strong {
            color: #e74c3c;
            font-weight: bold;
        }
        
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        
        pre {
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1em;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        
        hr {
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 2em 0;
        }
        """
        
        # Tạo HTML hoàn chỉnh
        full_html = f"""
        <!DOCTYPE html>
        <html lang="vi">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Báo giá dự án WordPress và N8N</title>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Tạo font configuration
        font_config = FontConfiguration()
        
        # Chuyển đổi HTML sang PDF
        html_doc = HTML(string=full_html)
        css_doc = CSS(string=css_content, font_config=font_config)
        
        # Xuất PDF
        html_doc.write_pdf(output_pdf_path, stylesheets=[css_doc], font_config=font_config)
        
        print(f"✅ Chuyển đổi thành công! File PDF đã được lưu tại: {output_pdf_path}")
        
    except Exception as e:
        print(f"❌ Lỗi khi chuyển đổi: {str(e)}")
        return False
    
    return True

def main():
    """
    Hàm main để chạy script
    """
    # Đường dẫn file input và output
    input_file = "Bao_gia_du_an_WordPress_n8n_SEO.md"
    output_file = "Bao_gia_du_an_WordPress_n8n_SEO.pdf"
    
    # Kiểm tra file input có tồn tại không
    if not os.path.exists(input_file):
        print(f"❌ Không tìm thấy file: {input_file}")
        return
    
    print(f"🔄 Đang chuyển đổi {input_file} sang PDF...")
    
    # Thực hiện chuyển đổi
    success = convert_markdown_to_pdf(input_file, output_file)
    
    if success:
        print(f"🎉 Hoàn thành! File PDF: {output_file}")
    else:
        print("💥 Chuyển đổi thất bại!")

if __name__ == "__main__":
    main()