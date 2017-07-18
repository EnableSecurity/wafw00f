import logging
from datetime import datetime

from sqlalchemy import Column, types as DbTypes
from sqlalchemy.sql.schema import UniqueConstraint

from cyberjack_core.models import Model

from wafw00f.lib.evillib import oururlparse
from wafw00f.main import WafW00F

log = logging.getLogger('wafw00f')


class DSWaf(Model):
    __tablename__ = 'ds_wafs'

    id = Column(DbTypes.Integer, primary_key=True)
    create_time = Column(DbTypes.DateTime, default=datetime.utcnow)
    domain = Column(DbTypes.String(255), nullable=False, index=True)
    waf_name = Column(DbTypes.String(100), index=True)
    num_of_requests = Column(DbTypes.Integer)
    update_time = Column(DbTypes.DateTime, nullable=False, default=datetime.utcnow)
    is_active = Column(DbTypes.Boolean, nullable=False, default=True)

    UniqueConstraint('domain', 'waf_name')


def run_wafw00f(targets, session):
    """
    a wrapper around Wafw00f class, saving the results in the DB
    @param targets: list of domains or urls to scan
    @param session: SQLAlchemy DB session where the results are saved
    """
    for target in targets:
        waf, attacker = _get_waf(target)
        _update_waf(target, waf, attacker, session)


def _get_waf(target):
    """
    gets the waf name (or a list of names) of a domain
    @param target: a single domain or url to scan
    @return: waf name: (or list of names)
    @return: attacker: representing different data regarding the requests used to get the data
    """
    if not (target.startswith('http://') or target.startswith('https://')):
        log.info('The url %s should start with http:// or https:// .. fixing (might make this unusable)' % target)
        target = 'http://' + target
    pret = oururlparse(target)
    if pret is None:
        log.critical('The url %s is not well formed' % target)
        return None
    (hostname, port, path, query, ssl) = pret
    attacker = WafW00F(hostname, port=port, ssl=ssl, path=path)
    if attacker.normalrequest() is None:
        log.error('Site %s appears to be down' % target)
        return
    waf = attacker.identwaf(False)
    log.info('Ident WAF: %s' % waf)
    return waf, attacker


def _update_waf(target, waf, attacker, session):
    """
    writes the waf scan result to the DB
    @param target: the domain or url that was scanned
    @return: waf name: (or list of names)
    @return: attacker: representing different data regarding the requests used to get the data
    @param session: SQLAlchemy DB session where the results are saved
    """
    if type(waf) == list:
        waf = waf[0]
    waf = str(waf) or ''
    domain = target.replace('http://', '')
    domain = domain.replace('https://', '')
    old_waf = session.query(DSWaf).filter_by(domain=domain, is_active=True).first()
    if old_waf is None or old_waf.waf_name != waf:
        new_waf = DSWaf(domain=domain, waf_name=waf, num_of_requests=attacker.requestnumber)
        session.add(new_waf)
        if old_waf:
            old_waf.is_active = False
        session.commit()
    else:
        old_waf.update_time = datetime.utcnow()
        session.commit()
