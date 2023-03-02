from .db import db
from map.map import advance_delivery, DELIVERED

class Package(db.Model):
    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(20))
    recipient = db.Column(db.String(20))
    origin = db.Column(db.String(20))
    destination = db.Column(db.String(20))
    location = db.Column(db.String(20))

    @staticmethod
    def advance_all_location():
        packages = Package.query.all()
        for package in packages:
            if package.location is not DELIVERED:
                package.location = advance_delivery(package.location, package.destination)

        db.session.commit()
