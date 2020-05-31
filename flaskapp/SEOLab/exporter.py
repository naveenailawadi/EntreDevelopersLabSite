import flask
from flaskapp.SEOLab.researcher import Report
import jinja2


class Exporter:
    def __init__(self, template_name):
        # create a proper templating engine for universal use
        """
        Usage is the same as flask.render_template:

        render_without_request('my_template.html', var1='foo', var2='bar')
        """
        env = jinja2.Environment(
            loader=jinja2.PackageLoader('flaskapp', 'templates')
        )
        self.template = env.get_template(template_name)

    def create_report(self):
        # create a pdf of the report
        current_report = Report('https://entredeveloperslab.com', 'Easton, PA', 'some_id')

        html_rendering = self.template.render(report=current_report, flask=flask)

        # output to pdf
        return html_rendering
