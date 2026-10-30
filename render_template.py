import jinja2
import json
from datetime import date

def render_index():
    data_json = json.loads(open('data.json').read())

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))  
    template = env.get_template('index.html.jinja2')

    rendered_html = template.render(
        personal_data = data_json['personal_data'],
        about_me_page = data_json['about_me_page'],
        resume_page = data_json['resume_page'],
        publication_page = data_json['publication_page'],
        portfolio_page = data_json['portfolio_page'],
        year = date.today().year,
    )

    with open('index.html', 'w') as f:
        f.write(rendered_html)

if __name__ == '__main__':
    render_index()