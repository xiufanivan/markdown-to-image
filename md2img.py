import imgkit
import pypandoc

# 配置文件路径
md_file = "./markdown/test.md"
image_file = "./img/test.png"
html_file = "./html/test.html"

# 需要安装：wkhtmltox-0.12.5-1.msvc2015-win64.exe
# 下载地址：https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox-0.12.5-1.msvc2015-win64.exe
# 设置wkhtmltopdf的路径，本地安装路径，设置你的wkhtmltox安装路径
path_wk = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'


def html_to_image(html_file, image_file):
    # 将HTML转换为图片
    options = {
        'format': 'png',
        'encoding': 'UTF-8',
        'quiet': '',
        'disable-smart-width': ''
    }
    config = imgkit.config(wkhtmltoimage=path_wk)
    imgkit.from_file(html_file, image_file, options=options, config=config)


def markdown_to_image():
    # 将Markdown文件转换为HTML
    html_content = pypandoc.convert_file(md_file, 'html', format='md', outputfile=html_file)

    # 在生成的HTML中引入MathJax库和渲染公式的脚本
    html_with_mathjax = '''
    <html>
    <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/latest.js?config=TeX-AMS_HTML"></script>
    </head>
    <body>
    {}
    </body>
    </html>
    '''.format(html_content)

    html_to_image(html_file, image_file)


if __name__ == '__main__':
    markdown_to_image()
