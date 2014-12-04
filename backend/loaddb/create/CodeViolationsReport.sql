CREATE TABLE CodeViolationsReport (
    ID                      NUMBER(6)       PRIMARY KEY,
    address_ID              INTEGER         NOT NULL,
    FOREIGN KEY(address_ID) REFERENCES      Address(ID),
    violation               VARCHAR2(100)   NOT NULL,
    caseType                VARCHAR2(100)   NOT NULL,
    inspector               VARCHAR2(20)    NOT NULL,
    status                  VARCHAR2(20)    NOT NULL
)
