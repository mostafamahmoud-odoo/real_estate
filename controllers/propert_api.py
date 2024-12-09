from odoo import http


class PropertApi(http.Controller):

    @http.route("/api/prpoerty" , methods=["GET"], type='http' , auth='none' ,csrf=False)
    def get_property_name(self):
        print("called from api")