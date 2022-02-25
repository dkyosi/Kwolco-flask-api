from flask_restful import Resource, reqparse
from app.api.countries.models import Countries

class GetCountries(Resource):
    """Get all countries"""
    def get(self):
        """Route to fetch all countries"""
        return Countries().get_countries()