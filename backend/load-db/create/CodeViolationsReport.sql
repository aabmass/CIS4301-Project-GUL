CREATE TABLE CodeViolationsReport (
    ID                      NUMBER(6)       PRIMARY KEY,
    address_ID              INTEGER         NOT NULL,
    FOREIGN KEY(address_ID) REFERENCES      Address(ID),
    infractionDate          DATE            NOT NULL,
    violation               VARCHAR2(100),
    caseType                VARCHAR2(100),
    inspector               VARCHAR2(20),
    status                  VARCHAR2(20)
)
