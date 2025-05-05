from colorama import Fore, init
import webbrowser
import http.server
import socketserver
import threading
import os
import time

init()

class HtmlTag:
    def __init__(self, tag_name, *children, **props):
        self.tag_name = tag_name
        self.children = children
        if 'class_' in props:
            props['class'] = props.pop('class_')
        self.props = props
        self.hover_styles = {}

    def style(self, **styles):
        """
        Available CSS properties:
        - background_color
        - color
        - font_size
        - margin
        - padding
        - border
        - width
        - height
        - display
        - position
        - top
        - left
        - right
        - bottom
        - text_align
        - vertical_align
        - overflow
        - z_index
        - opacity
        - box_shadow
        - border_radius
        - flex
        - justify_content
        - align_items
        - grid_template_columns
        - grid_template_rows
        - gap
        """
        style_str = "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in styles.items())
        if 'style' in self.props:
            self.props['style'] += "; " + style_str
        else:
            self.props['style'] = style_str
        return self

    def on_hover(self, **styles):
        self.hover_styles.update(styles)
        return self

    def render(self, indent: int = 0) -> str:
        ind = "  " * indent
        props_parts = [f'{k}="{v}"' for k, v in self.props.items()]
        props_str = (" " + " ".join(props_parts)) if props_parts else ""

        css = ""
        if 'id' in self.props:
            selector = f"#{self.props['id']}:hover"
        elif 'class' in self.props:
            selector = f".{self.props['class']}:hover"
        else:
            selector = f"{self.tag_name}:hover"

        if self.hover_styles:
            hover_style_str = "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in self.hover_styles.items())
            css = f"<style>{selector} {{{hover_style_str}}}</style>"

        if not self.children:
            if self.tag_name in {'meta', 'img', 'input', 'br', 'hr', 'link'}:
                return f"{ind}<{self.tag_name}{props_str} />\n{css}"
            return f"{ind}<{self.tag_name}{props_str}></{self.tag_name}>\n{css}"

        inner = []
        for child in self.children:
            if isinstance(child, HtmlTag):
                inner.append(child.render(indent + 1))
            else:
                inner.append("  " * (indent + 1) + str(child))
        inner_str = "\n".join(inner)
        return f"{ind}<{self.tag_name}{props_str}>\n{inner_str}\n{ind}</{self.tag_name}>\n{css}"

