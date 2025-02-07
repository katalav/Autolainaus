ALTER SEQUENCE lainaus_lainausnumero_seq OWNED BY lainaus.lainausnumero;
ALTER TABLE lainaus ADD CONSTRAINT auto_lainaus_fk
FOREIGN KEY (rekisterinumero)
REFERENCES auto (rekisterinumero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;


ALTER TABLE lainaaja ADD CONSTRAINT ryhma_lainaaja_fk
FOREIGN KEY (ryhma)
REFERENCES ryhma (ryhma)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE lainaus ADD CONSTRAINT lainaaja_lainaus_fk
FOREIGN KEY (hetu)
REFERENCES lainaaja (hetu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;