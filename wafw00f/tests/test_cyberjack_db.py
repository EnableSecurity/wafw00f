from unittest import TestCase
import httpretty

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

from cyberjack_core.models import Model

from wafw00f.main import WafW00F
from wafw00f.cyberjack_wrapper import _update_waf, DSWaf


class WafDBTest(TestCase):

    def setUp(self):
        # set up sqlite test db
        engine = create_engine('sqlite://')
        Model.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def test_db(self):
        domain = 'hsht.hs3w.com'
        waf, attacker = self.__generate_waf(domain, 'West263CDN', {'X-Cache': 'MISS from WT263CDN-1231786'})
        _update_waf(domain, waf, attacker, self.session)
        new_waf = self.session.query(DSWaf).first()
        self.assertTrue(new_waf.domain == domain)
        self.assertTrue(new_waf.waf_name)

    @httpretty.activate
    def __generate_waf(self, host, vendor, fake_headers):
        httpretty.register_uri(httpretty.GET, 'http://%s/' % host, body='fake text', adding_headers=fake_headers)
        attacker = WafW00F(host)
        waf = attacker.wafdetections[vendor](attacker)
        return waf, attacker
