import logging

from sqlalchemy import Column, types as DbTypes

from cyberjack_core.models import Model, CompanyMixin

from wafw00f.lib.evillib import oururlparse
from wafw00f.main import WafW00F

log = logging.getLogger('wafw00f')


class DSWaf(CompanyMixin, Model):
    __tablename__ = 'ds_wafs'

    waf_name = Column(DbTypes.String(100), index=True)
    num_of_requests = Column(DbTypes.Integer)


def run_wafw00f(targets, session):
    for target in targets:
        waf, attacker = _get_waf(target)
        _update_waf(target, waf, attacker, session)


def _get_waf(target):
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
    domain = target.replace('http://', '')
    domain = domain.replace('https://', '')
    ds_waf = session.query(DSWaf).filter_by(domain=domain).first()
    if ds_waf is None:
        ds_waf = DSWaf(domain=domain)
    ds_waf.waf_name = waf or ''
    ds_waf.num_of_requests = attacker.requestnumber
    session.add(ds_waf)
    session.commit()
