import httpretty
from unittest import TestCase

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
        # create a waf record
        _update_waf(domain, waf, attacker, self.session)
        new_waf = self.session.query(DSWaf).first()
        self.assertTrue(new_waf.domain == domain)
        self.assertTrue(new_waf.waf_name)
        update_time = new_waf.update_time
        waf_name = new_waf.waf_name

        # verify waf record is updated if same waf found
        _update_waf(domain, waf, attacker, self.session)
        new_waf = self.session.query(DSWaf).first()
        self.assertTrue(new_waf.update_time > update_time)
        num_of_wafs = self.session.query(DSWaf).count()
        self.assertTrue(num_of_wafs == 1)

        # verify a new record is created if a new waf is found
        _update_waf(domain, 'some other waf', attacker, self.session)
        num_of_wafs = self.session.query(DSWaf).count()
        self.assertTrue(num_of_wafs == 2)

        # verify there is only 1 active waf
        num_of_active_wafs = self.session.query(DSWaf).filter_by(domain=domain,
                                                                 is_active=True).count()
        self.assertTrue(num_of_active_wafs == 1)

        # verify the old waf is NOT active
        num_of_active_wafs = self.session.query(DSWaf).filter_by(domain=domain,
                                                                 waf_name=waf_name,
                                                                 is_active=False).count()
        self.assertTrue(num_of_active_wafs == 1)

    @httpretty.activate
    def __generate_waf(self, host, vendor, fake_headers):
        httpretty.register_uri(httpretty.GET, 'http://%s/' % host, body='fake text', adding_headers=fake_headers)
        attacker = WafW00F(host)
        waf = 'some waf'
        return waf, attacker
