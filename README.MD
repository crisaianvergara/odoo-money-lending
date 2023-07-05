python3 odoo-bin --addons-path=enterprise,addons,custom -d dblending -u money_lending,pos_custom,library_app --dev xml --xmlrpc-port=9000
python3 odoo-bin --addons-path=enterprise,addons,custom -d dblending -u money_lending,pos_custom,library_app --dev xml --xmlrpc-port=9000 --test-enable
python3 odoo-bin --addons-path=enterprise,addons,custom -d dblending -u money_lending,pos_custom,library_app,odoo_inheritance,cris_hospital,estate,estate_account --dev xml --xmlrpc-port=9000 --test-enable
<!-- Scaffold - creating odoo modules -->
./odoo-bin scaffold library_app custom