CREATE TABLE ADDRESS (
    ID              NUMBER(6)       PRIMARY KEY,
    STREETADDRESS   VARCHAR2(60)   NOT NULL,
    CITY            VARCHAR2(30)   NOT NULL,

    /* Coordinates given as latitude and longitude
     * (degrees) with 18 digits total, 16 to the right
     */
    COORD_LAT       NUMBER(18, 16)  NOT NULL,
    COORD_LON       NUMBER(18, 16)  NOT NULL
)

-- Other table codes here...
