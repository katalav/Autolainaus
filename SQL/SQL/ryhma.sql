SELECT * FROM public.ryhma
ORDER BY ryhma ASC
CREATE TABLE ryhma (
                ryhma VARCHAR(50) NOT NULL,
                vastuuhenkilo VARCHAR(50),
                CONSTRAINT ryhma_pk PRIMARY KEY (ryhma)
)