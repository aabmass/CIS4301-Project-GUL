CREATE TABLE FireRescueEMSResponse (
    ID                      NUMBER(6)       PRIMARY KEY,
    address_ID              INTEGER         NOT NULL,
    FOREIGN KEY(address_ID) REFERENCES      Address(ID),
    responseDate            DATE            NOT NULL,
    callType                VARCHAR2(10),
    responseUnit            VARCHAR2(10)
)
