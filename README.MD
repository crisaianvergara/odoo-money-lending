python3 odoo-bin --addons-path=enterprise,addons,custom -d dblending -u money_lending,pos_custom,library_app --dev xml --xmlrpc-port=9000
python3 odoo-bin --addons-path=enterprise,addons,custom -d dblending -u money_lending,pos_custom,library_app --dev xml --xmlrpc-port=9000 --test-enable
python3 odoo-bin --addons-path=enterprise,addons,custom -d dblending -u money_lending,pos_custom,library_app,library_member,odoo_inheritance,cris_hospital,estate,estate_account --dev xml --xmlrpc-port=9000 --test-enable
<!-- Scaffold - creating odoo modules -->
./odoo-bin scaffold library_app custom

<!-- Current database -->
odoo-bin --addons-path=enterprise,addons,custom -d db-training -u money_lending,pos_custom,library_app,library_member,odoo_inheritance,cris_hospital,estate,estate_account --dev xml --xmlrpc-port=9000

<!-- Opening Shell -->
python3 odoo-bin --addons-path=enterprise,addons,custom shell -d db-training -u library_app,library_member --dev xml
<!-- Commands -->
>>> self
res.users(1,)
>>> self._name
'res.users'
>>> self.name
'OdooBot'
>>> self.login
'__system__'
<!-- Closing Shell -->
Ctrl + D

<!-- More commands -->
>>> self.env
<odoo.api.Environment object at 0x7f2df5c5a980>
>>> self.env.cr
<odoo.sql_db.Cursor object at 0x7f2df7267d00>
>>> self.env.user
res.users(1,)
>>> self.env.uid
1
>>> self.env.context
{'lang': 'en_US', 'tz': 'Europe/Brussels'}
>>> self.env.company
res.company(1,)
>>> self.env.companies
res.company(1,)
>>> self.env["res.partner"]
res.partner()
>>> self.env["res.partner"].search([("display_name", "like", "Azure")])
res.partner(14, 26, 33, 27)
>>> self.env.ref('base.user_root')
res.users(1,)
>>> self.env["res.partner"].search([("display_name", "like", "Lumber")])
res.partner(15, 34)
>>> self.env['res.partner'].browse([15,34])
res.partner(15, 34)

<!-- Continue PAge 17 -->

