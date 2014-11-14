CREATE TABLE Address (
    ID              NUMBER(6)      PRIMARY KEY,
    streetAddress   VARCHAR2(60)   NOT NULL,
    city            VARCHAR2(30)   NOT NULL,

    /* Coordinates given as latitude and longitude
     * (degrees) with 18 digits total, 16 to the right
     */
    coord_Lat       NUMBER(18, 16)  NOT NULL,
    coord_Lon       NUMBER(18, 16)  NOT NULL
)

-- Other table codes here...