class Html:
    def html(self, *children, **props): return HtmlTag('html', *children, **props)
    def head(self, *children, **props): return HtmlTag('head', *children, **props)
    def title(self, *children, **props): return HtmlTag('title', *children, **props)
    def base(self, **props): return HtmlTag('base', **props)
    def link(self, **props): return HtmlTag('link', **props)
    def meta(self, **props): return HtmlTag('meta', **props)
    def style(self, *children, **props): return HtmlTag('style', *children, **props)
    def script(self, *children, **props): return HtmlTag('script', *children, **props)
    def body(self, *children, **props): return HtmlTag('body', *children, **props)

    def section(self, *children, **props): return HtmlTag('section', *children, **props)
    def nav(self, *children, **props): return HtmlTag('nav', *children, **props)
    def article(self, *children, **props): return HtmlTag('article', *children, **props)
    def aside(self, *children, **props): return HtmlTag('aside', *children, **props)
    def header(self, *children, **props): return HtmlTag('header', *children, **props)
    def footer(self, *children, **props): return HtmlTag('footer', *children, **props)
    def h1(self, *children, **props): return HtmlTag('h1', *children, **props)
    def h2(self, *children, **props): return HtmlTag('h2', *children, **props)
    def h3(self, *children, **props): return HtmlTag('h3', *children, **props)
    def h4(self, *children, **props): return HtmlTag('h4', *children, **props)
    def h5(self, *children, **props): return HtmlTag('h5', *children, **props)
    def h6(self, *children, **props): return HtmlTag('h6', *children, **props)
    def main(self, *children, **props): return HtmlTag('main', *children, **props)
    def address(self, *children, **props): return HtmlTag('address', *children, **props)

    def p(self, *children, **props): return HtmlTag('p', *children, **props)
    def hr(self, **props): return HtmlTag('hr', **props)
    def br(self, **props): return HtmlTag('br', **props)
    def pre(self, *children, **props): return HtmlTag('pre', *children, **props)
    def blockquote(self, *children, **props): return HtmlTag('blockquote', *children, **props)
    def ol(self, *children, **props): return HtmlTag('ol', *children, **props)
    def ul(self, *children, **props): return HtmlTag('ul', *children, **props)
    def li(self, *children, **props): return HtmlTag('li', *children, **props)
    def dl(self, *children, **props): return HtmlTag('dl', *children, **props)
    def dt(self, *children, **props): return HtmlTag('dt', *children, **props)
    def dd(self, *children, **props): return HtmlTag('dd', *children, **props)
    def figure(self, *children, **props): return HtmlTag('figure', *children, **props)
    def figcaption(self, *children, **props): return HtmlTag('figcaption', *children, **props)
    def div(self, *children, **props): return HtmlTag('div', *children, **props)
    def a(self, *children, **props): return HtmlTag('a', *children, **props)
    def em(self, *children, **props): return HtmlTag('em', *children, **props)
    def strong(self, *children, **props): return HtmlTag('strong', *children, **props)
    def small(self, *children, **props): return HtmlTag('small', *children, **props)
    def s(self, *children, **props): return HtmlTag('s', *children, **props)
    def cite(self, *children, **props): return HtmlTag('cite', *children, **props)
    def q(self, *children, **props): return HtmlTag('q', *children, **props)
    def dfn(self, *children, **props): return HtmlTag('dfn', *children, **props)
    def abbr(self, *children, **props): return HtmlTag('abbr', *children, **props)
    def data(self, *children, **props): return HtmlTag('data', *children, **props)
    def time(self, *children, **props): return HtmlTag('time', *children, **props)
    def code(self, *children, **props): return HtmlTag('code', *children, **props)
    def var_(self, *children, **props): return HtmlTag('var', *children, **props)
    def samp(self, *children, **props): return HtmlTag('samp', *children, **props)
    def kbd(self, *children, **props): return HtmlTag('kbd', *children, **props)
    def sub(self, *children, **props): return HtmlTag('sub', *children, **props)
    def sup(self, *children, **props): return HtmlTag('sup', *children, **props)
    def i(self, *children, **props): return HtmlTag('i', *children, **props)
    def b(self, *children, **props): return HtmlTag('b', *children, **props)
    def u(self, *children, **props): return HtmlTag('u', *children, **props)
    def mark(self, *children, **props): return HtmlTag('mark', *children, **props)
    def ruby(self, *children, **props): return HtmlTag('ruby', *children, **props)
    def rt(self, *children, **props): return HtmlTag('rt', *children, **props)
    def rp(self, *children, **props): return HtmlTag('rp', *children, **props)
    def bdi(self, *children, **props): return HtmlTag('bdi', *children, **props)
    def bdo(self, *children, **props): return HtmlTag('bdo', *children, **props)
    def span(self, *children, **props): return HtmlTag('span', *children, **props)
    def ins(self, *children, **props): return HtmlTag('ins', *children, **props)
    def del_(self, *children, **props): return HtmlTag('del', *children, **props)
    def img(self, **props): return HtmlTag('img', **props)
    def iframe(self, *children, **props): return HtmlTag('iframe', *children, **props)
    def embed(self, **props): return HtmlTag('embed', **props)
    def object(self, *children, **props): return HtmlTag('object', *children, **props)
    def param(self, **props): return HtmlTag('param', **props)
    def video(self, *children, **props): return HtmlTag('video', *children, **props)
    def audio(self, *children, **props): return HtmlTag('audio', *children, **props)
    def source(self, **props): return HtmlTag('source', **props)
    def track(self, **props): return HtmlTag('track', **props)
    def canvas(self, *children, **props): return HtmlTag('canvas', *children, **props)
    def map(self, *children, **props): return HtmlTag('map', *children, **props)
    def area(self, **props): return HtmlTag('area', **props)
    def table(self, *children, **props): return HtmlTag('table', *children, **props)
    def caption(self, *children, **props): return HtmlTag('caption', *children, **props)
    def colgroup(self, *children, **props): return HtmlTag('colgroup', *children, **props)
    def col(self, **props): return HtmlTag('col', **props)
    def tbody(self, *children, **props): return HtmlTag('tbody', *children, **props)
    def thead(self, *children, **props): return HtmlTag('thead', *children, **props)
    def tfoot(self, *children, **props): return HtmlTag('tfoot', *children, **props)
    def tr(self, *children, **props): return HtmlTag('tr', *children, **props)
    def td(self, *children, **props): return HtmlTag('td', *children, **props)
    def th(self, *children, **props): return HtmlTag('th', *children, **props)
    def form(self, *children, **props): return HtmlTag('form', *children, **props)
    def fieldset(self, *children, **props): return HtmlTag('fieldset', *children, **props)
    def legend(self, *children, **props): return HtmlTag('legend', *children, **props)
    def label(self, *children, **props): return HtmlTag('label', *children, **props)
    def input(self, **props): return HtmlTag('input', **props)
    def button(self, *children, **props): return HtmlTag('button', *children, **props)
    def select(self, *children, **props): return HtmlTag('select', *children, **props)
    def datalist(self, *children, **props): return HtmlTag('datalist', *children, **props)
    def optgroup(self, *children, **props): return HtmlTag('optgroup', *children, **props)
    def option(self, *children, **props): return HtmlTag('option', *children, **props)
    def textarea(self, *children, **props): return HtmlTag('textarea', *children, **props)
    def output(self, *children, **props): return HtmlTag('output', *children, **props)
    def progress(self, *children, **props): return HtmlTag('progress', *children, **props)
    def meter(self, *children, **props): return HtmlTag('meter', *children, **props)
    def details(self, *children, **props): return HtmlTag('details', *children, **props)
    def summary(self, *children, **props): return HtmlTag('summary', *children, **props)
    def menu(self, *children, **props): return HtmlTag('menu', *children, **props)
    def menuitem(self, *children, **props): return HtmlTag('menuitem', *children, **props)
    def dialog(self, *children, **props): return HtmlTag('dialog', *children, **props)


