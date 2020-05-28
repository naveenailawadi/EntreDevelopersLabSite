from datetime import datetime
from flaskapp import db


class LeadModel(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)

    # contact information
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True)

    # message stuff
    subject = db.Column(db.String(100), nullable=True)
    message = db.Column(db.String(5000), nullable=False)

    # additional platforms --> store as dict
    additional_platforms = db.Column(db.String(400), nullable=True)

    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Lead('{self.name}', '{self.date_posted}')"


# create a model for storing SEOLab information
class SEOLabPurchaseModel(db.Model):
    __tablename__ = 'seo_lab_purchases'
    id = db.Column(db.Integer, primary_key=True)

    # contact information
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True)

    # SEO request stuff
    domain = db.Column(db.String(140), nullable=False)
    search_id = db.Column(db.String(72), nullable=True)  # keep this nullable to verify purchase first then send the request
    sale_price = db.Column(db.Float, nullable=False)
    sale_type = db.Column(db.String(50), nullable=False)

    purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"SEOLabPurchaseModel('{self.name}', '{self.date_posted}')"


# create a model for leads from jobs scraping
class JobScrapeLeadsModel(db.Model):
    __tablename__ = 'job_scrape_leads'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(150), nullable=True)
    location = db.Column(db.String(75), nullable=True)

    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contacted = db.Column(db.Boolean, nullable=False, default=False)


class InternalPasswordModel(db.Model):
    __tablename__ = 'internal_passwords'
    id = db.Column(db.Integer, primary_key=True)
    use = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
