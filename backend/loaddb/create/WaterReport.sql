CREATE TABLE WaterReport (
    ID                      NUMBER(6)       PRIMARY KEY,
    address_ID              INTEGER         NOT NULL,
    FOREIGN KEY(address_ID) REFERENCES      Address(ID),
    month                   VARCHAR2(9)     NOT NULL,
    year                    NUMBER(4)       NOT NULL,
    consumption             NUMBER(10)      NOT NULL
)