def render(root: HtmlTag, filename: str = "index.html"):
    print(Fore.BLUE + "[i]" + Fore.LIGHTYELLOW_EX + " Render Started")
    reload_script = HtmlTag("script", """
        const last = {time: Date.now()};
        setInterval(() => {
            fetch(window.location.href + '?t=' + Date.now())
              .then(r => r.text())
              .then(text => {
                  if (!window._last_content) window._last_content = text;
                  if (window._last_content !== text) {
                      window._last_content = text;
                      location.reload();
                  }
              });
        }, 2000);
    """)
    if isinstance(root, HtmlTag) and root.tag_name == "html":
        for child in root.children:
            if isinstance(child, HtmlTag) and child.tag_name == "body":
                child.children += (reload_script,)
                break
        else:
            root.children += (HtmlTag("body", reload_script),)
    else:
        root = HtmlTag("html", root, HtmlTag("body", reload_script))

    html_doc = "<!DOCTYPE html>\n" + root.render()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(Fore.BLUE + "[✓]" + Fore.GREEN + " Render Done. result in" + Fore.MAGENTA + f" {filename}")

def run(root: HtmlTag, filename: str = "index.html", port: int = 8000):
    render(root, filename)

    handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer(("", port), handler)

    threading.Thread(target=server.serve_forever, daemon=True).start()

    url = f"http://localhost:{port}/{filename}"
    print(Fore.BLUE + "[i]" + Fore.LIGHTYELLOW_EX + f" Serving on {url}")
    webbrowser.open(url)

    last_mtime = os.path.getmtime(filename)
    try:
        while True:
            time.sleep(1)
            new_mtime = os.path.getmtime(filename)
            if new_mtime != last_mtime:
                print(Fore.YELLOW + "[~] Detected change, re-rendering...")
                render(root, filename)
                last_mtime = new_mtime
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Server shutting down.")
        server.shutdown()
